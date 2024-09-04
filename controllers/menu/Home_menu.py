from controllers.account.Create_account import create_account
from controllers.account.Access_account import access_account

from controllers.user.Register_user import register_user

def home_menu():
    options_menu = """
    ========== FICTI BANK ==========
    Seja bem vindo(a).
    O que você deseja?

    [C] Cadastrar cliente
    [A] Abrir conta
    [E] Acessar conta
    [Q] Sair
    ================================
    """

    option = input(options_menu)

    while True:

        if option == 'c':
            register_user()
            option = input(options_menu)

        elif option == 'a':
            create_account()
            option = input(options_menu)

        elif option == 'e':
            access_account()
            option = input(options_menu)

        elif option == 'q':
            print("Obrigado pela preferência, volte sempre.")
            break

        else:
            print("Opção inválida!")
            option = input(options_menu)