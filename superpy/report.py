import csv
import datetime

from rich.console import Console
from rich.table import Table
from buy import get_bought
from sell import get_sold
from current_day import get_current_day

output_folder = "output/"


def get_path(report_name, day):
    now = datetime.datetime.now()
    unique_number = now.strftime("%Y%m%d%H%M%S%f")
    return f"{output_folder}{report_name}_{day}_{unique_number}"


def advanced_feedback(report_name, to_csv, day, data):
    if to_csv:
        path = get_path(report_name, day)
        full_path = path + ".csv"
        file = open(full_path, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["product_name", report_name.lower()])
        for item in data:
            writer.writerow([item, data[item]])
        file.close()
        print(f"Report saved as: {full_path}")
    else:
        print(f"{report_name} on {day}:")
        console = Console()
        table = Table(show_header=True)
        table.add_column("product name")
        table.add_column("number", justify="right")
        for item in data:
            table.add_row(item, str(data[item]))
        console.print(table)


def inventory(to_csv):
    current_day = get_current_day()
    sold = get_sold()
    bought = get_bought()

    sold_ids = []
    for product in sold:
        sell_date = product["sell_date"]
        if sell_date <= current_day:
            sold_ids.append(product["bought_id"])

    stock = {}
    for product in bought:
        product_name = product["product_name"]
        buy_date = product["buy_date"]
        product_id = product["id"]
        expiration_date = product["expiration_date"]

        if buy_date <= current_day and not product_id in sold_ids:
            if expiration_date > current_day:
                if product_name in stock:
                    new_count = stock[product_name] + 1
                    stock.update({product_name: new_count})
                else:
                    stock.update({product_name: 1})

    advanced_feedback("Inventory", to_csv, current_day.isoformat(), stock)


def expired(to_csv):
    current_day = get_current_day()
    sold = get_sold()
    bought = get_bought()

    sold_ids = []
    for product in sold:
        sell_date = product["sell_date"]
        if sell_date <= current_day:
            sold_ids.append(product["bought_id"])

    expired = {}
    for product in bought:
        product_name = product["product_name"]
        buy_date = product["buy_date"]
        product_id = product["id"]
        expiration_date = product["expiration_date"]

        if buy_date <= current_day and not product_id in sold_ids:
            if expiration_date <= current_day:
                if product_name in expired:
                    new_count = expired[product_name] + 1
                    expired.update({product_name: new_count})
                else:
                    expired.update({product_name: 1})

    advanced_feedback("Expired", to_csv, current_day, expired)


def get_income(start_date, end_date):
    sold = get_sold()
    income = 0
    for product in sold:
        if start_date <= product["sell_date"] <= end_date:
            income += product["sell_price"]
    return income


def get_outgo(start_date, end_date):
    bought = get_bought()
    outgo = 0
    for product in bought:
        if start_date <= product["buy_date"] <= end_date:
            outgo += product["buy_price"]
    return outgo


def revenue(start_date, end_date):
    income = get_income(start_date, end_date)
    if start_date == end_date:
        print(f"Revenue on {start_date}: {'%.2f' % income}")
    else:
        print(f"Revenue from {start_date} to {end_date}: {'%.2f' % income}")


def profit(start_date, end_date):
    income = get_income(start_date, end_date)
    outgo = get_outgo(start_date, end_date)
    if start_date == end_date:
        print(f"Profit on {start_date}: {'%.2f' % (income - outgo)}")
    else:
        print(f"Profit from {start_date} to {end_date}: {'%.2f' % (income - outgo)}")


def expenses(start_date, end_date):
    outgo = get_outgo(start_date, end_date)
    if start_date == end_date:
        print(f"Expenses on {start_date}: {'%.2f' % outgo}")
    else:
        print(f"Expenses from {start_date} to {end_date}: {'%.2f' % outgo}")


if __name__ == "__main__":
    # console = Console()
    # table = Table(show_header=True)
    # table.add_column("id", justify="right")
    # table.add_column("product_name")
    # table.add_row("1", "orange")
    # table.add_row("2", "potato")
    # console.print(table)
    #
    # path = file_name("test-inventory") + ".txt"
    # print(path)
    # with open(path, "w") as file:
    #     file.write("test")
    #     file.close()
    # print(f"Report saved as {path}")
    advanced_feedback("test-rapport", True, False, "2020-02-20", {"orange": 6, "banana": 2})
    pass
