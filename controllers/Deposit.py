from database.default_inf import default

def deposit(deposit_amount):
    default["balance"] += deposit_amount
    default["extract"].append(f"Deposito: R$ {deposit_amount:.2f}") 
    print(f"Seu depósito de R$ {deposit_amount:.2f} foi efetuado!")