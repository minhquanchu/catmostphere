import json
from typing import List

from model.utils import getDBPath, now

def getMenu() -> dict:
    """
    Return the menu dictionary
    """
    path = getDBPath() + '\\order\\menu.json'
    try: 
        with open(path, 'r') as openFile:
            menu: dict = json.load(openFile)
        return menu
    except:
        raise Exception('failed to get menu, menu.json is missing')

def getInvoice(cashier: str, order: List[str], note: str = None, discount: int = 0) -> dict:
    """
    Return an invoice dictionary according to order(Side note: invoice is issued before the customer complete the purchase)
    Optional paramteter discount updates the total by subtracting the discount percentage (dicount takes value from 0: 0% -> 1: 100% ) 
    """
    path = getDBPath() + '\\order\\menu.json'
    try:
        with open(path, 'r') as openFile:
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
            Update quanity of order items (side note: if you set dict[key] = value, it just reassigns with the new value instead of updating it)
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

def updateLedger(receipt: dict) -> bool:
    """
    Add the receipt to ledger and update the revenue (side note: receipt is the same as invoice but after the completion of the order)
    Raise an expection if ledger.json is missing
    """
    path = getDBPath() + "\\order\\ledger.json"
    try:
        with open(path, 'r') as openFile:
            ledger = json.load(openFile)
        with open(path, 'w') as openFile:
            ledger['receipts'].append(receipt)
            ledger['balance']['revenue'] += receipt['total']
            json.dump(ledger, openFile, indent = 4, sort_keys = True)
    except:
        raise Exception('failed to update ledger, ledger.json is missing')
