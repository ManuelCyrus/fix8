RULES = {
    # Espaços em torno de operadores
    "E225": ("add", " "),   # missing whitespace around operator
    "E226": ("add", " "),   # missing whitespace around arithmetic operator
    "E227": ("add", " "),   # missing whitespace around bitwise or shift operator
    "E228": ("add", " "),   # missing whitespace around modulo operator

    # Linhas em branco
    "E301": ("add_line", "\n"),  # expected 1 blank line before function/class
    "E302": ("add_line", "\n"),  # expected 2 blank lines before top-level function
    "E303": ("add_line", "\n"),  # too many blank lines
    "W293": ("delete", None),     # blank line contains whitespace
    "W391": ("delete", None),     # blank line at end of file

    # Final de arquivo
    "W292": ("add", "\n"),  # no newline at end of file

    # Espaços desnecessários
    "W291": ("delete", None),  # trailing whitespace

    # Indentação
    "E111": ("delete", None),  # indentation is not a multiple of four
    "E114": ("delete", None),  # indentation is not a multiple of four (closing bracket)

    # Outras formatações simples
    "E701": ("add", " "),   # multiple statements on one line (simple split)
    "E702": ("add", "\n"),  # multiple statements on one line (split by newline)
}
