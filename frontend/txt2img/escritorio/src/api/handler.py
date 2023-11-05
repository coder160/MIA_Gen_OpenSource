from src.api.models import New_Server
import requests
import json


class API:
    def __init__(self, server: New_Server):
        self.__base_url = "http://{server_address}".format(
            server_address=server.get_full_address())
        self.__server_token = server.get_password()
        self.__headers_cpu = {'accept': 'application/json',
                              'Content-Type': 'application/json'}
        self.__headers_gpu = {"Authorization": f"Bearer {self.__server_token}",
                              "accept": "image/png",
                              "Content-Type": "application/json"}

    def _call_cpu(self, input: dict, method: str) -> requests.Response:
        return requests.post(json=input,
                             headers=self.__headers_cpu,
                             url=self.__base_url + method)

    def _call_gpu(self, input, method: str) -> requests.Response:
        return requests.post(data=json.dumps(input),
                             headers=self.__headers_gpu,
                             url=self.__base_url + method)
