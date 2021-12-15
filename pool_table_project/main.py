from pool_table import PoolTable

pool_tables = []

for x in range(12):
    pool_tables.append(PoolTable(x+1))

pool_tables[5].check_in()

for pool_table in pool_tables:
    pool_table.display_status()
