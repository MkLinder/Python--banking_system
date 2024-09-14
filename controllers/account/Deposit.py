from middleware.Date_time import compare_date, record_date_time


def deposit(acc_operations, /):
    if acc_operations["extract"]:
        trans_limit_today = compare_date(acc_operations)

        if trans_limit_today:
            return

        
    deposit_amount = int(input("Digite o valor que deseja depositar: R$"))
    if deposit_amount <= 0:
        print("\nValor inválido!")

    else:
        date = record_date_time()
        acc_operations["balance"] += deposit_amount
        acc_operations["extract"].append(
            {
                "Deposito": f"R$ {deposit_amount:.2f}", "Data_trans.": date
            }
        )

        print(f"\nSeu depósito de R$ {deposit_amount:.2f} foi efetuado!")              