from controllers.menu.Home_menu import home_menu

from datetime import date, datetime, time, timedelta

now = datetime.now().strftime("%d/%m/%Y %H:%M")
date_now = date.today()

registered_date_time = datetime.strptime(now, "%d/%m/%Y %H:%M").date()
print(registered_date_time)

print(registered_date_time == date_now)

home_menu()