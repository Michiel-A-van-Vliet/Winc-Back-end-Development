MicProductions SuperPy v1.0

* General *

This tool keeps track of a virtual 'current day', that affects input.

All product names must be in lower cases.

All dates must be in ISO format. Example: 1999-12-31


* Syntax *

usage: main.py [-h] [--today | --yesterday | --date DATE | --advance-time ADV_TIME] {buy,sell,report} ...

optional arguments:
  -h, --help            show this help message and exit
  --today, --now        Sets 'current day' to today
  --yesterday           Sets 'current day' to yesterday
  --date DATE           Sets 'current day' to specific ISO date (yyyy-mm-dd)
  --advance-time ADV_TIME
                        Advances a number of days. Negative numbers will make you travel back in time.

Commands:
  {buy,sell,report}
    buy                 Buy product
    sell                Sell product
    report              Make a report


usage: main.py buy [-h] --product-name PRODUCT_NAME --price PRICE --expiration-date EXPIRATION_DATE

optional arguments:
  -h, --help            show this help message and exit
  --product-name PRODUCT_NAME, -n PRODUCT_NAME
                        Name of bought product
  --price PRICE, -p PRICE
                        Price of bought product
  --expiration-date EXPIRATION_DATE, -x EXPIRATION_DATE
                        Product expiration date


usage: main.py sell [-h] --product-name PRODUCT_NAME --price PRICE

optional arguments:
  -h, --help            show this help message and exit
  --product-name PRODUCT_NAME, -n PRODUCT_NAME
                        Name of sold product
  --price PRICE, -p PRICE
                        Price of sold product


usage: main.py report [-h] [--start START] [--end END] [--csv] {inventory,revenue,profit,expenses,expired}

positional arguments:
  {inventory,revenue,profit,expenses,expired}
                        Type of report

optional arguments:
  -h, --help            show this help message and exit
  --start START, -s START
                        start date for report (default is 'current day')
  --end END, -e END     start date for report (default is 'current day')
  --csv                 Export report to CSV (reports 'inventory' and 'expired' only)


* Examples *

- Set 'current day' to today:
main.py --today

- Buy an orange:
main.py buy --product_name orange --price 0.1 --expiration_date 2020-12-31

- Sell a banana retroactively:
main.py --yesterday sell --product-name banana --price 1.2
Note: this changes the 'current day'

- Report on current day's revenue:
main.py report revenue

- Report profit of January 2020:
main.py report profit --start 2020-01-01 --end 2020-01-31

- Report expired products on specific date:
main.py --date 2020-02-20 report expired
Note: this changes the 'current day'.

- Report inventory and saves it to CSV file
main.py report inventory --csv
