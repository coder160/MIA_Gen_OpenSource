from src.pages.layout import App_Layout
from src.pages.login import Login

class App(App_Layout):
    def __init__(self):
        super()
        self._main_view()
        self.run_app(show_navigation=True)
    def _main_view(self):
        self._route_index = 0
        self.set_body(Login(callback=self.home_view,
                            api = self.get_api(),
                            server = self.get_server()).get_body())

if __name__ == '__main__':
    App()