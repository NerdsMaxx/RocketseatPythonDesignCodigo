from functools import wraps
from typing import Callable, Any, Dict
from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


def route_error_handler(func: Callable) -> Callable:
    """
    Decorator para capturar exceções em rotas e formatar a resposta de erro.
    Ele lida com erros HTTP específicos e erros genéricos do servidor.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Dict[str, Any]:
        print('NÃO FUNCIONA?')
        try:
            # Tenta executar a função da rota original
            return func(*args, **kwargs)
        except Exception as error:
            # Se qualquer exceção for lançada, ela é capturada aqui
            if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
                # Se for um erro HTTP conhecido (422 ou 400), formata a resposta
                return {
                    'status_code': error.status_code,
                    'body': {
                        'errors': [{
                            'title': error.name,
                            'detail': error.message
                        }]
                    }
                }

            # Para qualquer outra exceção, retorna um erro de servidor genérico (500)
            return {
                'status_code': 500,
                'body': {
                    'errors': [{
                        'title': 'Server Error',
                        'detail': str(error)
                    }]
                }
            }

    return wrapper