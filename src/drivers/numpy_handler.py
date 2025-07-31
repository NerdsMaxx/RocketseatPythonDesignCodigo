from typing import List

import numpy

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):

    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return float(self.__np.std(numbers))

    def variance(self, numbers: List[float]) -> float:
        return float(self.__np.var(numbers))