from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from ..drivers.numpy_handler import NumpyHandler

class MockResquest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self, force: bool = False) -> Dict:
        return self.json

class MockDriverHandlerError():
    def variance(self, numbers: List[float]) -> float:
        raise Exception('A variância é maior que multiplicação')

class MockDriverHandler():
    def variance(self, numbers: List[float]) -> float:
        return 3

def test_calculate_with_variance_error():
    mock_request = MockResquest({ "numbers": [1, 2, 3, 4, 5] })
    calculate_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculate_3.calculate(mock_request)
        assert str(excinfo.value) == 'A variância é maior que multiplicação'


def test_calculate():
    mock_request = MockResquest({"numbers": [1, 100, 1, 1, 100]})
    calculate_3 = Calculator3(MockDriverHandler())

    response = calculate_3.calculate(mock_request)

    # formato da resposta
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 3, 'result': {'value': 3, 'Sucess': True}}}