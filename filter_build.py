from abc import ABC


class BaseBuilder(ABC):
    def edit_photo(self, *args):
        ...


class Builder(BaseBuilder):
    def edit_photo(self, *args):
        for editor in args:
            eval(f"{editor}.render()")
