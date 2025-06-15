import argparse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import math

def simple_ymd_string(rd):
    result = []
    if rd.years:
        result.append(f"{rd.years} years")
    if rd.months:
        result.append(f"{rd.months} months")
    if rd.days:
        result.append(f"{rd.days} days")
    return ', '.join(result) if result else "0 days"

parser = argparse.ArgumentParser()
parser.add_argument("--days", help = "Enter the number of days you want.", type = int)
parser.add_argument("--from-date", help = "Enter the date you want (YYYY-MM-DD).", type = str)
parser.add_argument("--to-date", help = "Enter the date you want (YYYY-MM-DD).", type = str)
args = parser.parse_args()
date = ''
if args.days:
    date = datetime.now() + timedelta(days=args.days)
    if args.days > 0:
        print(f"{args.days} days from today the date will be {date.date()}.")
        pass
    elif args.days < 0:
        print(f"Before {abs(args.days)} days the date was {date.date()}.")
        pass
else:
    if args.from_date:
        date = datetime.strptime(args.from_date, "%Y-%m-%d")
        difference = simple_ymd_string(relativedelta(datetime.today().date(),date))
        print(f"The date {date.date()} was {difference} from {datetime.today().date()}")

    elif args.to_date:
        date = datetime.strptime(args.to_date, "%Y-%m-%d")
        difference = simple_ymd_string(relativedelta(date, datetime.today().date()))
        print(f"The date {date.date()} is {difference} from {datetime.today().date()}")
