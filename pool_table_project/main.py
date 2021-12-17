from pool_table import PoolTable
import util

pool_tables = []

for x in range(12):
    pool_tables.append(PoolTable(x+1))

while True:
    util.clear_screen()
    util.display_table_statuses(pool_tables)
    util.display_commands()
    choice = input("Select a choice: ")
    print('')

    try:
        # check into table
        if choice == "1":
            table_number = util.get_pool_table_number_input(
                "Which table is getting checked in to?", len(pool_tables))
            pool_tables[table_number].check_in()
        # check out of table
        elif choice == "2":
            table_number = util.get_pool_table_number_input(
                "Which table is getting checked out of?", len(pool_tables))
            pool_tables[table_number].check_out()
        # detailed status of table
        elif choice == "3":
            table_number = util.get_pool_table_number_input(
                "Get details from which table?", len(pool_tables))
            pool_tables[table_number].display_details()

        # entry log of table
        elif choice == "4":
            table_number = util.get_pool_table_number_input(
                "Get details from which table?", len(pool_tables))
            pool_tables[table_number].display_entries()

        # entry log of all tables
        elif choice == "5":
            cost = 0.00
            for pool_table in pool_tables:
                pool_table.display_entries(True)
                table_cost = pool_table.get_entries_cost()
                cost += table_cost
                divider = "***************************"
                inner_text = f"Table {pool_table.pool_table_number} Total: ${table_cost:.2f}".center(
                    len(divider) - 2)
                print(divider)
                print(
                    f"\n{inner_text}\n")
                print(divider + "\n\n")

            print("===========================")
            print(f"Total Cost: ${cost:.2f}\n")
            input('Press any key to continue...')

        elif choice.lower() == 'q':
            break

        else:
            raise IndexError

    except IndexError:
        util.display_error("Invalid Option")

    except ValueError:
        util.display_error("A number must be entered")
