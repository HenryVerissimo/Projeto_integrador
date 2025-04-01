import flet as ft
from flet import ControlEvent, Page

from src.ADM.controllers import CreateUserController, LoginAccountController, SelectController


def main(page: Page):
    
    ### CONFIGURAÇÕES DE PÁGINA ###

    page.title = "App ADM - GameOver"
    page.bgcolor = "#160f1c"
    page.window.width = 1280
    page.window.height = 720
    page.window.min_width = 880
    page.window.min_height = 700
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK
    page.fonts = {
        "LilitaOne-Regular": "src/ADM/assets/fonts/LilitaOne-Regular.ttf"
    }



    ### FUNÇÕES DE TROCA DE PÁGINAS ###

    def go_to_create_click(e: ControlEvent):
        
        page.controls.clear()
        create_account_widgets["text_error"].visible = False
        create_account_widgets["create_name"].value = ""
        create_account_widgets["create_email"].value = ""
        create_account_widgets["create_password"].value = ""
        create_account_widgets["confirm_password"].value = ""
        page.add(create_account_view)
        page.update()

    def go_to_login_click(e: ControlEvent):

        page.controls.clear()
        login_widgets["text_error"].visible = False
        login_widgets["user_email"].value = ""
        login_widgets["user_password"].value = ""
        page.add(login_view)
        page.update()

    def go_to_select_click(e: ControlEvent):

        page.controls.clear()
        select_widgets["text_error"].value = ""
        select_widgets["text_error"].visible = False
        select_results.content = select_widgets["text_no_results"]
        page.add(select_view)
        page.update()



    ### FUNÇÕES DE CHECAGEM DE DADOS ###

    def login_user_click(e: ControlEvent):
        login = LoginAccountController().login_account(login_widgets["user_email"].value, login_widgets["user_password"].value)

        if login["status"] == "error":
            login_widgets["text_error"].value = login["message"]
            login_widgets["text_error"].visible = True
            page.update()
            return None
        
        page.controls.clear()
        select_widgets["text_error"].value = ""
        select_widgets["text_error"].visible = False
        select_results.content = select_widgets["text_no_results"]
        page.add(select_view)
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
        select_widgets["text_error"].value = ""
        select_widgets["text_error"].visible = False
        select_results.content = select_widgets["text_no_results"]
        page.add(select_view)
        page.update()
        


    ### FUNÇÕES DE SELEÇÃO DE DADOS ###

    def select_results_click(e: ControlEvent):

        response = []
        columns = []
        rows = []

        table = select_widgets["select_table"].value


        if table == "Usuários":
            request = SelectController().select_all_users()
        
        if table == "Jogos":
            request = SelectController().select_all_games()

        if table == "Aluguéis":
            request = SelectController().select_all_games_rental()


        if request["status"] == "error":
            select_results.clean()
            select_results.content = ft.Text(value=str(request["message"]), text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular",color="#441b70", size=20))
            select_results.update()
            page.update()
            return None

        for registro in request["response"]:
            response.append(registro)
        
        while not columns:
            
            for column in response[0].keys():
                columns.append(ft.DataColumn(ft.Text(column, style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD))))

        for record in response:
            
            values = []
            for value in record.values():
                values.append(ft.DataCell(ft.Text(value, style=ft.TextStyle(color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD))))

            rows.append(ft.DataRow(cells=values))

        table = ft.DataTable(
            columns=columns,
            rows=rows                
        )

        select_results.content = table
        select_results.update()
            
        page.update()

    
    def select_columns_click(e: ControlEvent):

        if select_widgets["select_table"].value == "Usuários":
            options_columns = ["ID", "Nome", "Email", "Admin", "Status", "Todas"]
        
        elif select_widgets["select_table"].value == "Jogos":
            options_columns = ["ID", "Nome", "Preço", "Quantidade", "Genero", "Todas"]

        elif select_widgets["select_table"].value == "Aluguéis":
            options_columns = ["ID", "Usuário", "Jogo", "Data de aluguel", "Data de devolução", "Status", "Todas"]

        options_filter = []
        for option in options_columns:
            options_filter.append(ft.DropdownOption(key=option, content=ft.Text(value=option, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)))

        select_widgets["select_filter"].options = options_filter
        select_view.update()
        page.update()


    ### WIDGETS DO APLICATIVO ###

    login_widgets = {
        "logo_project": ft.Image(src="src/ADM/assets/images/logo_projeto.png", width=200, height=200),
        "text_login": ft.Text(value="LOGIN DE USUÁRIO", size=30, text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)),
        "user_email": ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200),
        "user_password": ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "button_login": ft.Button(text="ENTRAR NA CONTA", width=300, on_click=login_user_click, color="#180030", bgcolor=ft.Colors.PURPLE_200),
        "button_create_account": ft.TextButton(text="Criar uma nova conta", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_create_click),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER)
    }

    create_account_widgets = {
        "user_icon": ft.Image(src="images/user.png", width=150, height=150),
        "text_create_account": ft.Text( value="CRIAR UMA CONTA", size=30, text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)),
        "create_name": ft.TextField(label="Nome", width=300, border_color=ft.Colors.PURPLE_200,),
        "create_email": ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200,),
        "create_password": ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "confirm_password": ft.TextField(label="Confirmar senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "button_create_account": ft.Button(text="CRIAR UMA CONTA", width=300, on_click=create_user_click, color="#180030", bgcolor=ft.Colors.PURPLE_200),
        "button_back": ft.TextButton(text="Voltar para o login", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_login_click),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER)

    }

    home_bar_widgets = {
        "logo_project": ft.Image(src="src/ADM/assets/images/logo_projeto.png", width=50, height=50, col=6),
        "text_logout": ft.TextButton(icon=ft.Icons.EXIT_TO_APP, text="SAIR DA CONTA", col=3, style=ft.ButtonStyle(color=ft.Colors.WHITE), icon_color=ft.Colors.WHITE, on_click=go_to_login_click),
        "select_operations": ft.Dropdown(
            options=[
                ft.DropdownOption(key="INSERT", content= ft.Text("INSERT", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "SELECT", content= ft.Text("SELECT", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "UPDATE", content= ft.Text("UPDATE", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "DELETE", content= ft.Text("DELETE", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD))
            ],
            col=3,
            value="SELECT",
            border_color=ft.Colors.WHITE,
            border_width=3,
            bgcolor=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            
        ),    
    }

    select_widgets = {
    "title_database": ft.Text(value="REGISTROS NO BANCO DE DADOS", col=10, style=ft.TextStyle(font_family="LilitaOne-Regular",color=ft.Colors.BLACK, size=20)),
        "button_reload": ft.IconButton(icon=ft.Icons.REFRESH, col=2, on_click=select_results_click, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#601e9e")),
        "text_no_results": ft.Text(value="Sem resultados por enquanto", text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular",color="#441b70", size=20)),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER),
        "input_filter": ft.TextField(label="Digite o filtro", border_color=ft.Colors.PURPLE_200, border_width=1, width=150),
        "select_table": ft.Dropdown(
            options=[
                ft.DropdownOption(key="Jogos", content=ft.Text("Jogos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key="Usuários", content=ft.Text("Usuários", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key="Aluguéis", content=ft.Text("Alugueis", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            width=150,
            value="Usuários",
            border_color=ft.Colors.PURPLE_200,
            border_width=1,
            on_change=select_columns_click          
        ),
        "select_filter": ft.Dropdown(
            options=[
                ft.DropdownOption(key="ID", content=ft.Text("ID", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Nome", content=ft.Text("Nome", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Email", content=ft.Text("Email", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Admin", content=ft.Text("Admin", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Status", content=ft.Text("Status", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Todas", content=ft.Text("Todas", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ], 
            value="Todas", 
            border_color=ft.Colors.PURPLE_200, 
            border_width=1, 
            width=150 
        )
        
    }



    ### WIDGETS DINÂMICOS ###

        
    select_results = ft.Container(
        content=select_widgets["text_no_results"],
    )



    ### PÁGINAS DO APLICATIVO ###

    home_bar = ft.Container(
        margin= 0,
        padding=10,
        bgcolor="#6100b5",
        
        content=ft.ResponsiveRow(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                home_bar_widgets["text_logout"],
                home_bar_widgets["logo_project"],
                home_bar_widgets["select_operations"]
            ]
        )
    )


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
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[ 
                                    login_widgets["button_create_account"],
                                    login_widgets["text_error"]
                                    
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

    select_view = ft.Container(
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=home_bar
                ),
                ft.Container(
                    margin=ft.margin.only(top=40, left=40),
                    padding=ft.padding.all(30),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        select_widgets["select_table"],
                                        select_widgets["select_filter"],
                                        select_widgets["input_filter"]
                                    ]
                                )

                            )    
                        ]
                    )
                ),

                ft.Container(
                    width=700,
                    expand=True,
                    bgcolor="#9c57f7",
                    margin=ft.margin.all(40),
                    border_radius=10,
                    padding=0,
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                bgcolor="#8944e3",
                                padding=ft.padding.all(10),
                                content=ft.ResponsiveRow(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        select_widgets["title_database"],
                                        select_widgets["button_reload"]
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.all(30),
                                content=ft.Column(
                                    controls=[
                                        select_results
                                    ]
                                )
                            ),
                            create_account_widgets["text_error"],

                        ]
                    )
                )      
            ]
        )
    )
    

            
    ### CONFIGURA A PÁGINA INICIAL PADRÃO ###

    page.add(login_view)
    page.update()  

if __name__ == "__main__":

    app = ft.app(target=main, assets_dir="src/ADM/assets")
    
