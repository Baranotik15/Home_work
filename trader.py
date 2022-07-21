import random
import json


def read(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def write(file_name, x):
    with open(file_name, "w") as file:
        data_write = json.dump(x,file)

def tofixe(x):
    x = int(x * 100) / 100
    return x

def rate(data):
    rate_new = data.get("exchange_rate")
    print(rate_new)

def availible(data):
    usd = data.get("USD")
    uah = data.get("UAH")
    print(f'USD: {usd}; UAH: {uah}')

def buy_xxx(x, data):
    curs = data.get("exchange_rate")
    usd = data.get("USD")
    uah = data.get("UAH")
    availible_uah = x * curs
    if uah > availible_uah:
        uah = uah - availible_uah
        usd = usd + x
        data["USD"] = usd
        data["UAH"] = uah
        write("data.json", data)
        print( f'USD: {usd}; UAH: {uah}')
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {availible_uah}, AVAILABLE {uah}")


def sell_xxx(x, data):
    curs = data.get("exchange_rate")
    usd = data.get("USD")
    uah = data.get("UAH")
    availible_uah = x * curs
    if usd > x:
        uah = uah + availible_uah
        usd = usd - x
        data["USD"] = usd
        data["UAH"] = uah
        write("data.json", config)
        print(f'USD: {usd}; UAH: {uah}')
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {x}, AVAILABLE {usd}")

def buy_all(data):
    usd = data.get("USD")
    uah = data.get("UAH")
    curs = data.get("exchange_rate")
    curs_in_function = float(curs)
    buy_all = uah / curs_in_function
    buy_all_correct = tofixe(buy_all)
    uah_2 = uah - curs_in_function * buy_all_correct
    uah = tofixe(uah_2)
    usd_2 = usd + buy_all_correct
    usd = tofixe(usd_2)
    data["USD"] = usd
    data["UAH"] = uah
    write("data.json", data)
    print(f'USD: {usd}; UAH: {uah}')

def sell_all(data):
    usd = data.get("USD")
    uah = data.get("UAH")
    curs = data.get("exchange_rate")
    curs_in_function = float(curs)
    sell_all = usd * curs_in_function
    sell_all_correct = tofixe(sell_all)
    uah_2 = uah + sell_all_correct
    uah = tofixe(uah_2)
    usd_2 = usd - (sell_all / curs_in_function)
    usd = tofixe(usd_2)
    data["USD"] = usd
    data["UAH"] = uah
    write("data.json", data)
    print(f'USD: {usd}; UAH: {uah}')

def next(config, data):
    exchange_rate = config.get("exchange_rate")
    delta = config.get("delta")
    uah = data.get("UAH")
    usd = data.get("USD")
    max_curs = exchange_rate + delta
    min_curs = exchange_rate - delta
    curs = random.uniform(min_curs, max_curs)
    exchange_rate = round(curs, 2)
    config["exchange_rate"] = exchange_rate
    config["UAH"] = uah
    config["USD"] = usd
    write("data.json", config)



def restart(config):
    write("data.json", config)

if __name__ == '__main__':
    config = read("config.json")
    writr("data.json", config)
    data = read("data.json")

    availible(data)
    next(config, data)
    rate(data)
    buy_all(data)
    sell_all(data)
    buy_xxx(10, data)
    sell_xxx(11, data)
    restart(config)

