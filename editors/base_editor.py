from abc import ABC, abstractmethod


class BaseEditor(ABC):
    @abstractmethod
    def render(self, image: str):
        ...
