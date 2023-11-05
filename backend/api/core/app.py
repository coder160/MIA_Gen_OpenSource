from fastapi import FastAPI, HTTPException
from api.core.services.server_manager import Server_Manager
from api.core.services.text2image import Generator


class Middleware:
    @staticmethod
    def base_fast_api() -> FastAPI:
        return FastAPI()
    
    @staticmethod
    def fast_api_exception(code:int, info:str) -> HTTPException:
        return HTTPException(status_code=code, detail=info)
    
    @staticmethod
    def validate_token(server_token:str) -> bool:
        return Server_Manager.validate_server_token(server_token)
    
    @staticmethod
    def validate_password(password:str) -> bool:
        return Server_Manager.validate_server_password(password)
    
    @staticmethod
    def start_server(username:str)->str:
        """Inicia el servidor a partir de un nombre de Usuario.

        args:
            username                        (str)       :   Nombre de Usuario.
            password                        (str)       :   Contraseña del Servidor.
        return:
            server_token                    (str)       :   Nuevo Token Interno
        """
        server_token = Server_Manager.generate_token(username)
        Server_Manager.set_server_active_token(server_token)
        Server_Manager.set_server_active_user(username)
        return server_token
    
    @staticmethod
    def get_public_info()->dict:
        """Verifica la información interna del servidor backend y le entrega una copia al servidor frontend cliente.

        args:
            server_token                     (dict)      :   Datos del servidor Internos
        return:
            public_info                      (dict)      :   Datos del servidor, públicos
        """
        return Server_Manager.get_public_config()
    
    @staticmethod
    def set_server_status(running:bool)->bool:
        """Verifica el estatus actual del servidor.
        Permanecerá encendido una vez que inicie su aplicación cliente.
        En caso de encontrar un error grave, se dentendrá.

        args:
            server_token                     (dict)      :   Datos del servidor Internos.
        return:
            is_running                       (bool)      :   Estado del servidor.
        """
        Server_Manager.set_server_running(running)
        return Server_Manager.get_server_status()
    
    