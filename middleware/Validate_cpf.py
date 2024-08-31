from database.Registered_users import users

def validate_cpf(cpf):

    if len(users) == 0:
        return True

    else:
        cpf_found = [u for u in users if u["cpf"] == cpf]

        if cpf_found:
            print("Este CPF não está disponível.")
        else:
            return True      