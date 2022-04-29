from pandas import DataFrame
import pandas as pd
from dashboad import dataframe


class dataset:
    def __init__(self) -> None:
        self.data= dataframe
        #Add a total amount to every transaction
        self.add_sales()
        #Add a month column
        self.add_month()

    def most_retweets(self):
        more_retweets= self.data.groupby('retweet_count').sum()
        return more_retweets