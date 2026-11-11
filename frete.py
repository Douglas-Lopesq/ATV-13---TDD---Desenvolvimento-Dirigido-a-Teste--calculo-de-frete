def calcular_frete(peso_gramas: int) -> int:
    if peso_gramas <= 0 or peso_gramas > 10_000:
        raise ValueError("Peso deve estar entre 1 e 10.000 gramas.")

    if peso_gramas <= 1_000:
        return 10

    if peso_gramas <= 5_000:
        return 20

    return 30
