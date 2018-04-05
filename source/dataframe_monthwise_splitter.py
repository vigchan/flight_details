import pandas as pd

class DataframeMonthwiseSplitter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_frame = pd.read_csv(self.file_name, low_memory=False)
        print("The file name is: {}".format(self.file_name))

        print('DataFrame Dimensions:', self.data_frame.shape)

    def split_by_month(self, attribute, month, file_name):
        condition = self.data_frame[attribute] == month
        self.data_frame[condition].to_csv(file_name)


