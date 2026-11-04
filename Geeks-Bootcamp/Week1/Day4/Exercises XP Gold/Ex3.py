

def sum_series(x: int) -> int:
    str_x = str(x)
    term1 = int(str_x)
    term2 = int(str_x * 2)
    term3 = int(str_x * 3)
    term4 = int(str_x * 4)
    return term1 + term2 + term3 + term4
resultat = sum_series(3)
print(f"Résultat pour X = 3 : {resultat}")  