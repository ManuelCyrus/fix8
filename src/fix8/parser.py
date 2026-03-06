def parse_errors(errors):
    parsed = []
    for err in errors:
        parts = err.split(":")
        file = parts[0]
        line = int(parts[1])
        column = int(parts[2])
        code = parts[3].split()[0]
        parsed.append((file, line, column, code))
    return parsed
