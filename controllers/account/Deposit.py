def deposit(acc_operation):
    
    deposit_amount = int(input("Digite o valor que deseja depositar: R$"))
    if deposit_amount <= 0:
        print("Valor inválido!")

    else:
        acc_operation["balance"] += deposit_amount
        acc_operation["extract"].append(f"Deposito: R$ {deposit_amount:.2f}") 
        print(f"Seu depósito de R$ {deposit_amount:.2f} foi efetuado!")       