import subprocess
from parser import parse_errors
from patches import generate_patches, sort_patches
from fixer import apply_patches
from rules import RULES


def run_fix(file):
    while True:
        result = subprocess.run(
            ["flake8", file],
            capture_output=True,
            text=True
        )
        errors = result.stdout.splitlines()

        relevant_errors = [e for e in errors if e.split(":")[3].split()[0] in RULES]

        if not relevant_errors:
            break

        parsed = parse_errors(relevant_errors)
        patches = generate_patches(parsed)
        patches = sort_patches(patches)
        apply_patches(file, patches)
