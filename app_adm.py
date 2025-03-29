import flet as ft
from flet import ControlEvent, Page

from src.ADM.controllers import CreateUserController


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
        new_user = CreateUserController().create_user(create_account_widgets["create_name"].value, create_account_widgets["create_email"].value,
                                                       create_account_widgets["create_password"].value, create_account_widgets["confirm_password"].value)

        if new_user["status"] == "error":
            create_account_widgets["text_error"].value = new_user["message"]
            create_account_widgets["text_error"].visible = True
            page.update()
            return None
        
        page.controls.clear()
        page.add(home_view)
        page.update()
        
        
    def go_to_create_click(e: ControlEvent):
        
        page.controls.clear()
        create_account_widgets["text_error"].visible = False
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



    ### WIDGETS DO APLICATIVO ###

    login_widgets = {
        "logo_project": ft.Image(src="images/logo_projeto.png", width=200, height=200),
        "text_login": ft.Text(value="LOGIN DE USUÁRIO", size=30, text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)),
        "user_email": ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200),
        "user_password": ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "button_login": ft.Button(text="ENTRAR NA CONTA", width=300, on_click=login_user_click, color=ft.Colors.PURPLE_900, bgcolor=ft.Colors.PURPLE_200),
        "button_create_account": ft.TextButton(text="Criar uma nova conta", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_create_click)
    }
    create_account_widgets = {
        "user_icon": ft.Image(src="images/user.png", width=150, height=150),
        "text_create_account": ft.Text( value="CRIAR UMA CONTA", size=30, text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)),
        "create_name": ft.TextField(label="Nome", width=300, border_color=ft.Colors.PURPLE_200,),
        "create_email": ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200,),
        "create_password": ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "confirm_password": ft.TextField(label="Confirmar senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "button_create_account": ft.Button(text="CRIAR UMA CONTA", width=300, on_click=create_user_click, color=ft.Colors.PURPLE_900, bgcolor=ft.Colors.PURPLE_200),
        "button_back": ft.TextButton(text="Voltar para o login", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_login_click),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER)

    }


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
                            content=login_widgets["logo_project"]
                        ),
                        ft.Container(
                            padding=ft.padding.only(left= 10, right=10, top=0, bottom=30),
                            content=login_widgets["text_login"]
                        ),
                        ft.Container(
                            padding=ft.padding.only(left=50, right=50, top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    login_widgets["user_email"],
                                    login_widgets["user_password"],
                                    login_widgets["button_login"]
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[ login_widgets["button_create_account"]
                                    
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
                            content= create_account_widgets["user_icon"]
                        ),
                        ft.Container(
                            padding=ft.padding.only(left= 10, right=10, top=0, bottom=30),
                            content=create_account_widgets["text_create_account"]
                        ),
                        ft.Container(
                            padding=ft.padding.only(left=50, right=50, top=10, bottom=10),
                            content=ft.Column(
                                controls=[
                                    create_account_widgets["create_name"],
                                    create_account_widgets["create_email"],
                                    create_account_widgets["create_password"],
                                    create_account_widgets["confirm_password"],
                                    create_account_widgets["button_create_account"],                    
                                    
                                ]
                            )
                        ),
                        ft.Container(
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    create_account_widgets["button_back"],
                                    create_account_widgets["text_error"]
                                    
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

    app = ft.app(target=main, assets_dir="src/ADM/assets")
