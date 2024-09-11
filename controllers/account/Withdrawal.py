from middleware.Date_time import compare_date, record_date_time


def withdrawal(acc_operations):
    if acc_operations["extract"]:
        limit_trans_today = compare_date(acc_operations)

        if limit_trans_today:
            return

    if acc_operations["balance"] == 0:
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
            date = record_date_time()
            acc_operations["balance"] -= withdrawal_amount
            acc_operations["extract"].append(
                {
                    "Saque": f"R$ {withdrawal_amount:.2f}",
                    "Data_transacao": date
                }
            )
            print(f"Saque de R$ {withdrawal_amount:.2f} realizado!")