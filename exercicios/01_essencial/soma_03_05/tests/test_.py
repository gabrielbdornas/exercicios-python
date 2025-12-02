from soma_03_05.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(13)) == int, "Esperado um inteiro"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


@pytest.mark.parametrize("n, expected_result",[
    (5, 3),
    (10, 23),
    (20,78),
])
def test_options_resposta(n, expected_result):
    assert resposta(n) == expected_result, f"resposta({n}) deve ser igual a {expected_result}."