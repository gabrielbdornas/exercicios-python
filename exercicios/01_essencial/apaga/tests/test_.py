from apaga.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta('kitten', 4) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta('kitten', 4)) == str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"

def test_options_resposta():
    assert resposta('kitten', 4) == 'kittn' , f"Esperado valor 'kittn'"
    assert resposta('kitten', 1 ) == 'ktten' , f"Esperado valor 'ktten'"
    assert resposta('kitten', 0) == 'itten', f"Esperado valor 'kitten'"

def test_string_len():
    assert len(resposta('kitten', 4)) == len('kitten') - 1