import argparse
from pathlib import Path
from runner import run_fix


def main():
    parser = argparse.ArgumentParser(
        description="Fix flake8 errors automatically in files or directories"
    )

    parser.add_argument(
        "paths",
        nargs="+",
        help="Python file(s) or directory(ies) to fix"
    )

    args = parser.parse_args()

    python_files = []

    for path in args.paths:
        p = Path(path)
        if p.is_dir():
            python_files.extend(p.rglob("*.py"))  # busca recursiva
        elif p.is_file() and p.suffix == ".py":
            python_files.append(p)
        else:
            print(f"Skipping {p}, not a Python file or directory")

    for file in python_files:
        print(f"Processing {file}")
        run_fix(str(file))


if __name__ == "__main__":
    main()
