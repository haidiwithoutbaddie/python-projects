
import calendar

select_year = int(input("ENTER YEAR: "))
select_month = int(input("ENTER MONTH: "))
if select_month < 1 or select_month > 12:
    print("value between 1-12")

print("\n", calendar.month(select_year,select_month))
