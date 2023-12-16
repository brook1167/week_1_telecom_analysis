import unittest
import pandas as pd
import sys
sys.path.append("..")

top10_netflix_users = pd.read.csv('../data/top10_netflix.csv')
top10_user_session = pd.read.csv('../data/top10_user_session.csv')
user_overview = pd.read.csv('../data/user_overview_data.csv')

class DataTest(unittest.TestCase):
    expected_user_overview_column = [
    "Dur. (ms)",
    "MSISDN/Number",
    "Youtube_Total_Data",
    "Google_Total_Data",
    "Email_Total_Data",
    "Social_Media_Total_Data",
    "Netflix_Total_Data",
    "Gaming_Total_Data",
    "Other_Total_Data",
    "Total UL and DL"
    ]

    expected_top_users_session_column=[
        'MSISDN/Number',
        'Dur. (ms)'
    ]

    expected_top_netflix_users_column = [
        'MSISDN/Number','Netflix_Total_Data'
    ]

    def test_columns_equal_user_view(self):
        self.assertEqual(list(user_overview.columns), self.expected_user_overview_column)

    def test_columns_equal_top10_user_session(self):
        self.assertEqual(list(top10_user_session.columns), self.expected_top_users_session_column)

    def test_top10_netflix_users(self):
        self.assertEqual(list(top10_netflix_users .columns), self.expected_top_netflix_users_column)


if __name__ == '__main__':
    unittest.main()