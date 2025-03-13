import csv
import json
import pandas as pd
from datetime import datetime
import chardet

# Beolvassuk a categories.json fájlt
with open('categories.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# A fájl kódolásának automatikus felismerése
with open('transactions.csv', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# Beolvassuk a transactions.csv fájlt a felismert kódolással
transactions = []
with open('transactions.csv', 'r', encoding=encoding) as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        transactions.append(row)

# Kategorizáljuk a tranzakciókat
categorized_transactions = []
for transaction in transactions:
    partner_name = transaction['Partner név'].lower()
    amount = int(transaction['Összeg'].replace('\xa0', '').replace(' ', ''))
    date = datetime.strptime(transaction['Könyvelés dátuma'], '%Y.%m.%d')
    month_year = date.strftime('%Y.%m')
    
    category_found = False
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in partner_name:
                categorized_transactions.append({
                    'Hónap': month_year,
                    'Kategória': category,
                    'Összeg': amount
                })
                category_found = True
                break
        if category_found:
            break
    if not category_found:
        categorized_transactions.append({
            'Hónap': month_year,
            'Kategória': 'Egyéb',
            'Összeg': amount
        })

# DataFrame létrehozása a kategorizált tranzakciókból
df = pd.DataFrame(categorized_transactions)

# Összesítés hónap és kategória szerint
summary = df.groupby(['Hónap', 'Kategória'])['Összeg'].sum().unstack(fill_value=0)

# Összesen oszlop hozzáadása
summary['Összesen'] = summary.sum(axis=1)

# Excel fájlba mentés
summary.to_excel('kiadasok_osszesites.xlsx')

print("Az Excel táblázat sikeresen létrehozva: kiadasok_osszesites.xlsx")