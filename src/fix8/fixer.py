from .patches import group_patches

def apply_patches(file, patches):
    if not patches:
        return

    with open(file, "r") as f:
        lines = f.readlines()

    grouped = group_patches(patches)

    # Processar de baixo para cima para não quebrar os índices das linhas superiores
    for line_num in sorted(grouped.keys(), reverse=True):
        operations = sorted(grouped[line_num], reverse=True)
        idx_line = line_num - 1

        if idx_line >= len(lines):
            continue

        current = lines[idx_line]

        for column, action, char in operations:
            idx_column = column - 1

            if action == "add":
                if char is not None:
                    # Garante que char é string
                    val = str(char)
                    current = current[:idx_column] + val + current[idx_column:]

            elif action == "delete":
                if 0 <= idx_column < len(current):
                    current = current[:idx_column] + current[idx_column+1:]

            elif action == "add_line":
                # Se char for número (ex: E302 precisa de 2), insere essa quantidade
                num_lines = char if isinstance(char, int) else 1
                for _ in range(num_lines):
                    lines.insert(idx_line, "\n")
                    idx_line += 1 

            elif action == "add_blank":
                required = char if isinstance(char, int) else 1
                blank_count = 0
                i = idx_line - 1
                while i >= 0 and lines[i].strip() == "":
                    blank_count += 1
                    i -= 1
                missing = max(0, required - blank_count)
                for _ in range(missing):
                    lines.insert(idx_line, "\n")
                    idx_line += 1

            elif action == "delete_blank":
                i = idx_line - 1
                # Remove linhas em branco ACIMA da linha atual
                while i >= 0 and lines[i].strip() == "":
                    lines.pop(i)
                    idx_line -= 1
                    i -= 1

        # Atualiza a linha que foi modificada (ou que "desceu" devido aos inserts)
        if idx_line < len(lines):
            lines[idx_line] = current

    with open(file, "w") as f:
        f.writelines(lines)
