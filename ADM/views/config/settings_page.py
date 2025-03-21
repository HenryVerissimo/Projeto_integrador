from flet import Page
from abc import ABC, abstractmethod

class IConfigPage(ABC):

    @abstractmethod
    def _window(self, page: Page):
        pass
    
    @abstractmethod
    def _informations(self, page: Page):
        pass


class DefaultConfig(IConfigPage):
 
    def _window(self, page: Page) -> None:
        page.window.min_width = 600    
        page.window.min_height = 700
        page.window.width = 1000
        page.window.height = 700
        page.bgcolor = "#170e1f"
    
    def _informations(self, page: Page) -> None:
        page.title="GameOver Admin"


class AddConfigPage:
    def __init__(self, page: Page, config: IConfigPage) -> None:
        self.config = config
        self.page = page

    def settings(self) -> None:
        self.config._window(self.page)
        self.config._informations(self.page)
