from abc import ABC, abstractmethod

from PIL import Image, ImageFilter

from editors.base_editor import BaseEditor


class BaseFilter(BaseEditor, ABC):
    @abstractmethod
    def _filter(self, image: Image):
        ...


class BlurFilter(BaseFilter):
    def _filter(self, image: Image) -> None:
        image.filter(ImageFilter.BLUR)

    def render(self, image: str):
        base_image = Image.open(image)
        self._filter(base_image)
        base_image.save(image)
