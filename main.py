from controllers.menu.Home_menu import home_menu

from controllers.account.Create_account import create_account
from controllers.account.Access_account import access_account

from controllers.user.Register_user import get_user_data

while True:

    option = input(home_menu)

    if option == 'c':
         get_user_data()
    elif option == 'a':
        create_account()
    elif option == 'e':
        access_account()
    elif option == 'q':
        print("Obrigado pela preferência, volte sempre.")
        break