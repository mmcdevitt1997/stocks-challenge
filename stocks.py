stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak",
    "AAPL": "Apple Inc",
    "NKE": "Nike Inc",
    "AMD": "Advanced Micro Devises"
}

purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GM', 200, '1-jul-1998', 56),
    ('AAPL', 100, '5-jul-2017', 200),
    ('AMD', 200, '5-march-2018', 30),
    ('AMD', 200, '3-jul-2019', 82)
]

total_stock = 0
amount_of_stock = 0

for (compaine_name, number_of_stock, date_of_purchase, price_of_stock) in purchases:
    amount_of_stock = number_of_stock*price_of_stock

    total_stock += amount_of_stock

    print(f"I purchased {stockDict[compaine_name]} stock for ${amount_of_stock}")

print (f" Total stock value ${total_stock}")

for (compaine_name, number_of_stock, date_of_purchase, price_of_stock) in purchases:
    print(f"--{compaine_name}--")








