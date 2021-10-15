
import datetime

def validate_datetime(date_text):
    try:
        date = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")