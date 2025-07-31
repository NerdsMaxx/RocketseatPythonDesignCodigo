from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler


def calculator_2_factory():
    numpu_handler = NumpyHandler()
    calculator_2 = Calculator2(numpu_handler)

    return calculator_2