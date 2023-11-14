import pytest
from src.act2_3_4 import convertirAEntero


@pytest.mark.parametrize(
    "input_num, expected",
    [
        ("10",10),
        ("6",6),
        ("5", 5)
    ]
)
def test_convertirAEntero_params(input_num, expected):
    assert convertirAEntero(input_num) == expected


def test_num_noEntero():
    with pytest.raises(Exception):
        convertirAEntero("hola")