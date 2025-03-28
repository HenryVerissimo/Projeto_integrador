import flet as ft
from flet import ControlEvent, Page
from controllers import C


def main(page: Page):
    
    ### CONFIGURAÇÕES DE PÁGINA ###
    page.title = "App ADM - GameOver"
    page.bgcolor = "#160321"
    page.window.width = 1000
    page.window.height = 700
    page.window.min_width = 200
    page.window.min_height = 200
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {
        "LilitaOne-Regular": "/fonts/LilitaOne-Regular.ttf"
    }


    ### FUNÇÕES DE CONTROLE DE PÁGINAS ###
    def login_user_click(e: ControlEvent):

        #fazer query
        page.controls.clear()
        page.add(home_view)
        page.update()

    def create_user_click(e: ControlEvent):
        new_user = CreateUserController().create_user(create_name, create_email, create_password, confirm_password)

        if new_user["status"] == "error":
            create_error_text.value = new_user["message"]
            page.update()
            return None
        
        page.controls.clear()
        page.controls.add(home_view)
        page.update()
        
        
    def go_to_create_click(e: ControlEvent):
        
        page.controls.clear()
        page.add(create_account_view)
        page.update()

    def go_to_login_click(e: ControlEvent):

        page.controls.clear()
        page.add(login_view)
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
                                width=200,
                                height=200
                            )
                        ),
                        ft.Container(
                            padding=ft.padding.only(left= 10, right=10, top=0, bottom=30),
                            content=ft.Text(
                                value="LOGIN DE USUÁRIO",
                                size=30,
                                text_align=ft.TextAlign.CENTER,
                                style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300),
                            )
                        ),
                        ft.Container(
                            bgcolor="",
                            padding=ft.padding.only(left=50, right=50, top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    user_email := ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200,),
                                    user_password := ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
                                    ft.Button(text="ENTRAR NA CONTA", width=300, on_click=login_user_click, color=ft.Colors.PURPLE_900, bgcolor=ft.Colors.PURPLE_200),
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.TextButton(text="Criar uma nova conta", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_create_click)
                                ]
                            )
                        )                        
                    ]
                )               
            ]
        )   
    )

    create_account_view = ft.Container(
        height=page.window.height,

        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src="images/user.png",
                                width=150,
                                height=150
                            )
                        ),
                        ft.Container(
                            padding=ft.padding.only(left= 10, right=10, top=0, bottom=30),
                            content=ft.Text(
                                value="CRIAR UMA CONTA",
                                size=30,
                                text_align=ft.TextAlign.CENTER,
                                style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300),
                            )
                        ),
                        ft.Container(
                            bgcolor="",
                            padding=ft.padding.only(left=50, right=50, top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    create_name := ft.TextField(label="Nome", width=300, border_color=ft.Colors.PURPLE_200,),
                                    create_email := ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200,),
                                    create_password := ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
                                    confirm_password  := ft.TextField(label="Confirmar senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
                                    ft.Button(text="CRIAR UMA CONTA", width=300, on_click=login_user_click, color=ft.Colors.PURPLE_900, bgcolor=ft.Colors.PURPLE_200),
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.TextButton(text="Voltar para o login", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_login_click),
                                    create_error_text := ft.Text(value="", visible=False)
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
    page.add(create_account_view)
    page.update()  


if __name__ == "__main__":

    app = ft.app(target=main, assets_dir="assets")
