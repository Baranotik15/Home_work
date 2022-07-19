import random
import json

def RATE(curs):
    if curs:
        exchange_rate_naw = curs
        return exchange_rate_naw
    else:
        exchange_rate = data.get("exchange_rate")
        exchange_rate_naw = exchange_rate
        return exchange_rate_naw

def AVAILABLE():
    USD = data.get("USD")
    UAH = data.get("UAH")
    return f"USD = {USD}, UAH = {UAH}"

# def BUY_XXX():
#     a = 1
#     pass
#
# def SELL_XXX():
#     a = 1
#     pass

def BUY_ALL(curs):
    USD = data.get("USD")
    UAH = data.get("UAH")
    curs_in_function = float(curs)
    buy_all = UAH / curs_in_function
    buy_all_correct = float(round(buy_all, 2))
    UAH_2 = UAH - curs_in_function * buy_all_correct
    UAH = float(round(UAH_2, 2))
    USD_2 = USD + buy_all_correct
    USD = float(round(USD_2, 2))
    return f'сумма средств на USD счету: {USD};  сумма средств на UAH счету: {UAH}'

def SELL_ALL(curs):
    USD = 1011.15 # data.get("USD")
    UAH = data.get("UAH")
    curs_in_function = float(curs)
    sell_all = USD * curs_in_function
    sell_all_correct = float(round(sell_all, 2))
    UAH_2 = UAH + sell_all_correct
    UAH = float(round(UAH_2, 2))
    USD_2 = USD - (sell_all / curs_in_function)
    USD = float(round(USD_2, 2))
    return f'сумма средств на USD счету: {USD};  сумма средств на UAH счету: {UAH}'

def NEXT():
    exchange_rate = data.get("exchange_rate")
    delta = data.get("delta")
    max_curs = exchange_rate + delta
    min_curs = exchange_rate - delta
    curs = random.uniform(min_curs, max_curs)
    curs_2 = round(curs, 2)
    return curs_2


# def RESTART():

if __name__ == '__main__':

    with open('config.json', 'r') as fh:
        data = json.load(fh)

curs = NEXT()
print(curs)
b = RATE(curs=curs)
print(b)
c = AVAILABLE()
print(c)
v = BUY_ALL(curs=curs)
print(v)
q = SELL_ALL(curs=curs)
print(q)