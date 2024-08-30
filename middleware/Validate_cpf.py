from database.Registered_users import users

def validate_cpf(cpf):

    if len(users) == 0:
        return True

    else:
        for user in users:
            if user["cpf"] == cpf:
                print("Este CPF não está disponível.")
                return False

            else:
                return True  