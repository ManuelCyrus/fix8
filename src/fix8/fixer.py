from patches import group_patches


def apply_patches(file, patches):

    if not patches:
        return

    with open(file) as f:
        lines = f.readlines()

    grouped = group_patches(patches)

    for line in grouped:
        operations = sorted(grouped[line], reverse=True)
        idx_line = line - 1
        current = lines[idx_line]

        for column, action, char in operations:
            idx_column = column - 1

            if action == "add":
                current = current[:idx_column] + char + current[idx_column:]
            elif action == "delete":
                if 0 <= idx_column < len(current):
                    current = current[:idx_column] + current[idx_column+1:]
            elif action == "add_line":
                lines.insert(idx_line, char)

        lines[idx_line] = current

    with open(file, "w") as f:
        f.writelines(lines)
