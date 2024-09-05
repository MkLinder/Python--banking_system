def withdrawal(acc_operations):
    
    if acc_operations["transactions_made"] >= acc_operations["TRANSACTIONS_LIMIT"]:
        print("Limite de operações diárias atingido!")
    
    elif acc_operations["balance"] == 0:
        print("Você não possui saldo para sacar!")    
        
    else:
        withdrawal_amount = int(input("Digite o valor que deseja sacar: R$"))
        if withdrawal_amount <= 0:
            print("Valor inválido!")

        elif withdrawal_amount > acc_operations["limit"]:
            print(
                f"O valor limite por saque é de R${acc_operations["limit"]:.2f}"
            )

        elif withdrawal_amount > acc_operations["balance"]:
            print("Valor de saque superior ao saldo!")
            
        else:
            acc_operations["balance"] -= withdrawal_amount
            acc_operations["transactions_made"] += 1
            acc_operations["extract"].append(f"Saque: R$ {withdrawal_amount:.2f}")
            
            print(f"Saque de R$ {withdrawal_amount:.2f} realizado!")