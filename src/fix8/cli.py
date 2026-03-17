import argparse
from pathlib import Path
from .runner import run_fix


class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[32m"
    WARNING = "\033[33m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


def main():
    parser = argparse.ArgumentParser(
        description="Automatically fix Flake8 errors in Python files or directories.",
        epilog="Example usage: fix8 my_script.py my_folder/"
    )

    parser.add_argument(
        "paths",
        nargs="+",
        help="One or more Python files or directories to process."
    )

    args = parser.parse_args()

    print(f"{Colors.HEADER}{Colors.BOLD}Starting: Looking for Python files...{Colors.ENDC}")

    python_files = []

    for path in args.paths:
        p = Path(path)
        if p.is_dir():
            python_files.extend(p.rglob("*.py"))
        elif p.is_file() and p.suffix == ".py":
            python_files.append(p)
        else:
            print(f"{Colors.WARNING}[Warning]{Colors.ENDC} Skipping '{p}': not a Python file or directory.")

    print(f"{Colors.OKBLUE}Files found: {len(python_files)}{Colors.ENDC}")

    if not python_files:
        print(f"{Colors.FAIL}No Python files found to process. Exiting.{Colors.ENDC}")
        return

    print(f"{Colors.OKCYAN}Starting fixer... Fixing files, it may take a few seconds...{Colors.ENDC}")

    for file in python_files:
        print(f"{Colors.OKBLUE}Processing: {file}{Colors.ENDC}")
        run_fix(str(file))

    print(f"{Colors.OKGREEN}\nAll files fixed!{Colors.ENDC}")

    print(f"{Colors.BOLD}Don't forget to contribute to this project! {Colors.ENDC}", end="->")
    print(f"{Colors.OKBLUE}https://github.com/ManuelCyrus/fix8{Colors.ENDC}")


if __name__ == "__main__":
    main()
