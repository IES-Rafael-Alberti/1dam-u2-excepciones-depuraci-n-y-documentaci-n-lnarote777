import pytest
from src.act2_3_3 import cuenta_atras


@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0. "),
        (6, "6, 5, 4, 3, 2, 1, 0. "),
        (5, "5, 4, 3, 2, 1, 0. ")
    ]
)
def test_cuenta_atras_params(input_num, expected):
    assert cuenta_atras(input_num) == expected


def test_num_menorCero():
    with pytest.raises(ValueError):
        cuenta_atras(-4)