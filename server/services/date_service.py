
import datetime


class DateService:

    @classmethod
    def get_next_month_beginning(cls):
        # Step 1: Get the current date
        today = datetime.date.today()
        if today.month == 12:
            # If it's December, next month is January of the next year
            next_month = 1
            next_month_year = today.year + 1
        else:
            next_month = today.month + 1
            next_month_year = today.year

        # Step 3: Create the first day of the next month at 00:00:00
        return datetime.datetime(
            next_month_year, next_month, 1, 0, 0, 0)
