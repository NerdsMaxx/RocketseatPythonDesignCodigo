from typing import Dict, List
from .calculator_2 import Calculator2
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from ..drivers.numpy_handler import NumpyHandler


class MockResquest:
    def __init__(self, body: Dict) -> None:
        self.json = body

    def get_json(self, force: bool = False) -> Dict:
        return self.json

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3


# É TESTE UNITÁRIO POIS USA MOCK
def test_calculate():
    mock_request = MockResquest(body={ 'numbers': [1.45, 8.56, 8] })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print(response)

    # formato da resposta
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.33}}

# ELE TESTA A INTEGRAÇÃO ENTRE NUMPY HANDLER COM CALCULATOR 2, MAS O PROF QUER TESTE UNITÁRIO
def test_calculate_integration():
    mock_request = MockResquest(body={ 'numbers': [1.45, 8.56, 8] })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print(response)

    # formato da resposta
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.04}}