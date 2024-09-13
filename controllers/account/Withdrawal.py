def withdrawal(acc_operations):
    
    if acc_operations["transactions_made"] >= acc_operations["TRANSACTIONS_LIMIT"]:
        print("\nLimite de operações diárias atingido!")
    
    elif acc_operations["balance"] == 0:
        print("\nVocê não possui saldo para sacar!")    
        
    else:
        withdrawal_amount = int(input("Digite o valor que deseja sacar: R$"))
        if withdrawal_amount <= 0:
            print("\nValor inválido!")

        elif withdrawal_amount > acc_operations["limit"]:
            print(
                f"\nO valor limite por saque é de R${acc_operations["limit"]:.2f}"
            )

        elif withdrawal_amount > acc_operations["balance"]:
            print("\nValor de saque superior ao saldo!")
            
        else:
            acc_operations["balance"] -= withdrawal_amount
            acc_operations["transactions_made"] += 1
            acc_operations["extract"] += f"Saque:\t\tR$ {withdrawal_amount:.2f}\n"

            print(f"\nSaque de R$ {withdrawal_amount:.2f} realizado!")