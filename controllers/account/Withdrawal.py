from database.default_inf import default

def withdrawal(withdrawal_amount):
    default["balance"] -= withdrawal_amount
    default["withdrawals_made"] += 1
    default["extract"].append(f"Saque: R$ {withdrawal_amount:.2f}")
    print(f"Saque de R$ {withdrawal_amount:.2f} realizado!")