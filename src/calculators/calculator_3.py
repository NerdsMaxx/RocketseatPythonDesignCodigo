from functools import reduce
from typing import Dict, List, Tuple

from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator3:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler


    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.get_json(force=True)
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        response = self.__format_response(variance)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('Body mal formado')

        try:
            result = [float(num) for num in list(body['numbers'])]
        except ValueError:
            raise HttpBadRequestError('A propriedade "numbers" deve ser array que contenha float')

        return result

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        if len(numbers) == 0:
            raise HttpBadRequestError('Não é possível calcular multiplicação sem números')

        multiplication = reduce(lambda x, y: x * y, numbers)
        return multiplication

    def __verify_results(self, varience: float, multiplication: float) -> None:
        if varience >= multiplication:
            raise HttpBadRequestError('A variância é maior que multiplicação')

    def __format_response(self, variance: float) -> Dict:
        return {
            'data': {
                'Calculator': 3,
                'result': {
                    'value': variance,
                    'Sucess': True
                }
            }
        }