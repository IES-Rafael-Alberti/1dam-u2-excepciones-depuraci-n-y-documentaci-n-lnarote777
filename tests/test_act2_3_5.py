import pytest
from src.act2_3_5 import comprobarPassword


@pytest.mark.parametrize(
    "input_password, expected",
    [
        ("contraseña", "Tu contraseña coincide con la mía."),
        ("COntrAseÑa", "Tu contraseña coincide con la mía.")
    ]
)
def test_comprobarPassword_params(input_password, expected):
    assert comprobarPassword(input_password) == expected


def test_password_menorCero():
    with pytest.raises(NameError):
        comprobarPassword("PicaPiedra")