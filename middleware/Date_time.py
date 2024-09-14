from datetime import date, datetime


def record_date_time():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    return now

def compare_date(acc_operations):
    date_today = date.today().strftime("%d/%m/%Y")
    transactions_today = []

    for i in acc_operations["extract"]:
        if i.get("Data_trans.")[:10] == date_today:
            transactions_today.append(i.get("Data_trans.")[:10])

    if len(transactions_today) >= acc_operations["TRANSACTIONS_LIMIT"]:
        print("\nLimite de operações diárias atingido!")
        return transactions_today
    
    else:
        return