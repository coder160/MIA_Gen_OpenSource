
class New_Server:
    def __init__(self, server_address:str, username:str, password:str):
        self.__full_address = server_address
        self.__password = password
        self.__username = username
    
    def get_full_address(self) -> str:
        return self.__full_address
    
    def get_ip(self) -> str:
        try:
            _ip = self.get_full_address().split(':')[0]
        except:
            _ip = "localhost"
        finally:
            return _ip
    
    def get_port(self) -> str:
        try:
            _port = self.get_full_address().split(':')[1]
        except:
            _port = "8080"
        finally:
            return _port
        
    
    def get_password(self) -> str:
        return self.__password
    
    def get_username(self) -> str:
        return self.__username
    
    