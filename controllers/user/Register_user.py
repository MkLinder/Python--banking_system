from database.Registered_users import users

from middleware.Validate_cpf import validate_cpf
from middleware.Name_formatter import name_formatter


def register_user():
    
    def get_user_data(name, date, cpf, address):
        new_user = {"nome": name, "data_nascimento": date, "cpf": cpf, "endereco": address, "contas": []}
        
        users.append(new_user)
        print("\nUsuário cadastrado!")

    user_data = {"name": "", "date": "", "cpf": "", "address": ""}

    while user_data["name"] == "":
        name = str(input("Digite seu nome completo: "))
        if len(name) < 4:
            print("\nDigite um nome válido.")
        else :
            formatted_name = name_formatter(name)
            user_data["name"] = formatted_name.rstrip()
        
    while user_data["date"] == "":
        date = str(input("Digite sua data de nascimento [dd/mm/aaaa]: "))
        if len(date) < 10:
            print("\nDigite um formato válido [dd/mm/aaaa].")
        else:
            user_data["date"] = date

    while user_data["cpf"] == "":
            is_valid_cpf = validate_cpf()

            if is_valid_cpf:
                user_data["cpf"] = is_valid_cpf

    while user_data["address"] == "":
        address = str(input("Digite o seu endereço [Rua, número - bairro - cidade/UF]: "))
        if len(address) < 20:
            print("\nDigite um endereço válido.") 
        else:
            user_data["address"] = address

    get_user_data(
        user_data["name"], 
        user_data["date"], 
        user_data["cpf"], 
        user_data["address"]
    )