import pytest
from src.act2_3_2 import impares


@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, "1, 3, 5, 7, 9, "),
        (6, "1, 3, 5, "),
        (5, "1, 3, 5. ")
    ]
)
def test_impares_params(input_num, expected):
    assert impares(input_num) == expected


def test_impares_menorCero():
    with pytest.raises(ValueError):
        impares(-4)