from src.components.login_card import Login_card
from src.components.elements.inputs import Text_Input
from src.components.elements.row import Row
from src.components.elements.column import Column
from src.components.elements.butons import Filled_Button

from src.libs import base_builder

class Files:
    def __init__(self):
        pass
    def get_body(self):
        img = base_builder.Image(
            src=f"/icons/icon-512.png",
            width=100,
            height=100,
            fit=base_builder.ImageFit.CONTAIN)
        images = base_builder.Row(expand=1, wrap=False, scroll="always")
        return base_builder.Text("Files!")