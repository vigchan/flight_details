import pandas as pd

class DataframeSplitter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_frame = pd.read_csv(self.file_name, low_memory=False)
        print("The file name is: {}".format(self.file_name))


# Checking Values of Departure and Arrival delay - positive or negative
    def early_event(self, select_attributes, attribute, file_name):
        df = self.data_frame[select_attributes]
        condition = df[attribute] < 0
        df[condition].to_csv(file_name)

    def late_event(self, select_attributes, attribute, file_name):
        df = self.data_frame[select_attributes]
        condition = df[attribute] > 0
        df[condition].to_csv(file_name)

    def on_time_event(self, select_attributes, attribute, file_name):
        df= self.data_frame[select_attributes]
        condition = df[attribute] == 0
        df[condition].to_csv(file_name)

