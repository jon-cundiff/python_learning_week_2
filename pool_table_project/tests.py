import unittest
import os
from unittest.mock import patch
import datetime
from pool_table import PoolTable
from entry import Entry
import util


class PoolTableTests(unittest.TestCase):

    @patch.object(util, 'make_filename')
    def setUp(self, mock_make_filename):
        mock_make_filename.return_value = "test.json"
        self.pool_table = PoolTable(1)

    def test_pool_table_knows_if_occupied(self):
        self.assertEqual(False, self.pool_table.is_occupied(),
                         "Pool Table should return False")

        self.pool_table.start_date_time = datetime.datetime.now()
        self.assertEqual(True, self.pool_table.is_occupied(),
                         "Pool Table should return True")

    def test_pool_table_can_calculate_play_time_properly(self):
        self.pool_table.start_date_time = datetime.datetime(2021, 12, 1, 18, 0)
        end_date_time = datetime.datetime(2021, 12, 1, 18, 30)
        duration = self.pool_table.get_total_time_played_string(end_date_time)
        self.assertEqual("0:30", duration, "Should be 30 minutes")

        end_date_time = datetime.datetime(2021, 12, 1, 19, 30)
        duration = self.pool_table.get_total_time_played_string(end_date_time)
        self.assertEqual("1:30", duration, "Should be 1 hour 30 minutes")

    def test_pool_table_can_calculate_cost(self):
        play_time = 30

        cost = self.pool_table.get_total_cost(play_time)
        self.assertEqual(15.00, cost)

    def test_pool_table_can_be_checked_in(self):
        self.pool_table.check_in()
        self.assertNotEqual(None, self.pool_table.start_date_time,
                            "Pool table should have start date and time")

    def test_pool_table_should__not_check_in_if_occupied(self):
        self.pool_table.start_date_time = datetime.datetime(2021, 12, 1, 18, 0)
        self.pool_table.check_in()
        self.assertEqual(datetime.datetime(2021, 12, 1, 18, 0), self.pool_table.start_date_time,
                         "Pool table start date and time should not change")

    @patch.object(util, 'make_filename')
    def test_pool_table_can_be_checked_out(self, mock_make_filename):
        mock_make_filename.return_value = "test.json"
        self.pool_table.start_date_time = datetime.datetime(2021, 12, 1, 18, 0)
        self.pool_table.check_out()
        self.assertEqual(None, self.pool_table.start_date_time,
                         "Pool table start date and time to reset to None")
        self.assertEqual(1, len(self.pool_table.entries),
                         "Pool table entries list should increment by 1")

    def test_pool_table_cannot_be_checked_out_if_unoccupied(self):
        print('cannot be checked out')
        self.pool_table.check_out()
        self.assertEqual(0, len(self.pool_table.entries))

    def tearDown(self):
        if os.path.isfile('./test.json'):
            os.remove('./test.json')


unittest.main()
