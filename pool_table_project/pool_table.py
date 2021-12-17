import datetime
import util
from entry import Entry


class PoolTable:
    def __init__(self, pool_table_number):
        self.pool_table_number = pool_table_number
        self.start_date_time = None
        self.hourly_rate = 30
        self.entries = []

        # import entries from same day if app is restarted and convert into Entry instances
        raw_entries = util.get_entries(pool_table_number)
        for raw_entry in raw_entries:
            (pool_table_number, start_date_time, end_date_time,
             total_time_played, cost) = util.dict_entry_to_class_fields(raw_entry)
            entry = Entry(pool_table_number, start_date_time,
                          end_date_time, total_time_played, cost)
            self.entries.append(entry)

    def is_occupied(self):
        return self.start_date_time is not None

    def get_total_time_played(self, end_date_time):
        time_delta = end_date_time - self.start_date_time
        total_seconds = time_delta.seconds

        # return in minutes without extra seconds
        return int(total_seconds / 60)

    def get_total_time_played_string(self, end_date_time=None, play_time=None):
        total_minutes = 0
        if play_time:
            total_minutes = play_time
        elif end_date_time:
            total_minutes = self.get_total_time_played(end_date_time)
        hours = {
            "num": int(total_minutes / 60),
            "label": "hours"
        }

        minutes = {
            "num": total_minutes % 60,
            "label": "minutes"
        }

        # converts hours to hour and/or minutes to minute if 1
        for unit in [hours, minutes]:
            if unit["num"] == 1:
                unit["label"] = unit["label"][0:-1]
        message = ""
        if hours["num"] > 0:
            message += f"{hours['num']} {hours['label']} "
        return message + f"{minutes['num']} {minutes['label']}"

    def get_total_cost(self, play_time):
        return round(play_time / 60 * self.hourly_rate, 2)

    def create_entry(self, end_date_time):
        total_time_played = self.get_total_time_played(end_date_time)
        total_cost = self.get_total_cost(total_time_played)
        new_entry = Entry(self.pool_table_number,
                          self.start_date_time, end_date_time, total_time_played, total_cost)
        self.entries.append(new_entry)

        dict_entries = []
        for entry in self.entries:
            dict_entries.append(entry.export_as_dict())

        util.update_entries(self.pool_table_number, dict_entries)

    def check_in(self):
        if self.is_occupied():
            util.display_error(
                f"Pool Table {self.pool_table_number} is currently occupied")
        else:
            self.start_date_time = datetime.datetime.now()

    def check_out(self):
        if self.is_occupied():
            end_date_time = datetime.datetime.now()
            self.create_entry(end_date_time)
            self.start_date_time = None
        else:
            util.display_error(
                f"No one to check out at Pool Table {self.pool_table_number}")

    def display_status(self):
        number_string = str(self.pool_table_number).rjust(2)
        message = f"  Pool Table {number_string} - "
        if self.is_occupied():
            start_time = self.start_date_time.strftime(
                util.get_dt_format_string())
            duration = self.get_total_time_played_string(
                datetime.datetime.now())
            message += f"OCCUPIED since {start_time} - {duration}"
        else:
            message += "UNOCCUPIED"
        print(message)

    def display_header(self, inner_text, divider):
        print(divider)
        print(f"+{inner_text.center(len(divider) - 2)}+")
        print(divider + "\n")

    def display_details(self):
        divider = "++++++++++++++++++++++++++++++++++++++++"
        inner_text = f"Pool Table {self.pool_table_number}"
        self.display_header(inner_text, divider)

        if self.is_occupied():
            start_time = self.start_date_time.strftime(
                util.get_dt_format_string())
            now = datetime.datetime.now()
            duration = self.get_total_time_played_string(now)
            cost = self.get_total_cost(self.get_total_time_played(now))
            print(f"  OCCUPIED since {start_time}")
            print(f"  Duration: {duration}")
            print(f"  Current Cost: ${cost}")
        else:
            print("Currently UNOCCUPIED")

        print("\n" + divider + '\n')
        input('Press any key to continue...')

    def display_entries(self, skip_confirm):
        divider = "++++++++++++++++++++++++++++++++++++++++"
        today = datetime.date.today().strftime(f'%m-%d-%Y')
        inner_text = f"Pool Table {self.pool_table_number} Log: {today}"
        self.display_header(inner_text, divider)

        date_format = util.get_dt_format_string()
        if len(self.entries) > 0:
            for entry in self.entries:
                play_time = self.get_total_time_played_string(
                    play_time=entry.total_time_played)
                print(f"  Pool Table: {entry.pool_table_number}")
                print(
                    f"  Start Time: {entry.start_date_time.strftime(date_format)}")
                print(
                    f"  End Time: {entry.end_date_time.strftime(date_format)}")
                print(f"  Play Time: {play_time}")
                print(f"  Cost: ${entry.cost:.2f}\n")
                print(divider + '\n')
        else:
            print("  No entries\n")
        if skip_confirm:
            return

        input('Press any key to continue...')

    def get_entries_cost(self):
        cost = 0.00
        for entry in self.entries:
            cost += entry.cost
        return cost
