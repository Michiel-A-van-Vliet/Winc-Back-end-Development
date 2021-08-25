# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'
# Your code below this line.

import argparse
import report
import current_day
import datetime
from buy import buy
from sell import sell


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", title="Commands")

    date_parser = parser.add_mutually_exclusive_group()
    date_parser.add_argument("--today", "--now", action="store_true", help="Sets 'current day' to today")
    date_parser.add_argument("--yesterday", action="store_true", help="Sets 'current day' to yesterday")
    date_parser.add_argument("--date", dest="date", type=iso_date,
                             help="Sets 'current day' to specific ISO date (yyyy-mm-dd)")
    date_parser.add_argument("--advance-time", type=int, dest="adv_time",
                             help="Advances a number of days. Negative numbers will make you travel back in time.")

    buy_parser = subparsers.add_parser("buy", help="Buy product")
    buy_parser.add_argument("--product-name", "-n", required=True, type=str.lower, help="Name of bought product")
    buy_parser.add_argument("--price", "-p", required=True, type=float, help="Price of bought product")
    buy_parser.add_argument("--expiration-date", "-x", required=True, type=iso_date,
                            help="Product expiration date")

    sell_parser = subparsers.add_parser("sell", help="Sell product")
    sell_parser.add_argument("--product-name", "-n", required=True, type=str.lower, help="Name of sold product")
    sell_parser.add_argument("--price", "-p", required=True, type=float, help="Price of sold product")

    report_parser = subparsers.add_parser("report", help="Make a report")
    report_parser.add_argument("report_type", choices=("inventory", "revenue", "profit", "expenses", "expired"),
                               help="Type of report")
    report_parser.add_argument("--start", "-s", required=False, type=iso_date,
                               help="start date for report (default is 'current day')")
    report_parser.add_argument("--end", "-e", required=False, type=iso_date,
                               help="start date for report (default is 'current day')")
    report_parser.add_argument("--csv", action="store_true", default=False,
                               help="Export report to CSV (reports 'inventory' and 'expired' only)")

    args = parser.parse_args()

    if not args.command:
        print("MicProductions SuperPy v1.0")

    if args.today:
        current_day.today()
    elif args.yesterday:
        current_day.yesterday()
    elif args.date:
        current_day.set_date(args.date)
    elif args.adv_time:
        current_day.change_date(args.adv_time)

    if args.command == "report":
        if args.start:
            start_date = datetime.date.fromisoformat(args.start)
        else:
            start_date = current_day.get_current_day()
        if args.end:
            end_date = datetime.date.fromisoformat(args.end)
        else:
            end_date = current_day.get_current_day()

        if args.report_type == "inventory":
            report.inventory(args.csv)
        elif args.report_type == "revenue":
            report.revenue(start_date, end_date)
        elif args.report_type == "profit":
            report.profit(start_date, end_date)
        elif args.report_type == "expenses":
            report.expenses(start_date, end_date)
        elif args.report_type == "expired":
            report.expired(args.csv)

    elif args.command == "buy":
        buy(args.product_name, args.price, args.expiration_date)
    elif args.command == "sell":
        sell(args.product_name, args.price)


def iso_date(date: str) -> str:
    try:
        datetime.date.fromisoformat(date)
        return date
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected ISO date, got '{date}' instead.")


if __name__ == "__main__":
    main()
