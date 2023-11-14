import pytest
from src.act2_3_1 import edad_cumplida


@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (10, "1, 2, 3, 4, 5, 6, 7, 8, 9, 10 años. "),
        (6, "1, 2, 3, 4, 5, 6 años. "),
        (5, "1, 2, 3, 4, 5 años. ")
    ]
)
def test_edad_cumplida_params(input_edad, expected):
    assert edad_cumplida(input_edad) == expected


def test_edad_menorCero():
    with pytest.raises(ValueError):
        edad_cumplida(-4)