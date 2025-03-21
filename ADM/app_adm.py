import flet as ft

from views.config import AddConfigPage, DefaultConfig
from views.login_view import LoginUserView


def main(page: ft.Page):

    config = DefaultConfig()
    AddConfigPage(page, config).settings()

    page.controls.append(LoginUserView(page).build())

    page.update()
    
if __name__ == "__main__":

    ft.app(target=main)
