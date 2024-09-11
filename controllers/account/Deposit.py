from middleware.Date_time import compare_date, record_date_time


def deposit(acc_operations, /):
    if acc_operations["extract"]:
        limit_trans_today = compare_date(acc_operations)

        if limit_trans_today:
            return
        
    deposit_amount = int(input("Digite o valor que deseja depositar: R$"))
    if deposit_amount <= 0:
        print("Valor inválido!")

    else:
        date = record_date_time()
        acc_operations["balance"] += deposit_amount
        acc_operations["extract"].append(
            {
                "Deposito": f"R$ {deposit_amount:.2f}",
                "Data_transacao": date
            }
        )
        print(f"Seu depósito de R$ {deposit_amount:.2f} foi efetuado!")
              