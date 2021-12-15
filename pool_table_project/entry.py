class Entry:
    def __init__(self, pool_table_number, start_date_time, end_date_time, total_time_played, cost):
        self.pool_table_number = pool_table_number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.total_time_played = total_time_played
        self.cost = cost

    def export_as_dict(self):
        entry_dict = {
            "pool_table_number": self.pool_table_number,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "total_time_played": self.total_time_played,
            "cost": self.cost
        }

        return entry_dict
