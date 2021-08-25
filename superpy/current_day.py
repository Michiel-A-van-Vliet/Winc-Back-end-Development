import datetime

date_file = "data/current_day.cfg"


def write_date(iso_date):
    file = open(date_file, "w")
    file.write(iso_date)
    file.close()
    print("Date set to:", iso_date)


def get_current_day():
    try:
        return datetime.date.fromisoformat(open(date_file, "r").read())
    except OSError:
        new_date = datetime.date.today()
        write_date(str(new_date))
        return new_date


def today():
    new_day = str(datetime.date.today())
    write_date(new_day)
    return new_day


def yesterday():
    new_day = str(datetime.date.today() - datetime.timedelta(days=1))
    write_date(new_day)
    return new_day


def set_date(iso_date):
    write_date(iso_date)
    return iso_date


def change_date(days):
    new_day = str(get_current_day() + datetime.timedelta(days=days))
    write_date(new_day)
    return new_day
