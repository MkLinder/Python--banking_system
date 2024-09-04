from database.Registered_users import users

def validate_cpf():

    cpf = str(input("Digite seu cpf [00011122233]: "))
    if len(cpf) != 11:
        print("Digite um cpf válido no formato [00011122233].")

    elif len(users) == 0:
        return cpf
    
    else:
        cpf_found = [u for u in users if u["cpf"] == cpf]

        if cpf_found:
            print("Este CPF não está disponível.")
        else:
            return cpf      