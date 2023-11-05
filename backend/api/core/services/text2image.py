
class Generator:
    def __init__(self, model:str, token:str):
        self.__model = model
        self.__token = token
    
    def start_server(self, username: str):
        server_token = str()
        return server_token
    
    def get_model(self):
        return self.__model
    
    def get_token(self):
        return self.__token