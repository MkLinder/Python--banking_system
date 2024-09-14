from database.Registered_users import users
from database.Accounts import accounts
from database.Account_operations import account_operations

from controllers.menu.Account_operations_menu import account_operations_menu


def access_account():
    user_cpf = str(input("Digite seu CPF [00011122233]: "))
    db_user_found = [u for u in users if u["cpf"] == user_cpf]
    
    if db_user_found :
        db_user_accounts = [
            a for a in db_user_found[0]["contas"]
        ]

        if len(db_user_accounts) == 0:
            print("\nNenhuma conta bancária cadastrada para este usuário.")

        elif len(db_user_accounts) == 1:
            db_search_acc = [
                a for a in accounts["accounts_list"] if a["conta"] == db_user_accounts[0]
            ]

            user_password = input("Digite sua senha de acesso: ")
                
            if user_password != db_search_acc[0]["senha"]:
                print("\nSenha incorreta!")

            else:    
                db_acc_operations = [ 
                    a_o for a_o in account_operations if a_o["conta"] == db_user_accounts[0]
                ]

                account_operations_menu(
                    db_user_found[0]["nome"],
                    acc_operations = db_acc_operations[0]
                )   

        elif len(db_user_accounts) > 1:
            choose_account = int(input("Número da conta que deseja acessar: "))
            search_account = [a for a in db_user_accounts if a == choose_account]

            if search_account:
                db_search_acc = [
                    a for a in accounts["accounts_list"] if a["conta"] == search_account[0]
                ]

                user_password = input("Digite sua senha de acesso: ")
                
                if user_password != db_search_acc[0]["senha"]:
                    print("\nSenha incorreta!")

                else:    
                    db_acc_operations = [ 
                        a_o for a_o in account_operations if a_o["conta"] == search_account[0]
                    ]

                    account_operations_menu(
                        db_user_found[0]["nome"],
                        acc_operations = db_acc_operations[0]
                    )

            if not search_account:
                print("\nConta não encontrada!")      

        else:
            print("\nNenhuma conta vinculada a este CPF!")
    else:
        print("\nUsuário não encontrado! ")