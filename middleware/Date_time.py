from datetime import date, datetime


def record_date_time():
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    return now

def compare_date(acc_operations):
    date_today = date.today().strftime("%d/%m/%Y")
    
    transactions_today = [t for t in acc_operations["extract"] if t["Data_transacao"][:10] == date_today]
        
    if len(transactions_today) >= acc_operations["TRANSACTIONS_LIMIT"]:
        print("Limite de operações diárias atingido!")
        return transactions_today