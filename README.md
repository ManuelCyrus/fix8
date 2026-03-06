# fix8

**Version:** `0.1.0`  

**fix8** is an automated tool designed to detect and fix common **Flake8 / PEP8** style issues in Python projects. It automatically handles spacing, trailing whitespace, blank lines, and other common formatting problems.

---

##  Features

- **Automated Correction:** Detects and fixes common Python style issues without manual intervention.
- **Recursive Support:** Works on **multiple files** or **entire directories** recursively.
- **Efficiency:** Handles multiple errors on the same line.
- **CLI Ready:** Simple Command Line Interface for quick usage in projects or CI/CD pipelines.

---

##  How it Works

The `fix8` workflow follows a persistent correction cycle:

1. **Scan:** Runs `flake8` on the target file(s) or directory.
2. **Detect:** Identifies errors that match the built-in rule set.
3. **Patch:** Generates specific patches to fix the errors automatically.
4. **Loop:** Applies patches in a loop until no known errors remain.

---

##  Installation

### Via Pip
```bash
pip install fixer8
```


## Usage
fix8 is flexible and can be pointed at specific files or full project structures.

Fix a single file:


```bash
fix8 path/to/file.py
```
Fix multiple files:

```bash
Bash
fix8 file1.py file2.py or fix8 .
```

Mix files and directories:
```bash
fix8 file1.py src/ tests/
```
## Supported Rules
The following rules are currently supported for automated fixing:
- E225,Missing whitespace around operator,add
- E226,Missing whitespace around arithmetic operator,add
- E227,Missing whitespace around bitwise or shift operator,add
- E228,Missing whitespace around modulo operator,add
- E301,Expected 1 blank line before function/class,add_line
- E302,Expected 2 blank lines before top-level function,add_line
- E303,Too many blank lines,delete_line
- W291,Trailing whitespace,delete
- W292,No newline at end of file,add
- W293,Blank line contains whitespace,delete
- W391,Blank line at end of file,delete
- E111,Indentation is not a multiple of four,fix
- E114,Indentation is not a multiple of four (closing bracket),fix
- E701,Multiple statements on one line (simple split),add_newline
- E702,Multiple statements on one line (split by newline),add_newline