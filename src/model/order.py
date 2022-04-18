import json
from typing import List

from model.utils import now

def getMenu() -> dict:
    pass

def getInvoice(dir: str, cashier: str, order: List[str], note: str = None,discount: int = 0) -> dict:
    try:
        with open(f'{dir}/menu.json', 'r') as openFile:
            menu: dict = json.load(openFile)
        invoice = {
            'time': now(),
            'items': dict(),
            'note': note,
            'total': 0,
            'cashier': cashier
        }
        for item in order:
            invoice['total'] += (1 - discount)*menu[item]['price']
            """
            Update quanity of order items
            if an item is not in the receipt yet set quantity to 1
            else increment quantity by 1
            """
            if item in invoice['items'].keys():
                print(invoice['items'].keys())
                invoice['items'][item] = menu[item]
                invoice['items'][item]['quantity'] += 1
            else: 
                invoice['items'][item] = menu[item]
                invoice['items'][item]['quantity'] = 1        
        return invoice
    except:
        raise Exception('failed to get invoice, menu.json is missing')

def updateLedger(dir: str, receipt: dict) -> bool:
    try:
        with open(f'{dir}/ledger.json', 'r') as openFile:
            ledger = json.load(openFile)
        with open(f'{dir}/ledger.json', 'w') as openFile:
            ledger['receipts'].append(receipt)
            ledger['balance']['revenue'] += receipt['total']
            json.dump(ledger, openFile, indent = 4, sort_keys = True)
    except:
        raise Exception('failed to update ledger, ledger.json is missing')
