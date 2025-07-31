from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockResquest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self, force: bool = False) -> Dict:
        return self.json

def test_calculate():
    mock_request = MockResquest(body={ 'number': 1 })

    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)
    print(response)

    # formato da resposta
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # Assertividade da Resposta
    assert response['data']['result'] == 14.25
    assert response['data']['Calculator'] == 1

def test_calculate_with_body_error():
    mock_request = MockResquest(body={ 'something': 1 })
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == 'Body mal formado'

    mock_request = MockResquest(body={'number': 'testando'})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == 'A propriedade "number" deve ser float'

def test_something():
    print('Estou aqui no teste 1')
    pass

def test_something2():
    print('Estou aqui no teste 2')
    pass

def something3():
    print('Este método não vai ser acionada pois não tem prefixo "test_"')
    pass