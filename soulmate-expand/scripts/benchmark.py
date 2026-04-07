#!/usr/bin/env python3
from pathlib import Path
import sys

# Support both direct execution and module import
try:
    from .validate import validate
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from validate import validate

try:
    import tiktoken
    _enc = tiktoken.get_encoding("cl100k_base")
except ImportError:
    _enc = None


def count_tokens(text):
    if _enc is None:
        return len(text.split())  # fallback: word count
    return len(_enc.encode(text))


def benchmark_pair(orig_path: Path, expanded_path: Path):
    orig_text = orig_path.read_text()
    expanded_text = expanded_path.read_text()

    orig_tokens = count_tokens(orig_text)
    expanded_tokens = count_tokens(expanded_text)
    growth = 100 * (expanded_tokens - orig_tokens) / orig_tokens if orig_tokens > 0 else 0
    result = validate(orig_path, expanded_path)

    return (expanded_path.name, orig_tokens, expanded_tokens, growth, result.is_valid)


def print_table(rows):
    print("\n| File | Original | Expanded | Growth % | Valid |")
    print("|------|----------|----------|----------|-------|")
    for r in rows:
        print(f"| {r[0]} | {r[1]} | {r[2]} | +{r[3]:.1f}% | {'Yes' if r[4] else 'No'} |")


def main():
    # Direct file pair: python3 benchmark.py original.md expanded.md
    if len(sys.argv) == 3:
        orig = Path(sys.argv[1])
        expanded = Path(sys.argv[2])
        if not orig.exists():
            print(f"Not found: {orig}")
            sys.exit(1)
        if not expanded.exists():
            print(f"Not found: {expanded}")
            sys.exit(1)
        print_table([benchmark_pair(orig, expanded)])
        return

    # Glob mode: repo_root/tests/soulmate-expand/
    tests_dir = Path(__file__).parent.parent.parent / "tests" / "soulmate-expand"
    if not tests_dir.exists():
        print(f"Tests dir not found: {tests_dir}")
        sys.exit(1)

    rows = []
    for orig in sorted(tests_dir.glob("*.compressed.md")):
        expanded = orig.with_name(orig.stem.removesuffix(".compressed") + ".md")
        if expanded.exists():
            rows.append(benchmark_pair(orig, expanded))

    if not rows:
        print("No expanded file pairs found.")
        return

    print_table(rows)


if __name__ == "__main__":
    main()
