import datetime


def get_datetime_utc():
    now = datetime.datetime.utcnow()
    # Format the date and time to the desired format
    formatted_date = now.isoformat(timespec='milliseconds') + 'Z'
    return formatted_date


def get_tomorrow_date_utc():
    today_utc = datetime.datetime.utcnow()
    tomorrow_utc = today_utc + datetime.timedelta(days=1)
    tomorrow_utc_str = tomorrow_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return tomorrow_utc_str

