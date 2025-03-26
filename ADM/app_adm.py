import flet as ft
from flet import ControlEvent, Page


def main(page: Page):
    
    ### CONFIGURAÇÕES DE PÁGINA ###
    page.title = "App ADM - GameOver"
    page.window.width = 1000
    page.window.height = 700
    page.window.min_width = 600
    page.window.min_height = 600
    page.scroll = ft.ScrollMode.AUTO
    page.fonts = {
        "LilitaOne-Regular": "/fonts/LilitaOne-Regular.ttf"
    }


    ### FUNÇÕES DE CONTROLE DE PÁGINAS ###
    def login_user_click(e: ControlEvent):

        query = textemail.value

        page.controls.clear()
        page.add(home_view)
        page.update()

    def Home_back_click(e: ControlEvent):

        page.controls.clear()
        page.add(login_view)
        page.update()


    ### FUNÇÕES DE TRATAMENTO DE DADOS ###


    ### PÁGINAS DO APLICATIVO ###
    login_view = ft.Container(
        height=page.window.height,

        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="images/logo_projeto.png",
                                width=250,
                                height=250
                            )
                        ),
                        ft.Container(
                            content=ft.Text(
                                value="LOGIN DE USUÁRIO",
                                size=30,
                                text_align=ft.TextAlign.CENTER,
                                style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)
                            )
                        ),
                        ft.Container(
                            bgcolor="",
                            padding=ft.padding.only(left=50, right=50, top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    textemail := ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200,),
                                    ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
                                    ft.Button(text="ENTRAR NA CONTA", width=300, on_click=login_user_click, color=ft.Colors.PURPLE_900, bgcolor=ft.Colors.PURPLE_200),
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.TextButton(text="Criar uma nova conta", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100))
                                ]
                            )
                        )                        
                    ]
                )               
            ]
        )   
    )

    home_view = ft.Container(
       content=ft.ResponsiveRow(
            controls=[
                ft.Text(value="Home", size=30, weight=ft.FontWeight.BOLD),
                ft.Button(text="Sair da conta", on_click=Home_back_click)
            ]
        )
    )
     
            

    ### CONFIGURA A PÁGINA INICIAL PADRÃO ###
    page.add(login_view)
    page.update()  

if __name__ == "__main__":

    app = ft.app(target=main, assets_dir="assets")
