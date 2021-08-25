import csv
import datetime
from current_day import get_current_day
from buy import get_bought

sold_file = "data/sold.csv"


def get_sold():
    try:
        file = open(sold_file, newline="")
        reader = csv.reader(file)
        next(reader)
        sold = []
        for row in reader:
            sold_id = int(row[0])
            bought_id = int(row[1])
            sell_date = datetime.date.fromisoformat(row[2])
            sell_price = float(row[3])
            sold.append({"id": sold_id, "bought_id": bought_id, "sell_date": sell_date, "sell_price": sell_price})
        return sold
    except OSError:
        file = open(sold_file, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["id", "bought_id", "sell_date", "sell_price"])
        return []


def sell(product_name, sell_price):
    sold = get_sold()
    bought = get_bought()
    current_day = get_current_day()

    bought_id = 0
    bought_ids_of_sold_products = []
    for product in sold:
        bought_ids_of_sold_products.append(product["bought_id"])

    product_exists = False
    for product in bought:
        if product["product_name"] == product_name:
            product_exists = True
            if product["expiration_date"] >= current_day and product["id"] not in bought_ids_of_sold_products:
                bought_id = product["id"]
                break

    if bought_id > 0:
        sell_date = current_day.isoformat()
        sold_id = len(sold) + 1
        sold_product = {
            "id": sold_id,
            "bought_id": bought_id,
            "sell_date": sell_date,
            "sell_price": sell_price,
        }
        sold.append(sold_product)
        with open(sold_file, "a", newline="") as file:
            newline = [sold_id, bought_id, sell_date, sell_price]
            writer = csv.writer(file)
            writer.writerow(newline)
        print(f"Sold one {product_name} on {sell_date}.")
    else:
        if product_exists:
            print(f"Product '{product_name}' out of stock or expired")
        else:
            print(f"Product '{product_name}' does not exist")


if __name__ == "__main__":
    pass
