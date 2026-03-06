class Error:
    FLAKE8_FIXES = {
        "E225": ("missing whitespace around operator", "a", " "),
        "W292": ("no newline at end of file", "a", "\n"),
        "W291": ("trailing whitespace", "d", " "),
    }

    @staticmethod
    def check_error(search_code: str) -> list:
        for error, info in Error.FLAKE8_FIXES.items():
            if search_code in error:
                return [error, info]
        return []
