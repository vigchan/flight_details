import pandas as pd
import matplotlib.pyplot as plt

class AttributeGrouper:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_frame = pd.read_csv(self.file_name, low_memory=False)
        print("The file name is: {}".format(self.file_name))
        if self.data_frame.empty:
            print('Data Frame is empty')
        else:
            print('DataFrame Dimensions:', self.data_frame.shape)

# Creating Plots for data

    def plot(self, attributes, top_rank, out_file_name=None):
        if self.data_frame.empty:
            return
        plt.gcf().subplots_adjust(bottom=0.3)
        out = self.data_frame[attributes].groupby(attributes).size().sort_values(ascending=False).head(top_rank)
        if out_file_name is None:
            out.plot.bar()
        else:
            out.plot.bar().get_figure().savefig(out_file_name)
        print("Plot Complete")

# Exporting CSV files
    def export(self, attributes, file_name, column_headers):
        if self.data_frame.empty:
            return
        out = self.data_frame[attributes].groupby(attributes).size().sort_values(ascending=False)

        out.to_csv(file_name, header=True, index_label=column_headers)

# Grouping Carrier and then Origin destination pairs and counts.
    def carrierPath(self, attributes, file_name, column_headers):
        if self.data_frame.empty:
            return
        out = self.data_frame[attributes].groupby(attributes).size().sort_values(ascending=False)

        out.to_csv(file_name, header=True, index_label=column_headers)

    