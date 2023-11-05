from src.components.login_card import Login_card
from src.components.elements.inputs import Text_Input
from src.components.elements.row import Row
from src.components.elements.column import Column
from src.components.elements.butons import Filled_Button

from src.api.client_api import Client_Api
from src.api.models import New_Server


class Login:
    def __init__(self, callback=None, api=Client_Api, server=New_Server):
        self.__main_content = []
        self.fn_callback = callback
        self.__new_api = api
        self.__new_server = server

    def set_content(self, content_row: list):
        _row = Row(content_row)
        _column = Column([_row.compose()])
        self.__main_content = _column.compose()

    def get_content(self) -> Column:
        return self.__main_content

    def get_card(self) -> Login_card:
        _titulo = "Introduzca su Servidor (dirección dirección IP), Puerto y Contraseña."
        _subtitulo = "Encuentre toda la información en su Servidor Privado."
        self._input_server = Text_Input(label="Servidor:Puerto").compose()
        self._input_user = Text_Input(label="Usuario").compose()
        self._input_passwrd = Text_Input(label="Contraseña", is_secret=True, is_reveleable=True).compose()
        _submit_btn = Filled_Button("Iniciar Máquina Cliente", fn=self.submit_login).compose()
        __row_submit = Row([_submit_btn]).compose()
        _formulario = [self._input_server,
                       self._input_user,
                       self._input_passwrd,
                       __row_submit]
        return Login_card(_titulo, _subtitulo, _formulario).compose()

    def submit_login(self, e):
        _server = self.__new_server(self._input_server.value,self._input_user.value,self._input_passwrd.value)
        _api = self.__new_api(server=_server)
        self.__logged_in = _api.start_server()
        if self.__logged_in == True:
            self.fn_callback(None)
            _msg = "Conexión Exitosa con Servidor Backend"
        else:
            _msg = "Conexión Fallida con Servidor Backend"
        print(f"[{_msg}\t:\t{self.__logged_in}]")
            


    def get_body(self) -> Column:
        _main_content = [self.get_card()]
        self.set_content(_main_content)
        return self.get_content()
