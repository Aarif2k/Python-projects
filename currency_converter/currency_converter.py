from forex_python.converter import CurrencyRates, RatesNotAvailableError

try:
    c = CurrencyRates()
    amount = int(input("Enter the amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()
    print(from_currency, " To ", to_currency, amount)
    result = c.convert(from_currency, to_currency, amount)
    print(result)
except RatesNotAvailableError:
    print("Currency rates are not available at the moment. Please try again later.")
