#!/usr/bin/env python3
"""
Soulmate Expand CLI

Usage:
    soulmate-expand <filepath>
"""

import sys
from pathlib import Path

from .expand import expand_file
from .detect import detect_file_type, should_expand


def print_usage():
    print("Usage: soulmate-expand <filepath>")


def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    filepath = Path(sys.argv[1])

    # Check file exists
    if not filepath.exists():
        print(f"File not found: {filepath}")
        sys.exit(1)

    if not filepath.is_file():
        print(f"Not a file: {filepath}")
        sys.exit(1)

    # Detect file type
    file_type = detect_file_type(filepath)

    print(f"Detected: {file_type}")

    # Check if expandable
    if not should_expand(filepath):
        print("Skipping: file is not natural language (code/config)")
        sys.exit(0)

    print("Starting soulmate expansion...\n")

    try:
        success = expand_file(filepath)

        if success:
            print("\nExpansion completed successfully")
            backup_path = filepath.with_name(filepath.stem + ".compressed.md")
            print(f"Expanded:   {filepath}")
            print(f"Compressed: {backup_path}")
            sys.exit(0)
        else:
            print("\nExpansion failed after retries")
            sys.exit(2)

    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)

    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
