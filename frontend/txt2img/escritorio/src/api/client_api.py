from src.api.handler import API
from src.api.models import New_Server
class Client_Api:
    def __init__(self, server:New_Server):
        self.__api = API(server=server)
        self.__server = server
        self.__private_server_token = None

    def get_server_token(self):
        return self.__private_server_token if self.__private_server_token != None else "Invalid_Token"

    def start_server(self) -> bool:
        _data = {"username": self.__server.get_username(), "password": self.__server.get_password()}
        _started = False
        try:
            _raw = self.__api._call_cpu(method="/start_server",input=_data)
            if _raw.ok:
                _response_json = _raw.json()
                _started = True
                self.__private_server_token = _response_json.get('server_token')
            else:
                raise Exception(_raw.reason)
        except Exception as error:
            print(error)
            _started = False
        finally:
            return _started

                
            
