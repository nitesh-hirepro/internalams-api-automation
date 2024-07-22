import datetime


def get_datetime_utc():
    now = datetime.datetime.utcnow()

    # Format the date and time to the desired format
    formatted_date = now.isoformat(timespec='milliseconds') + 'Z'

    return formatted_date

