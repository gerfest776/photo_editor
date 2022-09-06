from editors.base_editor import BaseEditor
from PIL import Image


class SimpleResizer(BaseEditor):
    def __init__(self, size: tuple):
        self.size = size

    def render(self, image: str) -> None:
        base_image = Image.open(image)
        base_image.resize(self.size)
        base_image.save(image)
