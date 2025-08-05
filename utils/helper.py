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

def compare_experience(expected, extracted):
    """
    Compare expected and extracted experience values (as years, can be float or string like '6.8').
    Returns True if extracted is within [expected-1, expected+1], else False.
    """
    try:
        expected_val = float(expected)
        extracted_val = float(extracted)
    except (ValueError, TypeError):
        return False
    return (expected_val - 1) <= extracted_val <= (expected_val + 1)

def convert_date_format(date_str: str) -> str:
    """
    Args:
        date_str (str): Input date string in the format 'YYYY-MM-DDTHH:MM:SSZ'.

    Returns:
        str: Date string in 'DD/MM/YYYY' format.
    """
    try:
        # Parse the input ISO format date
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        # Format it to desired output
        return dt.strftime("%d/%m/%Y")
    except ValueError as e:
        return f"Invalid date format: {e}"

def transform_education_data(input_list):
    """
    Args:
        input_list (list): List of dictionaries containing education data.

    Returns:
        list: Transformed list of dictionaries with required keys.
    """
    output_list = []
    for item in input_list:
        transformed = {
            "college": item.get("InstituteMappedText", ""),
            "degree": item.get("DegreeMappedText", ""),
            "branch": item.get("BranchMappedText", ""),
            "yop": item.get("EndYearMappedText", ""),
            "cgpa/%": item.get("Percentage", ""),
            "isFinal": item.get("IsFinal", 0)
        }
        output_list.append(transformed)
    return output_list


def transform_work_experience(input_list):
    """
    Args:
        input_list (list): List of dictionaries with work experience data.

    Returns:
        list: Transformed list of dictionaries.
    """
    output_list = []
    for item in input_list:
        transformed = {
            "company": item.get("CompanyMappedText") or item.get("EmployerText", ""),
            "designation": item.get("DesignationMappedText", ""),
            "fromMonth": item.get("FromMonth", ""),
            "fromYear": item.get("FromYearText", ""),
            "toMonth": item.get("ToMonth", ""),
            "toYear": item.get("ToYearText", ""),
            "IsLatest": item.get("IsLatest", 0)
        }
        output_list.append(transformed)
    return output_list