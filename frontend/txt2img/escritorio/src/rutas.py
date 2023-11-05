from src.pages.about import About
from src.pages.files import Files
from src.pages.generative import Generative
from src.pages.inicio import Home
from src.pages.login import Login
from src.pages.settings import Settings


class Rutas:
    def __init__(self):
        self.__route_list = {"Inicio": Home,
                             "App": Generative,
                             "Files": Files,
                             "Settings": Settings,
                             "About": Login,
                             "Error":Login}

    def get_dict(self) -> dict:
        return self.__route_list

    def get_list(self) -> list:
        _list = []
        for _k, _v in self.get_dict().items():
            _list.append(_v)
        return _list

    def path_to_index(self, path) -> int:
        _indexes = {}
        for _i, _k in enumerate(self.get_dict().keys()):
            _indexes[_k] = _i
        return _indexes[path]

    def get_route(self, path):
        return self.get_dict().get(path, "Error")
