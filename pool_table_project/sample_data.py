from pool_table import PoolTable
import datetime
import random

datetime_start = datetime.datetime.now()
pool_tables = []


def generate_random_entries(pool_table):
    for x in range(random.randint(0, 7)):
        minutes = random.randint(15, 90)
        end_date = datetime_start + datetime.timedelta(minutes=minutes)
        pool_table.create_entry(end_date)


for x in range(12):
    pool_tables.append(PoolTable(x+1))
    pool_tables[x].start_date_time = datetime_start
    generate_random_entries(pool_tables[x])
