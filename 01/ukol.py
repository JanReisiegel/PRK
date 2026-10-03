# Úkol na 5. 10. 2026
import re

tests_colors = {
    "valid": [
        'color "green"',
        'color "dark-blue"',
        'color "red"',  # prázdný řetězec je syntakticky stále platný řetězec
    ],
    "invalid": [
        'color green',           # chybí uvozovky
        'color "red\nblue"',     # obsahuje konec řádku uvnitř
        'color "yellow"red"',  # neukončený/neplatný uvozovkami uvnitř
    ],
}

tests_operators = {
    "valid": [
        "a <= b",
        "c == d",
        "a = c + d",
    ],
    "invalid": [
        "a === b",  # nepovolený tříznakový operátor
        "if(true && false)",   # operátor, který v sadě není
        "i++",  # identifikátor/číslo, ne operátor
    ],
}

tests_comment = {
    "valid": [
        "a = 5 ; toto je komentář",
        ";",                     # samostatný středník na řádku
        "; vpravo 90; znova ;",  # středníky uvnitř komentáře nevadí
        """; první komentář
        ; druhý komentář""",  # více řádků, každý začíná středníkem
    ],
    "invalid": [
        "a = 5 toto neni komentar",    # nezačíná středníkem
        "// c-style komentar",   # špatný úvodní znak
        "# python styl komentar",   # obsahuje znak nového řádku Tady
    ],
}


def test_regex(name, pattern, valid_cases, invalid_cases):
    '''function for run tests on regex pattern'''
    print(f"Testing {name}: {pattern}")
    print("Valid cases:")
    for case in valid_cases:
        matches = re.findall(pattern, case)
        if matches:
            print(f"\tPASS: '{case}' matched as expected.")
            for match in matches:
                print(f"\t\tMatched: '{match}'")
        else:
            print(f"\tFAIL: '{case}' should be valid but did not match.")
    print("Invalid cases:")
    for case in invalid_cases:
        matches = re.findall(pattern, case)
        if matches:
            print(f"\tFAIL: '{case}' should be invalid but matched.")
            for match in matches:
                print(f"\t\tMatched: '{match}'")
        else:
            print(f"\tPASS: '{case}' did not match as expected.")


if __name__ == "__main__":
    COLORS_PATTERN = r'[ ]+\"[^\"\n]+\"$'
    OPERATORS_PATTERN = r' (<=|>=|==|!=|[+\-*/<>=()\[\],]) '
    COMMENTS_PATTERN = r';(.*)$'

    test_regex(
        "Colors",
        COLORS_PATTERN,
        tests_colors["valid"],
        tests_colors["invalid"])
    test_regex(
        "Operators",
        OPERATORS_PATTERN,
        tests_operators["valid"],
        tests_operators["invalid"])
    test_regex(
        "Comments",
        COMMENTS_PATTERN,
        tests_comment["valid"],
        tests_comment["invalid"])
