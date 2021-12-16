import os
import json
import datetime


def make_filename():
    if not os.path.isdir('./entries'):
        os.mkdir('./entries')
    today = datetime.date.today()
    return f"./entries/{today.month}-{today.day}-{today.year}.json"


def get_all_entries():
    filename = make_filename()
    if os.path.isfile(filename):
        with open(filename) as file:
            return json.load(file)
    else:
        return {}


def get_entries(pool_table_number):
    entries = get_all_entries()
    try:
        return entries[str(pool_table_number)]
    except KeyError:
        return []


def update_entries(pool_table_number, table_entries):
    entries = get_all_entries()
    entries[str(pool_table_number)] = table_entries

    filename = make_filename()
    with open(filename, "w") as file:
        json.dump(entries, file, indent=4)


def get_dt_format_string():
    return "%b %d, %Y %H:%M:%S"


def dict_entry_to_class_fields(entry):
    pool_table_number = entry["pool_table_number"]
    start_date_time = datetime.datetime.strptime(
        entry["start_date_time"], get_dt_format_string())
    end_date_time = datetime.datetime.strptime(
        entry["end_date_time"], get_dt_format_string())
    total_time_played = entry["total_time_played"]
    cost = entry["cost"]
    return (pool_table_number, start_date_time, end_date_time, total_time_played, cost)
