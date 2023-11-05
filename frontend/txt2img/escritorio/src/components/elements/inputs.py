from src.libs import base_builder

class Text_Input:
    def __init__(self, label:str , is_secret=False, is_reveleable=False):
        self._is_secret = is_secret
        self._is_revelable = is_reveleable
        self._label = label
    def compose(self):
        return base_builder.TextField(label=self._label, 
                                      password=self._is_secret, 
                                      can_reveal_password=self._is_revelable)