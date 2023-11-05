from src.libs import base_builder

class Login_card:
    def __init__(self, titulo:str, subtitulo: str, formulario: list):
        self.__title = base_builder.Text(titulo)
        self.__subtitle = base_builder.Text(subtitulo)
        self._card_width = 680
        self._card_padding = 10
        self._formulario = formulario

    def get_title(self):
        return self.__title
    
    def get_subtitle(self):
        return self.__subtitle

    def compose(self):
        self.__content = [base_builder.ListTile(title=self.get_title(),subtitle=self.get_subtitle())]
        for _param in self._formulario:
            self.__content.append(_param)
            
        return base_builder.Card(
            content=base_builder.Container(
                content=base_builder.Column(self.__content),
                width=self._card_width,
                padding=self._card_padding))
