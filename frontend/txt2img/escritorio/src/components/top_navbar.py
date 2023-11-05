from src.libs import base_builder

class Top_NavBar:
    def __init__(self):
        self.__title = "NavBar_Top AI en Corto"
        
    def get_title(self):
        return self.__title
        
    def compose(self, fn_nav_home, fn_nav_app, fn_nav_files, fn_nav_settings):
        return base_builder.AppBar(leading=base_builder.Icon(base_builder.icons.PALETTE),
                                            leading_width=40,
                                            title=base_builder.Text(self.get_title()),
                                            center_title=False,
                                            bgcolor=base_builder.colors.SURFACE_VARIANT,
                                            actions=[base_builder.IconButton(base_builder.icons.SPACE_DASHBOARD_OUTLINED, 
                                                                             on_click=fn_nav_home),
                                                     base_builder.IconButton(base_builder.icons.FILTER_3, 
                                                                             on_click=fn_nav_app),
                                                     base_builder.PopupMenuButton(items=[base_builder.PopupMenuItem(text="Item 1"),
                                                                                         base_builder.PopupMenuItem(),  # divider
                                                                                         base_builder.PopupMenuItem(text="Checked item", 
                                                                                                                    checked=False, 
                                                                                                                    on_click=self.check_item_clicked)])])
        
    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        return self
        