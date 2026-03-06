from collections import defaultdict
from rules import RULES


def generate_patches(parsed):
    patches = []
    for file, line, column, code in parsed:
        if code not in RULES:
            continue
        action, char = RULES[code]
        patches.append((line, column, action, char))
    return patches


def sort_patches(patches):
    return sorted(patches, key=lambda p: (p[0], -p[1]))


def group_patches(patches):
    grouped = defaultdict(list)
    for line, column, action, char in patches:
        grouped[line].append((column, action, char))
    return grouped
