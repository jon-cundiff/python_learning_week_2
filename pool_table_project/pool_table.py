import datetime
from entry import Entry


class PoolTable:
    def __init__(self, pool_table_number):
        self.pool_table_number = pool_table_number
        self.start_date_time = None
        self.hourly_rate = 30
        self.entries = []

    def is_occupied(self):
        return self.start_date_time is not None

    def get_total_time_played(self, end_date_time):
        time_delta = end_date_time - self.start_date_time
        total_seconds = time_delta.seconds

        # return in minutes without extra seconds
        return int(total_seconds / 60)

    def get_total_time_played_string(self, end_date_time):
        total_minutes = self.get_total_time_played(end_date_time)
        total_hours = int(total_minutes / 60)
        remaining_minutes = total_minutes % 60
        return f"{total_hours}:{remaining_minutes:02d}"

    def get_total_cost(self, play_time):
        return round(play_time / 60 * self.hourly_rate, 2)

    def create_entry(self, end_date_time):
        total_time_played = self.get_total_time_played(end_date_time)
        total_cost = self.get_total_cost(total_time_played)
        new_entry = Entry(self.pool_table_number,
                          self.start_date_time, end_date_time, total_time_played, total_cost)
        self.entries.append(new_entry)

    def check_in(self):
        if self.is_occupied():
            print(f"Pool Table {self.pool_table_number} is currently occupied")
        else:
            self.start_date_time = datetime.datetime.now()

    def check_out(self):
        if self.is_occupied():
            end_date_time = datetime.datetime.now()
            self.create_entry(end_date_time)
            self.start_date_time = None
        else:
            print(
                f"No one to check out at Pool Table {self.pool_table_number}")

    def display_status(self):
        message = f"Pool Table {self.pool_table_number} - "
        if self.is_occupied():
            start_time = self.start_date_time.strftime("%b %d %Y %H:%M:%S")
            duration = self.get_total_time_played_string(
                datetime.datetime.now())
            message += f"OCCUPIED since {start_time} - {duration}"
        else:
            message += "UNOCCUPIED"
        print(message)
