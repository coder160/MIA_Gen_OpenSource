from src.libs import base_builder
from src.rutas import Rutas
from src.components.top_navbar import Top_NavBar
from src.components.bot_navbar import Bot_NavBar
from src.components.navigation_rail import Navigation_Rail

from src.api.client_api import Client_Api
from src.api.models import New_Server

class App_Layout(base_builder.Page):
    def __init__(self):
        super()

    def get_api(self):
        return Client_Api
    
    def get_server(self):
        return New_Server
    
    def home_view(self, btn):
        self.navigate_top("Inicio")

    def app_view(self, btn):
        self.navigate_top("App")

    def files_view(self, btn):
        self.navigate_top("Files")

    def settings_view(self, btn):
        self.navigate_top("Settings")

    def navigate_top(self, route_lbl):
        self._route_index = Rutas().path_to_index(route_lbl)
        self.show_navigation = True if self._route_index == 0 else False
        self.refresh_view()
        
    def navigate_bottom(self, nav_btn):
        self._route_index = nav_btn.control.selected_index
        self.show_navigation = True if self._route_index == 0 else False
        self.refresh_view()
    
    def navigate_rail(self, nav_btn):
        self._route_index = nav_btn.control.selected_index
        self.show_navigation = True
        self.refresh_view()
        
    def refresh_view(self):
        active_view = Rutas().get_list()[self._route_index]
        self.get_page().controls.pop()
        self.set_body(active_view().get_body())
        self.build(self.get_page())

    def set_top_navbar(self):
        self.get_page().appbar = Top_NavBar().compose(fn_nav_home=self.home_view,
                                                      fn_nav_app=self.app_view,
                                                      fn_nav_files=self.files_view,
                                                      fn_nav_settings=self.settings_view)

    def set_bot_navbar(self):
        self.get_page().navigation_bar = Bot_NavBar().compose(fn_navigation=self.navigate_bottom,
                                                              index = self._route_index)

    def set_navigation(self):
        if self.show_navigation == True:
            self.get_page().add(base_builder.Row([Navigation_Rail().compose(fn_navigation=self.navigate_rail,
                                                                            index = self._route_index),
                                                  base_builder.VerticalDivider(
                                                      width=1),
                                                  base_builder.Column([self.get_body()],
                                                                      alignment=base_builder.MainAxisAlignment.START,
                                                                      expand=True)], expand=True))
        else:
            self.get_page().add(base_builder.Row([base_builder.Column([self.get_body()],
                                                                      alignment=base_builder.MainAxisAlignment.START,
                                                                      expand=True)], expand=True))

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def get_page(self):
        return self.__page

    def build(self, page):
        self.__page = page
        self.set_top_navbar()
        self.set_bot_navbar()
        self.set_navigation()
        self.get_page().update()

    def run_app(self, show_navigation=True):
        self.show_navigation = show_navigation
        base_builder.app(target=self.build)
