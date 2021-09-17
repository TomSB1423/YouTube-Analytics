import os
import pandas as pd
import matplotlib.pyplot as plt


class YoutubeAnalytics:
    def __init__(self, path_name, df=None):
        self.path_name = path_name
        self.df = df

    def open_df(self):
        try:
            self.df = pd.read_json(f"{self.path_name}")
            return True
        except:
            return False

    def get_data(self):
        if not self.df:
            self.open_df()
        # for col in self.df:
        #     print(col)
        print(self.df["time"])
        self.df["time"] = self.df["time"].astype("datetime64")
        self.df[["title"]].groupby(
            [self.df["time"].dt.year, self.df["time"].dt.month]
        ).count().plot(kind="bar")
        plt.show()


path_name = os.environ.get("DF_PATH")
service = YoutubeAnalytics(path_name)
service.get_data()
