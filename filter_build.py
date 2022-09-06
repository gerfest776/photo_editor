from abc import ABC


class BaseBuilder(ABC):
    def __init__(self, image: str):
        self.image = image

    def edit_photo(self, *args):
        ...


class Builder(BaseBuilder):
    def edit_photo(self, *args):
        for editor in args:
            eval(f"{editor}.render({self.image})")
