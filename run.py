from flask import jsonify

from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.main.server.server import app

@app.errorhandler(HttpBadRequestError)
@app.errorhandler(HttpUnprocessableEntityError)
def handle_known_http_exceptions(error):
    """
    Este handler captura todas as exceções dos tipos
    HttpBadRequestError e HttpUnprocessableEntityError.
    """
    response = {
        'errors': [{
            'title': error.name,
            'detail': error.message
        }]
    }
    # Retorna o JSON formatado e o status code do próprio erro
    return jsonify(response), error.status_code


@app.errorhandler(Exception)
def handle_generic_exception(error):
    """
    Este é um handler "catch-all". Ele captura qualquer exceção
    que não tenha um handler específico.
    É perfeito para erros inesperados (500 Internal Server Error).
    """
    response = {
        'errors': [{
            'title': 'Server Error',
            'detail': 'Ocorreu um erro inesperado no servidor.'
        }]
    }

    return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)