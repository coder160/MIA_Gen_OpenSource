from src.libs import base_builder


class Bot_NavBar:
    def __init__(self):
        self.__title = "NavBar_Bop AI en Corto"

    def get_title(self):
        return self.__title

    def compose(self, fn_navigation, index):
        return base_builder.NavigationBar(
            selected_index=index,
            on_change=fn_navigation,
            destinations=[base_builder.NavigationDestination(icon=base_builder.icons.SPACE_DASHBOARD_OUTLINED,
                                                             selected_icon=base_builder.icons.SPACE_DASHBOARD_ROUNDED,
                                                             label="Inicio"),
                          base_builder.NavigationDestination(icon=base_builder.icons.FIBER_NEW_OUTLINED,
                                                             selected_icon=base_builder.icons.FIBER_NEW_ROUNDED,
                                                             label="App"),
                          base_builder.NavigationDestination(icon=base_builder.icons.FOLDER_OPEN,
                                                             selected_icon=base_builder.icons.FOLDER,
                                                             label="Files"),
                          base_builder.NavigationDestination(icon=base_builder.icons.SETTINGS_SUGGEST_OUTLINED,
                                                             selected_icon=base_builder.icons.SETTINGS_SUGGEST_ROUNDED,
                                                             label="Settings"),
                          base_builder.NavigationDestination(icon=base_builder.icons.PERM_DEVICE_INFORMATION_OUTLINED,
                                                             selected_icon=base_builder.icons.PERM_DEVICE_INFORMATION_ROUNDED,
                                                             label="About")])
