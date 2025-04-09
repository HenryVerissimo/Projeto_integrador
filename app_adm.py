import flet as ft
from flet import ControlEvent, Page
from datetime import datetime
from src.ADM.controllers import CreateUserController, LoginAccountController, SelectController, InsertController, UpdateController


def main(page: Page):
    
    ### CONFIGURAÇÕES DE PÁGINA ###

    def page_config(page: Page):
        page.title = "App ADM - GameOver"
        page.bgcolor = "#160f1c"
        page.window.min_width = 940
        page.window.min_height = 700
        page.window.full_screen = False
        page.padding = 0
        page.scroll = ft.ScrollMode.AUTO
        page.theme_mode = ft.ThemeMode.DARK
        page.fonts = {
            "LilitaOne-Regular": "src/ADM/assets/fonts/LilitaOne-Regular.ttf"
        }

    def restart_window(page: Page) -> None:
        if page.width < 940 or page.height < 700:
            page.window.width = 940
            page.window.height = 700
            page.update()

    page_config(page)
    page.on_resized = lambda e: restart_window(page)

    

    ### ENTER AUTOMÁTICO PARA BOTÕES ###

    def key_press_click(e: ControlEvent):

        if page.controls[0] == login_view:
            if e.key == "Enter":
                login_user_click(e)

        elif page.controls[0] == create_account_view:
            if e.key == "Enter":
                create_user_click(e)

        elif page.controls[0] == select_view:
            if e.key == "Enter":
                select_results_click(e)

        elif page.controls[0] == insert_view:
            if e.key == "Enter":
                insert_database_click(e)

        elif page.controls[0] == update_view:
            if e.key == "Enter":
                update_database_click(e)

    page.on_keyboard_event = key_press_click



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

    def go_to_operations_click(e: ControlEvent):
        page.controls.clear()

        login_widgets["text_error"].visible = False
        create_account_widgets["text_error"].visible = False

        if home_bar_widgets["select_operations"].value == "CONSULTAR":
            page.add(select_view)

        if home_bar_widgets["select_operations"].value == "INSERIR":
            page.add(insert_view)

        if home_bar_widgets["select_operations"].value == "ATUALIZAR":
            page.add(update_view)

        if home_bar_widgets["select_operations"].value == "DELETAR":
            page.add(delete_view)

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
        create_account_widgets["text_error"].value = ""
        create_account_widgets["text_error"].visible = False
        select_results.content = select_widgets["text_no_results"]
        page.add(select_view)
        page.update()
        


    ### FUNÇÕES DE SELEÇÃO DE DADOS ###

    def select_results_click(e: ControlEvent):

        response = []
        columns = []
        rows = []

        table = select_widgets["select_table"].value
        column = select_widgets["select_filter"].value
        value = select_widgets["input_filter"].value
        bool_value = select_widgets["select_status_or_admin"].value


        if table == "Usuários":
            if select_widgets["select_filter"].value == "Todas":
                request = SelectController.select_all_users()
            
            elif select_widgets["select_filter"].value == "Status" or select_widgets["select_filter"].value == "Admin":
                request = SelectController.select_users_by_filter(column=column, value=bool_value)
            
            else:
                request = SelectController.select_users_by_filter(column=column, value=value)
        
        if table == "Jogos":
            if select_widgets["select_filter"].value == "Todas":
                request = SelectController.select_all_games()

            else:
                request = SelectController.select_games_by_filter(column=column, value=value)


        if table == "Aluguéis":
            if select_widgets["select_filter"].value == "Todas":
                request = SelectController.select_all_games_rental()

            else:
                request = SelectController.select_games_rental_by_filter(column=column, value=value)


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

        select_widgets["select_filter"].value = "Todas"
        select_widgets["input_filter"].value = ""
        select_widgets["input_filter"].visible = False
        select_widgets["select_status_or_admin"].value = None
        select_widgets["select_status_or_admin"].visible = False
        
        if select_widgets["select_table"].value == "Usuários":
            options_columns = ["ID", "Nome", "Email", "Admin", "Status", "Todas"]
        
        elif select_widgets["select_table"].value == "Jogos":
            options_columns = ["ID", "Nome", "Preço", "Quantidade", "Gênero", "Todas"]

        elif select_widgets["select_table"].value == "Aluguéis":
            options_columns = ["ID", "ID do usuário", "ID do jogo", "Data de aluguel", "Data de devolução", "Todas"]

        options_filter = []
        for option in options_columns:
            options_filter.append(ft.DropdownOption(key=option, content=ft.Text(value=option, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)))

        select_widgets["select_filter"].options = options_filter
        select_view.update()
        page.update()


    def select_add_filter_click(e: ControlEvent):

        select_widgets["input_filter"].value = ""
        select_widgets["select_status_or_admin"].value = None

        if select_widgets["select_filter"].value == "Todas":
            select_widgets["input_filter"].visible = False
            select_widgets["select_status_or_admin"].visible = False 
        
        elif select_widgets["select_filter"].value == "Status" or select_widgets["select_filter"].value == "Admin":
            select_widgets["input_filter"].visible = False
            select_widgets["select_status_or_admin"].visible = True
        
        else:
            select_widgets["select_status_or_admin"].visible = False
            select_widgets["input_filter"].visible = True

        select_view.update()
        page.update()


    def insert_inputs_click(e: ControlEvent):
            
            insert_widgets["input_01"].value = ""
            insert_widgets["input_02"].value = ""
            insert_widgets["input_03"].value = ""
            insert_widgets["input_04"].value = ""
            insert_widgets["input_05"].value = ""
            insert_widgets["input_06"].value = ""
            insert_widgets["drop_01"].value = None
            insert_widgets["text_insert"].value = ""

            
            if insert_widgets["select_table"].value == "Jogos":
                insert_widgets["image"].src = "src/ADM/assets/images/pasta_jogos.png"
                insert_widgets["title_database"].value = "REGISTRO DE JOGO"
                insert_widgets["input_01"].label = "Nome"
                insert_widgets["input_02"].label = "Preço"
                insert_widgets["input_03"].label = "Quantidade"
                insert_widgets["input_04"].label = "Gênero"
                insert_widgets["input_05"].label = "descrição"

                insert_widgets["input_03"].password = False
                insert_widgets["input_04"].password = False

                insert_widgets["input_01"].visible = True 
                insert_widgets["input_02"].visible = True               
                insert_widgets["input_03"].visible = True            
                insert_widgets["input_04"].visible = True     
                insert_widgets["input_05"].visible = True
                insert_widgets["input_06"].visible = False
                insert_widgets["button_date"].visible = False
                insert_widgets["drop_01"].visible = False
                insert_widgets["text_insert"].visible = False

            elif insert_widgets["select_table"].value == "Usuários":
                insert_widgets["image"].src = "src/ADM/assets/images/pasta_usuarios.png"
                insert_widgets["title_database"].value = "REGISTRO DE USUÁRIO"
                insert_widgets["input_01"].label = "Nome"
                insert_widgets["input_02"].label = "email"
                insert_widgets["input_03"].label = "senha"         
                insert_widgets["input_04"].label = "Confirmar senha"       
                insert_widgets["drop_01"].label = "Admin"

                insert_widgets["input_03"].password = True
                insert_widgets["input_04"].password = True

                insert_widgets["input_01"].visible = True 
                insert_widgets["input_02"].visible = True               
                insert_widgets["input_03"].visible = True            
                insert_widgets["input_04"].visible = True   
                insert_widgets["input_05"].visible = False
                insert_widgets["input_06"].visible = False
                insert_widgets["button_date"].visible = False
                insert_widgets["drop_01"].visible = True
                insert_widgets["text_insert"].visible = False

            elif insert_widgets["select_table"].value == "Aluguéis":
                insert_widgets["image"].src = "src/ADM/assets/images/pasta_alugueis.png"
                insert_widgets["title_database"].value = "REGISTRO DE ALUGUEL"
                insert_widgets["input_01"].label = "ID do usuário"
                insert_widgets["input_02"].label = "ID do jogo"
                insert_widgets["input_06"].label = "Data de devolução"

                insert_widgets["input_01"].visible = True
                insert_widgets["input_02"].visible = True
                insert_widgets["input_03"].visible = False
                insert_widgets["input_04"].visible = False
                insert_widgets["input_05"].visible = False
                insert_widgets["input_06"].visible = True
                insert_widgets["drop_01"].visible = False
                insert_widgets["button_date"].visible = True
                insert_widgets["button_insert"].visible = True
                insert_widgets["text_insert"].visible = False


            insert_widgets.update()
            page.update()


    def insert_date_click(e: ControlEvent):
        formatted_date = e.control.value.strftime("%d/%m/%Y")
        insert_widgets["input_06"].value = formatted_date
        page.update()

    
    def insert_database_click(e: ControlEvent):

        if insert_widgets["select_table"].value == "Jogos":
            name = insert_widgets["input_01"].value
            price = insert_widgets["input_02"].value
            quantity = insert_widgets["input_03"].value
            genre = insert_widgets["input_04"].value
            description = insert_widgets["input_05"].value

            request = InsertController().insert_game(name=name, price=price, quantity=quantity, genre=genre, description=description)

            if request["status"] == "error":
                insert_widgets["text_insert"].value = request["message"]
                insert_widgets["text_insert"].visible = True
                page.update()
                return None
            
            insert_widgets["text_insert"].value = request["message"]
            insert_widgets["text_insert"].visible = True
            insert_widgets["input_01"].value = ""
            insert_widgets["input_02"].value = ""
            insert_widgets["input_03"].value = ""
            insert_widgets["input_04"].value = ""
            insert_widgets["input_05"].value = ""

            page.update()


        elif insert_widgets["select_table"].value == "Usuários":
            name = insert_widgets["input_01"].value
            email = insert_widgets["input_02"].value
            password = insert_widgets["input_03"].value
            confirm_password = insert_widgets["input_04"].value
            admin = insert_widgets["drop_01"].value

            request = InsertController().insert_user(name=name, email=email, password=password, confirm_password=confirm_password, admin=admin)

            if request["status"] == "error":
                insert_widgets["text_insert"].value = request["message"]
                insert_widgets["text_insert"].visible = True
                page.update()
                return None

            insert_widgets["text_insert"].value = request["message"]
            insert_widgets["text_insert"].visible = True
            insert_widgets["input_01"].value = ""
            insert_widgets["input_02"].value = ""
            insert_widgets["input_03"].value = ""
            insert_widgets["input_04"].value = ""
            insert_widgets["drop_01"].value = ""

            page.update()

        elif insert_widgets["select_table"].value == "Aluguéis":
            user_id = insert_widgets["input_01"].value
            game_id = insert_widgets["input_02"].value
            date_return = insert_widgets["input_06"].value

            request = InsertController().insert_game_rental(user_id=user_id, game_id=game_id, date_return=date_return)

            if request["status"] == "error":
                insert_widgets["text_insert"].value = request["message"]
                insert_widgets["text_insert"].visible = True
                page.update()
                return None

            insert_widgets["text_insert"].value = request["message"]
            insert_widgets["text_insert"].visible = True
            insert_widgets["input_01"].value = ""
            insert_widgets["input_02"].value = ""
            insert_widgets["input_06"].value = ""

            page.update()
    
    def update_columns_click(e: ControlEvent):

        update_widgets["update_column"].value = "ID"
        update_widgets["update_input_filter"].value = ""

        if update_widgets["update_table"].value == "Usuários":
            options_columns = ["ID", "Nome", "Email", "Senha", "Admin", "Status"]
        
        elif update_widgets["update_table"].value == "Jogos":
            options_columns = ["ID", "Nome", "Preço", "Quantidade", "Gênero"]

        elif update_widgets["update_table"].value == "Aluguéis":
            options_columns = ["ID", "ID do usuário", "ID do jogo", "Data de aluguel", "Data de devolução"]

        options_filter = []
        for option in options_columns:
            options_filter.append(ft.DropdownOption(key=option, content=ft.Text(value=option, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)))

        update_widgets["update_column"].options = options_filter
        update_inputs_click(e)
        update_view.update()
        page.update()

    def update_add_filter_click(e: ControlEvent):

        update_widgets["update_input_filter"].value = ""
        update_widgets["update_select_filter"].value = None
        update_widgets["update_text"].value = ""
        update_widgets["update_text"].visible = False

        if update_widgets["update_column"].value == "Admin" or update_widgets["update_column"].value == "Status":
            update_widgets["update_input_filter"].visible = False
            update_widgets["update_select_filter"].visible = True
        
        else:
            update_widgets["update_input_filter"].visible = True
            update_widgets["update_select_filter"].visible = False
        

        update_view.update()
        page.update()

    def update_inputs_click(e: ControlEvent):

        update_widgets["input_01"].value = ""
        update_widgets["input_02"].value = ""
        update_widgets["input_03"].value = ""
        update_widgets["input_04"].value = ""
        update_widgets["input_05"].value = ""
        update_widgets["input_06"].value = ""
        update_widgets["input_07"].value = ""
        update_widgets["drop_01"].value = None
        update_widgets["drop_02"].value = None
        update_widgets["update_text"].value = ""
        update_widgets["update_text"].visible = False

        if update_widgets["update_table"].value == "Usuários":
            update_widgets["input_01"].label = "Nome"
            update_widgets["input_02"].label = "Email"
            update_widgets["input_03"].label = "Senha"
            update_widgets["drop_01"].label = "Admin"
            update_widgets["drop_02"].label = "Status"

            update_widgets["input_03"].password = True

            update_widgets["input_01"].visible = True
            update_widgets["input_02"].visible = True
            update_widgets["input_03"].visible = True
            update_widgets["drop_01"].visible = True
            update_widgets["drop_02"].visible = True
            update_widgets["button_update"].visible = True

            update_widgets["input_04"].visible = False
            update_widgets["input_05"].visible = False
            update_widgets["input_06"].visible = False
            update_widgets["input_07"].visible = False
            update_widgets["button_date"].visible = False
            update_widgets["button_date2"].visible = False

        elif update_widgets["update_table"].value == "Jogos":
            update_widgets["input_01"].label = "Nome"
            update_widgets["input_02"].label = "Preço"
            update_widgets["input_03"].label = "Quantidade"
            update_widgets["input_04"].label = "Gênero"
            update_widgets["input_05"].label = "descrição"

            update_widgets["input_03"].password = False

            update_widgets["input_01"].visible = True
            update_widgets["input_02"].visible = True
            update_widgets["input_03"].visible = True
            update_widgets["input_04"].visible = True
            update_widgets["input_05"].visible = True
            update_widgets["button_update"].visible = True

            update_widgets["input_06"].visible = False
            update_widgets["input_07"].visible = False
            update_widgets["drop_01"].visible = False
            update_widgets["drop_02"].visible = False
            update_widgets["button_date"].visible = False
            update_widgets["button_date2"].visible = False


        elif update_widgets["update_table"].value == "Aluguéis":
            update_widgets["input_01"].label = "ID do usuário"
            update_widgets["input_02"].label = "ID do jogo"
            update_widgets["input_06"].label = "Data de aluguel"
            update_widgets["input_07"].label = "Data de devolução"

            update_widgets["input_03"].password = False

            update_widgets["input_01"].visible = True
            update_widgets["input_02"].visible = True
            update_widgets["input_06"].visible = True
            update_widgets["input_07"].visible = True
            update_widgets["button_date"].visible = True
            update_widgets["button_date2"].visible = True
            update_widgets["button_update"].visible = True

            update_widgets["input_03"].visible = False
            update_widgets["input_04"].visible = False
            update_widgets["input_05"].visible = False
            update_widgets["drop_01"].visible = False
            update_widgets["drop_02"].visible = False
            

        update_view.update()
        page.update()

    def update_database_click(e: ControlEvent):

        if update_widgets["update_table"].value == "Usuários":
            if update_widgets["input_01"].value not in ["", None]:
                name = update_widgets["input_01"].value
            else:
                name = None

            if update_widgets["input_02"].value not in ["", None]:
                email = update_widgets["input_02"].value
            else:
                email = None

            if update_widgets["input_03"].value not in ["", None]:
                password = update_widgets["input_03"].value
            else:
                password = None
            
            if update_widgets["drop_01"].value not in ["", None]:
                admin = update_widgets["drop_01"].value
            else:
                admin = None

            if update_widgets["drop_02"].value not in ["", None]:
                status = update_widgets["drop_02"].value
            else:
                status = None

            request = UpdateController().update_user(name=name, email=email, password=password, admin=admin, status=status, filter_column=update_widgets["update_column"].value, filter_value=update_widgets["update_input_filter"].value)

            if request["status"] == "error":
                update_widgets["update_text"].value = request["message"]
                update_widgets["update_text"].visible = True
                page.update()
                return None
            
            update_widgets["update_text"].value = request["message"]
            update_widgets["update_text"].visible = True

            update_widgets["update_input_filter"].value = ""
            update_widgets["input_01"].value = ""
            update_widgets["input_02"].value = ""
            update_widgets["input_03"].value = ""
            update_widgets["drop_01"].value = None
            update_widgets["drop_02"].value = None

            page.update()

        elif update_widgets["update_table"].value == "Jogos":
            if update_widgets["input_01"].value not in ["", None]:
                name = update_widgets["input_01"].value
            else:
                name = None

            if update_widgets["input_02"].value not in ["", None]:
                price = update_widgets["input_02"].value
            else:
                price = None
            
            if update_widgets["input_03"].value not in ["", None]:
                quantity = update_widgets["input_03"].value
            else:
                quantity = None

            if update_widgets["input_04"].value not in ["", None]:
                genre = update_widgets["input_04"].value
            else:
                genre = None
            
            if update_widgets["input_05"].value not in ["", None]:
                description = update_widgets["input_05"].value
            else:
                description = None

            request = UpdateController().update_game(name=name, price=price, quantity=quantity, genre=genre, description=description, filter_column=update_widgets["update_column"].value, filter_value=update_widgets["update_input_filter"].value)

            if request["status"] == "error":
                update_widgets["update_text"].value = request["message"]
                update_widgets["update_text"].visible = True
                page.update()
                return None
            
            update_widgets["update_text"].value = request["message"]
            update_widgets["update_text"].visible = True

            update_widgets["input_01"].label = ""
            update_widgets["input_02"].label = ""
            update_widgets["input_03"].label = ""
            update_widgets["input_04"].label = ""
            update_widgets["input_05"].label = ""

            page.update()



        elif update_widgets["update_table"].value == "Aluguéis":
            if update_widgets["input_01"].value not in ["", None]:
                user_id = update_widgets["input_01"].value
            else:
                user_id = None

            if update_widgets["input_02"].value not in ["", None]:
                game_id = update_widgets["input_02"].value
            else:
                game_id = None
            
            if update_widgets["input_06"].value not in ["", None]:
                rental_date = update_widgets["input_06"].value
            else:
                rental_date = None

            if update_widgets["input_07"].value not in ["", None]:
                return_date = update_widgets["input_07"].value
            else:
                return_date = None

            request = UpdateController().update_rental(user_id=user_id, game_id=game_id, rental_date=rental_date, return_date=return_date, filter_column=update_widgets["update_column"].value, filter_value=update_widgets["update_input_filter"].value)

            if request["status"] == "error":
                update_widgets["update_text"].value = request["message"]
                update_widgets["update_text"].visible = True
                page.update()
                return None
            
            update_widgets["update_text"].value = request["message"]
            update_widgets["update_text"].visible = True

            update_widgets["input_01"].value = ""
            update_widgets["input_02"].value = ""
            update_widgets["input_06"].value = ""
            update_widgets["input_07"].value = ""

            page.update()

        if request["status"] == "error":
            update_widgets["update_text"].value = request["message"]
            update_widgets["update_text"].visible = True
            page.update()
            return None
        
        update_widgets["update_text"].value = request["message"]
        update_widgets["update_text"].visible = True

        update_widgets["update_input_filter"].value = ""
        update_widgets["input_01"].value = ""
        update_widgets["input_02"].value = ""
        update_widgets["input_03"].value = ""
        update_widgets["input_04"].value = ""
        update_widgets["input_05"].value = ""
        update_widgets["input_06"].value = ""

        page.update()

    def update_date_click(e: ControlEvent):
        formatted_date = e.control.value.strftime("%d/%m/%Y")
        update_widgets["input_06"].value = formatted_date
        page.update()

    def update_date2_click(e: ControlEvent):
        formatted_date = e.control.value.strftime("%d/%m/%Y")
        update_widgets["input_07"].value = formatted_date
        page.update()

    def update_close_alert(e: ControlEvent):
        page.close(update_alert)
        page.update()

        if e.control.text == "SIM":
            update_database_click(e)

    def delete_database(e: ControlEvent):

        id = delete_widgets["delete_id_input"].value

        if delete_widgets["delete_table"].value == "Usuários":
            request = ""

        if delete_widgets["delete_table"].value == "Jogos":
            request = ""

        if delete_widgets["delete_table"].value == "Aluguéis":
            request = ""

        if request["status"] == "error":
            delete_widgets["delete_text"].value = request["message"]
            delete_widgets["delete_text"].visible = True
            page.update()
            return None
        
        delete_widgets["delete_text"]. value = request["message"]
        delete_widgets["delete_text"].visible = True

        delete_widgets["delete_id_input"].value = ""

        page.update()

    def delete_close_alert(e: ControlEvent):
        page.close(delete_alert)
        page.update()

        if e.control.text == "SIM":
            delete_database(e)

            

    ### WIDGETS DO APLICATIVO ###

    login_widgets = {
        "logo_project": ft.Image(src="src/ADM/assets/images/logo_projeto.png", width=200, height=200),
        "text_login": ft.Text(value="LOGIN DE USUÁRIO", size=30, text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular", color=ft.Colors.PURPLE_300)),
        "user_email": ft.TextField(label="Email", width=300, border_color=ft.Colors.PURPLE_200),
        "user_password": ft.TextField(label="Senha", width=300, password=True, border_color=ft.Colors.PURPLE_200),
        "button_login": ft.Button(text="ENTRAR NA CONTA", width=300, on_click=login_user_click, color="#180030", bgcolor=ft.Colors.PURPLE_200, autofocus=True),
        "button_create_account": ft.TextButton(text="Criar uma nova conta", style=ft.ButtonStyle(color=ft.Colors.PURPLE_100), on_click=go_to_create_click),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER)
    }

    create_account_widgets = {
        "user_icon": ft.Image(src="src/ADM/assets/images/user.png", width=150, height=150),
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
                ft.DropdownOption(key="INSERIR", content= ft.Text("INSERIR", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "CONSULTAR", content= ft.Text("CONSULTAR", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "ATUALIZAR", content= ft.Text("ATUALIZAR", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key = "DELETAR", content= ft.Text("DELETAR", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            col=3,
            value="CONSULTAR",
            border_color=ft.Colors.WHITE,
            border_width=2,
            bgcolor="#6100b5",
            on_change=go_to_operations_click,
            text_style=ft.TextStyle(color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            
        ),    
    }

    select_widgets = {
    "title_database": ft.Text(value="REGISTROS NO BANCO DE DADOS", col=10, style=ft.TextStyle(font_family="LilitaOne-Regular",color=ft.Colors.BLACK, size=20)),
        "button_reload": ft.IconButton(icon=ft.Icons.REFRESH, col=2, on_click=select_results_click, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#601e9e")),
        "text_no_results": ft.Text(value="Sem resultados por enquanto", text_align=ft.TextAlign.CENTER, style=ft.TextStyle(font_family="LilitaOne-Regular",color="#441b70", size=20)),
        "text_error": ft.Text(value="", visible=False, text_align=ft.TextAlign.CENTER),
        "input_filter": ft.TextField(label="Digite o filtro", border_color=ft.Colors.PURPLE_200, border_width=1, width=150, visible=False),
        "select_table": ft.Dropdown(
            options=[
                ft.DropdownOption(key="Jogos", content=ft.Text("Jogos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key="Usuários", content=ft.Text("Usuários", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)), 
                ft.DropdownOption(key="Aluguéis", content=ft.Text("Aluguéis", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            width=150,
            value="Usuários",
            border_color=ft.Colors.PURPLE_200,
            border_width=2,
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
            border_width=2, 
            width=150,
            on_change=select_add_filter_click
        ),
        "select_status_or_admin":ft.Dropdown(
            options=[
                ft.DropdownOption(key="True", content=ft.Text(value="True", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="False", content=ft.Text(value="False", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            label="Filtro", 
            border_color=ft.Colors.PURPLE_200, 
            border_width=2, 
            width=150, 
            visible=False
        )
        
    }

    insert_widgets = {
        "image": ft.Image(src="src/ADM/assets/images/pasta_jogos.png", fit=ft.ImageFit.COVER, width=200, height=200),
        "title_database": ft.Text(value="REGISTRO DE JOGO", size=30, style=ft.TextStyle(font_family="LilitaOne-Regular",color=ft.Colors.PURPLE_300)),
        "select_table": ft.Dropdown(
            options=[
                ft.DropdownOption(key="Usuários", content=ft.Text("Usuários", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Jogos", content=ft.Text("Jogos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Aluguéis", content=ft.Text("Aluguéis", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            value="Jogos",
            border_color=ft.Colors.PURPLE_300,
            on_change=insert_inputs_click,
            border_width=2, 
            width=150
        ),
        "input_01": ft.TextField(label="Nome",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible=True),
        "input_02": ft.TextField(label="Preço", width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_03": ft.TextField(label="Quantidade", width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_04": ft.TextField(label="Gênero",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_05": ft.TextField(label="Descrição",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_06": ft.TextField(width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= False),
        "text_insert": ft.Text(value="", visible=False, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        "button_date": ft.IconButton(
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date= datetime.now().date(),
                    last_date= datetime(year=2050, month=12, day=31),
                    on_change=insert_date_click,
                    cancel_text= "Cancelar",
                    confirm_text= "Confirmar",
                    field_label_text= "data de devolução",
                    help_text="Escolha uma data"

                )
            ),
            icon=ft.Icons.DATE_RANGE,
            icon_color=ft.Colors.PURPLE_300,
            visible= False
        ),
        "drop_01": ft.Dropdown(
            options=[
                ft.DropdownOption(key="True", content=ft.Text(value="True", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="False", content=ft.Text(value="False", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            visible=False,
            width=300,
            border_color=ft.Colors.PURPLE_500,
            border_width=2
        ),
        "button_insert": ft.ElevatedButton(
            text="INSERIR", 
            icon=ft.Icons.CHECK,
            width=150,
            on_click=insert_database_click,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.PURPLE_600,
                icon_color=ft.Colors.WHITE,
                color=ft.Colors.WHITE,
            )
        )
    }

    update_widgets = {
        "image": ft.Image(src="src/ADM/assets/images/pasta_update.png", width=200, height=200),
        "title": ft.Text(value="ATUALIZAR DADOS", size=30, style=ft.TextStyle(font_family="LilitaOne-Regular",color=ft.Colors.PURPLE_300)),
        "update_table": ft.Dropdown(
            options=[
                ft.DropdownOption(key="Usuários", content=ft.Text("Usuários", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Jogos", content=ft.Text("Jogos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Aluguéis", content=ft.Text("Aluguéis", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            value="Jogos",
            width=150,
            border_color=ft.Colors.PURPLE_300,
            border_width=2,
            on_change=update_columns_click
        ),
        "update_column": ft.Dropdown(
            options=[
                ft.DropdownOption(key="ID", content=ft.Text("ID", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Nome", content=ft.Text("Nome", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Preço", content=ft.Text("Preço", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Quantidade", content=ft.Text("Quantidade", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Gênero", content=ft.Text("Gênero", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Descrição", content=ft.Text("descrição", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
            ],
            value="ID",
            width=150,
            border_color=ft.Colors.PURPLE_300,
            border_width=2,
            on_change=update_add_filter_click
        ),
        "update_input_filter": ft.TextField(label="Filtro", width=150, border_color=ft.Colors.PURPLE_300, border_width=2),
        "update_select_filter": ft.Dropdown(
            options=[
                ft.DropdownOption(key="True", content=ft.Text(value="True", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="False", content=ft.Text(value="False", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            label="Filtro",
            visible=False,
            width=150,
            border_color=ft.Colors.PURPLE_300,
            border_width=2
        ),
        "input_01": ft.TextField(label="Nome",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible=True),
        "input_02": ft.TextField(label="Preço", width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_03": ft.TextField(label="Quantidade", width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_04": ft.TextField(label="Gênero",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_05": ft.TextField(label="Descrição",width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= True),
        "input_06": ft.TextField(width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= False),
        "input_07": ft.TextField(width=300, border_color=ft.Colors.PURPLE_500, border_width=2, visible= False),
        "button_date": ft.IconButton(
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date= datetime.now().date(),
                    last_date= datetime(year=2050, month=12, day=31),
                    on_change=update_date_click,
                    cancel_text= "Cancelar",
                    confirm_text= "Confirmar",
                    field_label_text= "data de aluguel",
                    help_text="Escolha uma data"
                )
            ),
            icon=ft.Icons.DATE_RANGE,
            icon_color=ft.Colors.PURPLE_300,
            visible= False
        ),
        "button_date2": ft.IconButton(
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date= datetime.now().date(),
                    last_date= datetime(year=2050, month=12, day=31),
                    on_change=update_date2_click,
                    cancel_text= "Cancelar",
                    confirm_text= "Confirmar",
                    field_label_text= "data de devolução",
                    help_text="Escolha uma data"
                )
            ),
            icon=ft.Icons.DATE_RANGE,
            icon_color=ft.Colors.PURPLE_300,
            visible= False
        ),
        "drop_01": ft.Dropdown(
            options=[
                ft.DropdownOption(key="True", content=ft.Text(value="True", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="False", content=ft.Text(value="False", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            visible=False,
            width=300,
            border_color=ft.Colors.PURPLE_500,
            border_width=2
        ),
        "drop_02": ft.Dropdown(
            options=[
                ft.DropdownOption(key="True", content=ft.Text(value="True", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="False", content=ft.Text(value="False", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            visible=False,
            width=300,
            border_color=ft.Colors.PURPLE_500,
            border_width=2
        ),
        "button_update": ft.ElevatedButton(
            text="ATUALIZAR", 
            icon=ft.Icons.CHECK,
            width=150,
            on_click=lambda e: page.open(update_alert),
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.PURPLE_600,
                icon_color=ft.Colors.WHITE,
                color=ft.Colors.WHITE
            )
        ),
        "update_text": ft.Text(value="", visible=False, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)

    }

    delete_widgets = {
        "image": ft.Image(src="src/ADM/assets/images/lixeira.png", width=150, height=150),
        "title": ft.Text(value="DELETAR DADOS", color=ft.Colors.PURPLE_300, font_family="LilitaOne-Regular", size=30),
        "delete_table": ft.Dropdown(
            options=[
                ft.DropdownOption(key="Usuários", content=ft.Text(value="Usuários", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Jogos", content=ft.Text(value="Jogos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)),
                ft.DropdownOption(key="Aluguéis", content=ft.Text(value="Aluguéis", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD))
            ],
            label="Tabela",
            width=150,
            border_color=ft.Colors.PURPLE_500,
            border_width=2
        ),
        "delete_id_input": ft.TextField(label="ID", width=150, border_color=ft.Colors.PURPLE_500, border_width=2),
        "button_delete": ft.ElevatedButton(
            text="DELETAR",
            icon=ft.Icons.DELETE,
            width=300,
            on_click=lambda e: page.open(delete_alert),
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.PURPLE_500,
                icon_color=ft.Colors.WHITE,
                color=ft.Colors.WHITE
            )
        ),
        "delete_text": ft.Text(value="", visible=False, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        "alert_text": ft.Text(value="REGISTROS SÃO DELETADOS PERMANENTEMENTE!", color=ft.Colors.PURPLE_400, font_family="LilitaOne-Regular", size=15)

    }


    ### WIDGETS DINÂMICOS ###

        
    select_results = ft.Container(
        content=select_widgets["text_no_results"],
    )

    update_alert = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Atualizar registro(s)"),
        content=ft.Text(value="Certeza que deseja fazer a atualização de dados?"),
        actions=[
            ft.TextButton(text="SIM", on_click=update_close_alert, style=ft.ButtonStyle(color=ft.Colors.PURPLE_300)),
            ft.TextButton(text="NÃO", on_click=update_close_alert, style=ft.ButtonStyle(color=ft.Colors.PURPLE_300))
        ]
    )

    delete_alert = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="Deletar registro"),
        content=ft.Text(value="Certeza que deseja deletar o registro permanentemente?"),
        actions=[
            ft.TextButton(text="SIM", on_click=delete_close_alert, style=ft.ButtonStyle(color=ft.Colors.PURPLE_300)),
            ft.TextButton(text="NÃO", on_click=delete_close_alert, style=ft.ButtonStyle(color=ft.Colors.PURPLE_300))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
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
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
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
                                        select_widgets["input_filter"],
                                        select_widgets["select_status_or_admin"]
                                    ]
                                )

                            )    
                        ]
                    )
                ),

                ft.Container(
                    col={"sm": 12, "md": 11, "lg": 10, "xl": 9},
                    bgcolor="#9c57f7",
                    margin=ft.margin.all(40),
                    border_radius=10,
                    padding=0,
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                bgcolor="#8944e3",
                                padding=ft.padding.all(10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        select_widgets["title_database"],
                                        select_widgets["button_reload"]
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.all(30),
                                content=ft.ResponsiveRow(
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

    insert_view = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=home_bar
                ),

                ft.Container(
                    col=6,
                    height=600,
                    padding=ft.Padding(right=0, left=40, top=40, bottom=40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            insert_widgets["image"],
                            insert_widgets["title_database"]
                        ]
                    )
                ),

                ft.Container(
                    col=6,
                    height=600,
                    padding=ft.Padding(right=40, left=0, top=40, bottom=40),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            insert_widgets["select_table"],
                            insert_widgets["input_01"],
                            insert_widgets["input_02"],
                            insert_widgets["input_03"],
                            insert_widgets["input_04"],
                            insert_widgets["input_05"],
                            insert_widgets["drop_01"],
                            ft.Container(
                                margin=ft.margin.only(left=50),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        insert_widgets["input_06"],
                                        insert_widgets["button_date"]
                                    ]
                                )
                            ),
                            insert_widgets["button_insert"],
                            insert_widgets["text_insert"],
                        ]
                    )
                )

            ]
        )
    )

    update_view = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=home_bar
                ),

                ft.Container(
                    col=5,
                    height=600,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            update_widgets["image"],
                            update_widgets["title"]
                        ]
                    )
                ),

                ft.Container(
                    col=6,
                    height=600,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,                        
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(bottom=20, top=70),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        update_widgets["update_table"],
                                        update_widgets["update_column"],
                                        update_widgets["update_input_filter"],
                                        update_widgets["update_select_filter"]
                                    ]
                                )
                            ),

                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        update_widgets["input_01"],
                                        update_widgets["input_02"],
                                        update_widgets["input_03"],
                                        update_widgets["input_04"],
                                        update_widgets["input_05"],
                                        update_widgets["drop_01"],
                                        update_widgets["drop_02"],
                                        ft.Container(
                                            margin=ft.margin.only(left=50),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    update_widgets["input_06"],
                                                    update_widgets["button_date"]
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            margin=ft.margin.only(left=50),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    update_widgets["input_07"],
                                                    update_widgets["button_date2"]
                                                ]
                                            )
                                        ),
                                        update_widgets["button_update"],
                                        update_widgets["update_text"]
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    )

    delete_view = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=home_bar
                ),

                ft.Container(
                    margin=ft.margin.only(bottom=40, top=40),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            delete_widgets["image"],
                            delete_widgets["title"]
                        ]
                    )
                ),

                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            delete_widgets["delete_table"],
                            delete_widgets["delete_id_input"]
                        ]
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=10),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            delete_widgets["button_delete"],
                            delete_widgets["delete_text"],
                            
                        ]
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=180),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            delete_widgets["alert_text"]    
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

