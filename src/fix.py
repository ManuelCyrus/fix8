from core import Error

class fix8:

    def __init__(self, file: str) -> None:
        q, error_code, line, column = self.destructure(file)
        self.fix(q, error_code, line, column)

    def destructure(self, error: str) -> list:
        parts = [part.strip() for part in error.split(":")]
        file = parts[0]
        line = parts[1]
        column = parts[2]
        error_code = parts[3].split()[0]  
        return [file, error_code, line, column]

    def fix(self, file, error_code, line_error, column_error) -> None:

        if error := Error.check_error(error_code):

            with open(file) as q:
                lines = q.readlines()

            idx_line = int(line_error) - 1
            idx_column = int(column_error) - 1
            current_line = lines[idx_line]

            if error[1][1] == "a":
                char_to_add = error[1][2]

                fixed_line = (
                    current_line[:idx_column]
                    + char_to_add
                    + current_line[idx_column:]
                )

                lines[idx_line] = fixed_line

            with open(file, "w") as f:
                f.writelines(lines)