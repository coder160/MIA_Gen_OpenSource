from api.core.app import Middleware as Backend_Middleware_App

# CODIGOS DE ERROR
# 400           -           SOLICITUD MAL FORMADA 
# 401           -           SOLICITUD INCOMPLETA O MAL AUTENTICADA
# 403           -           SOLICITUD RECHAZADA POR PROCESO INTERNO
# 404           -           SOLICITUD MAL FORMADA


api = Backend_Middleware_App.base_fast_api()

@api.post("/start_server/", status_code=201)
def method_start_server(request_data:dict) -> dict:
    __response=dict({"request_data":request_data})
    
    if not request_data:
        __msg = "Request_Data - Mal Formado"
        raise Backend_Middleware_App.fast_api_exception(code = int(400), info=str(__msg))
    
    elif not 'username' in request_data:
        __msg = "Not Username - Not Found"
        raise Backend_Middleware_App.fast_api_exception(code = int(401), info=str(__msg))
    
    elif not 'password' in request_data:
        __msg = "Not Password - Not Found"
        raise Backend_Middleware_App.fast_api_exception(code = int(401), info=str(__msg))
    else:
        if Backend_Middleware_App.validate_password(password=request_data.get('password')):
            _new_token = Backend_Middleware_App.start_server(username=request_data.get('username'))
            if Backend_Middleware_App.validate_token(_new_token):
                __response['SERVER_RUNNING'] = Backend_Middleware_App.set_server_status(True)
                __response['SERVER_TOKEN'] = _new_token
                return __response
            else:
                Backend_Middleware_App.set_server_status(False)
                __msg = "Error Crítico - Imposible verificar su Token"
                raise Backend_Middleware_App.fast_api_exception(code = int(403), info=str(__msg))
        else:
            __msg = "Contraseña Incorrecta, verifique su contraseña en Servidor Backend"
            raise Backend_Middleware_App.fast_api_exception(code = int(403), info=str(__msg))
    