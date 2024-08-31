from database.Registered_users import users
from database.Accounts import accounts
from database.Account_operations import account_operations

from controllers.menu.Menu_account_options import account_menu

from controllers.account.Deposit import deposit
from controllers.account.Withdrawal import withdrawal
from controllers.account.Extract import extract


def access_account():
    user_cpf = str(input("Digite seu CPF [000.111.222-33]: "))
    db_user_found = [u for u in users if u["cpf"] == user_cpf]
    if db_user_found :
        db_account_found = [a for a in accounts["accounts_list"] if a["conta"] == db_user_found[0]["conta"]]

        if db_account_found:
            db_acc_operations = [
                a_o for a_o in account_operations if a_o["conta"] == db_account_found[0]["conta"]
            ]

            user_password = input("Digite sua senha de acesso: ")
            
            if user_password != db_account_found[0]["senha"]:
                print("Senha incorreta!")
            else:    
                account_options = input(account_menu(db_user_found[0]["nome"]))

                while account_options != 'q':
                    if account_options == 'd':
                        deposit(db_acc_operations[0])
                        account_options = input(account_menu(db_user_found[0]["nome"]))
                            
                    elif account_options == 's':
                        withdrawal(db_acc_operations[0])
                        account_options = input(account_menu(db_user_found[0]["nome"]))


                    elif account_options == "e":
                        extract(db_acc_operations[0])
                        account_options = input(account_menu(db_user_found[0]["nome"]))

                    elif account_options == "q":
                        break    
                    
                    else:
                        print("Operação inválida! Por favor, digite uma operação válida.")
        else:
            print("Nenhuma conta vinculada a este CPF!")
    else:
        print("Usuário não encontrado! ")