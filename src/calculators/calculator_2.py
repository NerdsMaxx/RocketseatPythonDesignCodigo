from typing import Dict, List

from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator2:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler


    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.get_json(force=True)
        input_data = self.__validate_body(body)
        result = self.__process_data(input_data)

        return self.__format_response(result)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('Body mal formado')

        try:
            result = [float(num) for num in list(body['numbers'])]
        except ValueError:
            raise HttpBadRequestError('A propriedade "numbers" deve ser array que contenha float')

        return result

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)

        return 1 / result

    def __format_response(self, calc_result: float) -> Dict:
        return {
            'data': {
                'Calculator': 2,
                'result': round(calc_result, 2)
            }
        }