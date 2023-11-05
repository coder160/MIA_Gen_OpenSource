from src.libs import base_builder

class Column:
    def __init__(self, content:list):
        self._content = content

    def compose(self, ):
        return base_builder.Column(self._content,
                                   alignment=base_builder.MainAxisAlignment.CENTER)
    
        