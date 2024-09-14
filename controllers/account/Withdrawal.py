from middleware.Date_time import compare_date, record_date_time


def withdrawal(acc_operations):
    if acc_operations["extract"]:
        trans_limit_today = compare_date(acc_operations)

        if trans_limit_today:
            return

    if acc_operations["balance"] == 0:
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
            date = record_date_time()
            acc_operations["balance"] -= withdrawal_amount
            acc_operations["extract"].append(
                {
                    "Saque": f"\tR${withdrawal_amount:.2f}", "Data_trans.": date
                }
            )
            print(f"\nSaque de R$ {withdrawal_amount:.2f} realizado!")