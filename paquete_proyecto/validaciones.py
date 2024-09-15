import re

def validar(entrada):
    if re.match(r"^-?\d+$",entrada):
        return 1
    else:
        return 0