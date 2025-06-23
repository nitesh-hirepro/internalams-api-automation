import datetime
import random
import string


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


def generate_today_and_year_later_date():
    today = datetime.datetime.today()
    one_year_later = today + datetime.timedelta(days=365)
    today_formatted = today.strftime("%Y-%m-%d")
    one_year_later_formatted = one_year_later.strftime("%Y-%m-%d")
    return today_formatted, one_year_later_formatted


def generate_dummy_email():
    # Define possible characters for the local part of the email
    characters = string.ascii_lowercase + string.digits

    # Randomly select the length of the local part
    local_part_length = random.randint(6, 12)

    # Generate the local part of the email
    local_part = ''.join(random.choice(characters) for _ in range(local_part_length))

    domain = 'gmail.com'

    # Combine local part and domain to create the email
    email = f"{local_part}@{domain}"

    return email

def get_value_or_empty(dictionary, key):
    """
        Returns the value of the key if it exists in the dictionary,
        otherwise returns an empty string.

        :param dictionary: dict, the dictionary to check
        :param key: the key to look for
        :return: value associated with the key, or empty string if key is not found
    """
    return dictionary.get(key, "")