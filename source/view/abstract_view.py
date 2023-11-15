from abc import ABC, abstractmethod
from source.view.session import Session

class AbstractView(ABC):
    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def make_choice(self):
        pass