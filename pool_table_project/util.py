import os
import json
import datetime


def clear_screen():
    # windows
    if os.name == "nt":
        os.system('cls')
    # mac/linux
    else:
        os.system('clear')


def display_table_statuses(pool_tables):
    divider = '=============================='
    centered_text = 'Pool Table Statuses'.center(len(divider) - 2)
    print(divider)
    print(f"={centered_text}=")
    print(divider)
    for pool_table in pool_tables:
        pool_table.display_status()
    print(divider)


def display_commands():
    print("\n1. Check-in to a pool table")
    print("2. Check-out of a pool table")
    print("3. Get detailed status on pool table")
    print("4. Get pool table log")
    print("5. Get log for all tables")
    print("Press 'q' to quit\n")


def display_error(message):
    print("\033[31;1m" + "ERROR: " + message + "\033[0m")
    input('Press any key to clear error. ')


def get_pool_table_number_input(message, upper_limit):
    table_number = int(
        input(f"{message} (1-{upper_limit}) "))
    if table_number - 1 not in range(upper_limit):
        raise IndexError

    return table_number - 1


def make_filename():
    if not os.path.isdir('./entries'):
        os.mkdir('./entries')
    today = datetime.date.today().strftime(f'%m-%d-%Y')
    return f"./entries/{today}.json"


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
    return "%b %d, %Y %I:%M %p"


def dict_entry_to_class_fields(entry):
    pool_table_number = entry["pool_table_number"]
    start_date_time = datetime.datetime.strptime(
        entry["start_date_time"], get_dt_format_string())
    end_date_time = datetime.datetime.strptime(
        entry["end_date_time"], get_dt_format_string())
    total_time_played = entry["total_time_played"]
    cost = entry["cost"]
    return (pool_table_number, start_date_time, end_date_time, total_time_played, cost)
