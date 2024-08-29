import json

from database.default_inf import default

def extract():
    print("\n============ EXTRATO ============")
    print(
        "Não foram realizadas movimentações." if not default["extract"] else json.dumps(default["extract"], indent=4)
    )
    print(f"\nSaldo: R$ {default["balance"]:.2f}")
    print("=================================")