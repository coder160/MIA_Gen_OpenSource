import json


class Server_Manager:
    @staticmethod
    def get_config_file() -> str:
        return 'api/core/services/server_config.json'

    @staticmethod
    def generate_token(new_string: str) -> str:
        return new_string

    @staticmethod
    def get_private_config() -> dict:
        PRIVATE_SERVER_DATA = {}
        with open(Server_Manager.get_config_file(), 'r') as json_file:
            PRIVATE_SERVER_DATA = json.load(json_file)
        return PRIVATE_SERVER_DATA

    @staticmethod
    def get_public_config() -> dict:
        PUBLIC_SERVER_DATA = {"SERVER_IP": Server_Manager.get_server_ip(),
                              "SERVER_PORT": Server_Manager.get_server_port(),
                              "SERVER_STARTED": Server_Manager.get_server_status(),
                              "ACTIVE_USER": Server_Manager.get_server_active_user()}
        return PUBLIC_SERVER_DATA

    @staticmethod
    def set_private_config(key, value):
        data = Server_Manager.get_private_config()
        data[key] = value
        with open(Server_Manager.get_config_file(), 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def set_server_active_token(active_token: str) -> str:
        Server_Manager.set_private_config("ACTIVE_TOKEN", active_token)

    @staticmethod
    def set_server_active_user(active_username: str) -> str:
        Server_Manager.set_private_config("ACTIVE_USER", active_username)

    @staticmethod
    def set_server_running(status: bool) -> str:
        Server_Manager.set_private_config("SERVER_STARTED", status)

    @staticmethod
    def validate_server_password(password:str) -> bool:
        return True if Server_Manager.get_private_config().get('SERVER_PASSWORD') == password else False
    
    @staticmethod
    def validate_server_token(server_token:str) -> bool:
        return True if Server_Manager.get_private_config().get('ACTIVE_TOKEN') == server_token else False

    @staticmethod
    def get_server_ip() -> str:
        return Server_Manager.get_private_config().get('SERVER_IP')

    @staticmethod
    def get_server_port() -> str:
        return Server_Manager.get_private_config().get('SERVER_PORT')

    @staticmethod
    def get_server_status() -> bool:
        return Server_Manager.get_private_config().get('SERVER_STARTED')

    @staticmethod
    def get_server_active_user() -> str:
        return Server_Manager.get_private_config().get('ACTIVE_USER')