conversion_type = input('What types of currency would you like to convert to which?(USD-UAH, UAH-USD, UAH-EUR, EUR-UAH) ').upper()
currency = conversion_type.split('-')
amount = float(input(f'How much {currency[0]} do you have? '))

if conversion_type == 'USD-UAH':
    converted = amount * 38.7
elif conversion_type == 'UAH-USD':
    converted = amount / 38.7
elif conversion_type == 'UAH-EUR':
    converted = amount / 42.12
elif conversion_type == 'EUR-UAH':
    converted = amount * 42.12

print(f' With {amount} {currency[0]} you get {round(converted, 2)} {currency[-1]}')
