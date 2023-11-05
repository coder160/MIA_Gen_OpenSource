from src.libs import base_builder

class Row:
    def __init__(self, content:list, align_horizontal=base_builder.MainAxisAlignment.CENTER, align_vertical=base_builder.CrossAxisAlignment.END):
        self._alignment = align_horizontal
        self._vertical_alignment = align_vertical
        self._content = content
    def compose(self, ):
        return base_builder.Row(self._content,
                                alignment=self._alignment,
                                vertical_alignment=self._vertical_alignment)
        