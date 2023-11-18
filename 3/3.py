import datetime
import calendar

year = int(input("Enter the year: "))

for month in range(1, 13):
    if month < 12:
        last_day = datetime.date(year, month+1, 1) - datetime.timedelta(days=1)
    else:
        last_day = datetime.date(year+1, 1, 1) - datetime.timedelta(days=1)

    if last_day.weekday() == calendar.SATURDAY:
        last_day -= datetime.timedelta(days=1)
    elif last_day.weekday() == calendar.SUNDAY:
        last_day -= datetime.timedelta(days=2)

    formatted_date = last_day.strftime("%d.%m.%Y")
    print(calendar.month_name[month], formatted_date)
