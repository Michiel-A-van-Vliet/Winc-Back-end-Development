import csv
import datetime
from current_day import get_current_day

bought_file = "data/bought.csv"


def get_bought():
    try:
        file = open(bought_file, newline="")
        reader = csv.reader(file)
        next(reader)
        bought = []
        for row in reader:
            bought_id = int(row[0])
            product_name = row[1]
            buy_date = datetime.date.fromisoformat(row[2])
            buy_price = float(row[3])
            expiration_date = datetime.date.fromisoformat(row[4])
            bought.append({"id": bought_id, "product_name": product_name, "buy_date": buy_date, "buy_price": buy_price,
                           "expiration_date": expiration_date})
        return bought
    except OSError:
        file = open(bought_file, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["id", "product_name", "buy_date", "buy_price", "expiration_date"])
        return []


def buy(product_name, buy_price, expiration_date):
    buy_date = get_current_day().isoformat()
    bought = get_bought()
    bought_id = len(bought) + 1
    new_product = {
        "id": bought_id,
        "product_name": product_name,
        "buy_date": buy_date,
        "buy_price": buy_price,
        "expiration_date": expiration_date,
    }
    bought.append(new_product)
    with open(bought_file, "a", newline="") as file:
        newline = [bought_id, product_name, buy_date, buy_price, expiration_date]
        writer = csv.writer(file)
        writer.writerow(newline)
    print(f"Bought one {product_name} on {buy_date}.")
