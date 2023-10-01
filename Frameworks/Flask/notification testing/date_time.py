from datetime import datetime, timedelta
import time

# Get the current date and time
current_datetime = datetime.today()
date_today=(current_datetime.date())
new_date=current_datetime.date()+timedelta(5)


if new_date<date_today:
	print("passed day")
elif new_date>date_today:
	print("Future")





