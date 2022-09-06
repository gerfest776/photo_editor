from abc import ABC

from PIL import Image, ImageColor, ImageDraw, ImageFont

from editors.base_editor import BaseEditor


class BaseWaterMark(BaseEditor, ABC):
    def __init__(self, pos: tuple):
        self.pos = pos


class ImageWaterMark(BaseWaterMark):
    def __init__(self, pos: tuple, water_mark_path: str):
        super().__init__(pos)
        self.water_mark_path: str = water_mark_path

    def render(self, image: str) -> None:
        base_image = Image.open(image)
        base_image.paste(Image.open(self.water_mark_path), self.pos)
        base_image.show()
        base_image.save(image)


class TextWaterMark(BaseWaterMark):
    def __init__(self, pos: tuple, text: str, color: str, font: ImageFont):
        super().__init__(pos)
        self.text: str = text
        self.color: tuple = ImageColor.getrgb(color)
        self.font = font

    def render(self, image: str) -> None:
        photo = Image.open(image)

        ImageDraw.Draw(photo).text(self.pos, self.text, fill=self.color, font=self.font)
        photo.show()
        photo.save(image)
