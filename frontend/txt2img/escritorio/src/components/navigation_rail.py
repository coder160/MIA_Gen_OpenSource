from src.libs import base_builder


class Navigation_Rail:
    def __init__(self):
        self.__title = "NavBar_Top AI en Corto"

    def get_title(self):
        return self.__title

    def compose(self, fn_navigation, index):
        return base_builder.NavigationRail(selected_index=index,
                                           label_type=base_builder.NavigationRailLabelType.ALL,
                                           min_width=100,
                                           min_extended_width=400,
                                           leading=base_builder.FloatingActionButton(
                                               icon=base_builder.icons.CREATE, text="Add"),
                                           group_alignment=-0.9,
                                           destinations=[base_builder.NavigationRailDestination(icon=base_builder.icons.SPACE_DASHBOARD_OUTLINED,
                                                                                                selected_icon=base_builder.icons.SPACE_DASHBOARD_ROUNDED,
                                                                                                label="Inicio"),
                                                         base_builder.NavigationRailDestination(icon=base_builder.icons.FIBER_NEW_OUTLINED,
                                                                                                selected_icon=base_builder.icons.FIBER_NEW_ROUNDED,
                                                                                                label="App"),
                                                         base_builder.NavigationRailDestination(icon=base_builder.icons.FOLDER_OPEN,
                                                                                                selected_icon=base_builder.icons.FOLDER,
                                                                                                label="Files"),
                                                         base_builder.NavigationRailDestination(icon=base_builder.icons.SETTINGS_SUGGEST_OUTLINED,
                                                                                                selected_icon=base_builder.icons.SETTINGS_SUGGEST_ROUNDED,
                                                                                                label="Settings"),
                                                         base_builder.NavigationRailDestination(icon=base_builder.icons.PERM_DEVICE_INFORMATION_OUTLINED,
                                                                                                selected_icon=base_builder.icons.PERM_DEVICE_INFORMATION_ROUNDED,
                                                                                                label="About"),
                                                         ],
                                           on_change=fn_navigation)

    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        return self
