from patches import group_patches


def apply_patches(file, patches):
    if not patches:
        return

    with open(file) as f:
        lines = f.readlines()

    grouped = group_patches(patches)

    # Aplicar de baixo para cima para não quebrar índices
    for line in sorted(grouped.keys(), reverse=True):
        operations = sorted(grouped[line], reverse=True)
        idx_line = line - 1

        # Evita erros se o índice for maior que o número de linhas
        if idx_line >= len(lines):
            continue

        current = lines[idx_line]

        for column, action, char in operations:
            idx_column = column - 1

            if action == "add":
                if char is None:
                    continue
                current = current[:idx_column] + char + current[idx_column:]

            elif action == "delete":
                if 0 <= idx_column < len(current):
                    current = current[:idx_column] + current[idx_column+1:]

            elif action == "add_line":
                if char is None:
                    char = "\n"
                # Insere apenas se não houver uma linha em branco já
                if idx_line > 0 and lines[idx_line-1].strip() == "":
                    continue
                lines.insert(idx_line, char)

            elif action == "add_blank":
                # char aqui é o número de linhas que devem existir
                required = char
                blank_count = 0
                i = idx_line - 1
                while i >= 0 and lines[i].strip() == "":
                    blank_count += 1
                    i -= 1
                missing = required - blank_count
                for _ in range(max(0, missing)):
                    lines.insert(idx_line, "\n")

            elif action == "delete_blank":
                # remove linhas em excesso acima da linha
                i = idx_line - 1
                while i >= 0 and lines[i].strip() == "":
                    lines.pop(i)
                    i -= 1

        lines[idx_line] = current

    with open(file, "w") as f:
        f.writelines(lines)