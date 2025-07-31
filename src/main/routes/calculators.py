from flask import Blueprint, jsonify, request

from src.errors.error_controller import route_error_handler
from src.main.factories.calculator_1_factory import calculator_1_factory
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_3_factory import calculator_3_factory

calc_route_bp = Blueprint("calc_route", __name__, url_prefix='/calculator')

@calc_route_bp.post('/1')
def calculator_1():
    calc = calculator_1_factory()
    result = calc.calculate(request)

    return jsonify(result), 200

@calc_route_bp.post('/2')
def calculator_2():
    calc = calculator_2_factory()
    result = calc.calculate(request)

    return jsonify(result), 200

@calc_route_bp.post('/3')
def calculator_3():
    calc = calculator_3_factory()
    result = calc.calculate(request)

    return jsonify(result), 200