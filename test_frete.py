import pytest

from frete import calcular_frete


@pytest.mark.parametrize(
    "peso_gramas, valor_esperado",
    [
        (1, 10),
        (500, 10),
        (1000, 10),
        (1001, 20),
        (2000, 20),
        (5000, 20),
        (5001, 30),
        (6000, 30),
        (10000, 30),
    ],
)
def test_calcular_frete_por_faixa(peso_gramas, valor_esperado):
    assert calcular_frete(peso_gramas) == valor_esperado


@pytest.mark.parametrize("peso_gramas", [0, -1])
def test_calcular_frete_entradas_invalidas(peso_gramas):
    with pytest.raises(ValueError):
        calcular_frete(peso_gramas)


@pytest.mark.parametrize("peso_gramas", [10001])
def test_calcular_frete_acima_do_limite(peso_gramas):
    with pytest.raises(ValueError):
        calcular_frete(peso_gramas)
