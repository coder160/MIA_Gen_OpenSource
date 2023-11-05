from src.libs import base_builder

class Filled_Button:
    def __init__(self,  label:str, fn=None , is_disabled = bool(False)):
        self._is_disabled= is_disabled
        self._label = label
        self._fn = fn
        
    def compose(self):
        return base_builder.FilledButton(self._label, disabled=self._is_disabled, on_click = self._fn)