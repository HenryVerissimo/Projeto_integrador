import flet as ft

from .config.interface_view import InterfaceView

class LoginUserView(InterfaceView):

    def __init__(self, page: ft.Page) -> None:
        self.logo_projeto = ft.Image(src=r"ADM/views/assets/logo_projeto.png", width=200, height=200)
        self.texto_login = ft.Text(value="Login de usuário", size=20, font_family= "Nimbus Mono PS", text_align=ft.TextAlign.CENTER, color=ft.colors.WHITE)
        self.entrada_nome = ft.TextField(hint_text="Insira o nome de usuário", width=300, text_align=ft.TextAlign.CENTER, border_color="#a06be3")
        self.entrada_senha = ft.TextField(hint_text="Insira sua senha",password=True, width=300, text_align=ft.TextAlign.CENTER, border_color="#a06be3")
        self.botao_entrar = ft.Button(text="Entrar", width=150, color="#101413", bgcolor="#a06be3")
        self.botao_esqueceu_senha = ft.TextButton(text="Esqueci minha senha", style=ft.ButtonStyle("#a06be3"))
        self.botao_criar_conta = ft.TextButton(text="Criar uma conta nova", style=ft.ButtonStyle("#a06be3"))


    def build(self) -> ft.Row:
        return ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        ft.Container(
                            ft.Column(
                                controls=[
                                    self.logo_projeto,
                                    self.texto_login   
                                ],
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER
                            )
                        ),
                        
                        ft.Container(
                            ft.Column(
                                expand=True,
                                spacing=15,
                                controls=[
                                    self.entrada_nome,
                                    self.entrada_senha
                                ]
                            ),                 
                        ),

                        ft.Container(
                            ft.Row(
                                spacing=10,
                                controls=[
                                    self.botao_entrar,
                                    self.botao_esqueceu_senha    
                                ]
                            )           
                        ),

                        ft.Container(
                            ft.Row(
                                controls=[
                                    self.botao_criar_conta 
                                ]
                            ),
                            height=200               
                        )
                    ]
                )
            ],        
        )