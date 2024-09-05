from datetime import date, datetime, time, timedelta

def deposit(acc_operation):
    if acc_operation["transactions_made"] >= acc_operation["TRANSACTIONS_LIMIT"]:
        print("Limite de operações diárias atingido!")
        return
    
    deposit_amount = int(input("Digite o valor que deseja depositar: R$"))
    if deposit_amount <= 0:
        print("Valor inválido!")

    else:
        acc_operation["balance"] += deposit_amount
        acc_operation["extract"].append(
            {
                "Deposito": f"R$ {deposit_amount:.2f}"
            }
        )
        acc_operation["transactions_made"] += 1
        print(f"Seu depósito de R$ {deposit_amount:.2f} foi efetuado!")
              