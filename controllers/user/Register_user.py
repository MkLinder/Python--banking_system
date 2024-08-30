from database.Registered_users import users
from middleware.Validate_cpf import validate_cpf
from middleware.Name_formatter import name_formatter


def get_user_data():
    def register_user(name, date, cpf, address):
        new_user = {"nome": name, "data_nascimento": date, "cpf": cpf, "endereco": address, "account": False}
        users.append(new_user)
        print("Usuário cadastrado!")

    complete_user = {"name": "", "date": "", "cpf": "", "address": ""}

    while complete_user["name"] == "":
        name = str(input("Digite seu nome completo: "))
        if len(name) < 4:
            print("Digite um nome válido.")
        else :
            formatted_name = name_formatter(name)
            complete_user["name"] = formatted_name.rstrip()
        
    while complete_user["date"] == "":
        date = str(input("Digite sua data de nascimento [dd/mm/aaaa]: "))
        if len(date) < 10:
            print("Digite um formato de data válido [dd/mm/aaaa].")
        else:
            complete_user["date"] = date

    while complete_user["cpf"] == "":        
        cpf = str(input("Digite seu cpf [000.111.222-33]: "))
        if len(cpf) < 14:
            print("Digite um cpf válido no formato [000.111.222-33].")
        else:
            is_valid_cpf = validate_cpf(cpf)

            if is_valid_cpf:
                complete_user["cpf"] = cpf

    while complete_user["address"] == "":
        address = str(input("Digite o seu endereço [Rua, número - bairro - cidade/UF]: "))
        if len(address) < 20:
            print("Digite um endereço válido.") 
        else:
            complete_user["address"] = address

    register_user(
        complete_user["name"], 
        complete_user["date"], 
        complete_user["cpf"], 
        complete_user["address"]
    )