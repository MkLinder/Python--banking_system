from database.Accounts import accounts
from database.Account_operations import account_operations
from database.Registered_users import users

def create_account():
    new_account = {"agencia": "0001", "conta": "", "titular": "", "senha": ""}
    valid_cpf = False

    while valid_cpf == False:
        user_cpf = str(input("Digite o seu cpf [000.111.222-33]: "))

        if len(user_cpf) < 14:
            print("Formato inválido!")
            
        else:
            user_found = [u for u in users if u["cpf"] == user_cpf]

            if user_found:
                db_account_found = [
                    a for a in accounts["accounts_list"] if a["conta"] == user_found[0]["conta"]
                ]

                if db_account_found:
                    print("Já existe uma conta vinculada a este CPF.")

                else:
                    new_account["titular"] = user_found[0]["nome"]
                    new_account["conta"] = accounts["account_number"]

                    account_operations.append({
                        "conta": new_account["conta"],
                        "balance": 0, 
                        "limit": 500, 
                        "extract": [], 
                        "withdrawals_made": 0, 
                        "WITHDRAWALS_LIMIT": 3
                    })

                    user_found[0]["conta"] = new_account["conta"]
                    accounts["account_number"] += 1
                    valid_cpf = True
                    break
            else:
                print("Usuário não encontrado! Faça o cadastro de cliente antes de abrir a conta.")

    while new_account["senha"] == "":
        new_pass = str(input("Crie uma senha com no mínimo 4 números: "))
        if len(new_pass) < 4:
            print("A senha deve ter no mínimo 4 números!")
        else:
            new_account["senha"] = new_pass

    accounts["accounts_list"].append(new_account)
    valid_cpf = False
    print("Conta criada com sucesso! Você já pode acessar a sua conta.")                              