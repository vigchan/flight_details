from source.attribute_grouper import AttributeGrouper


class MonthAttributeGrouper(object):

    MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                   "October",
                   "November", "December"]

    def __init__(self, month):
        self.attribute_grouper = AttributeGrouper("generatedCsv/monthwiseFiles/{}.csv".format(month))
        self.month = month

    def plot(self, attributes, top_rank, out_file_name=None):
        self.attribute_grouper.plot(attributes, top_rank, out_file_name)

    def export(self, attributes, file_name, column_headers):
        self.attribute_grouper.export(attributes, file_name, column_headers)

    def month_attribute_grouper(self, attributes, headers, purpose, top_rank):
        self.export(attributes, "outputFiles/monthwiseAggregates/{}_{}.csv".format(self.month, purpose), headers)
        self.plot(attributes, top_rank, "plots/monthwiseAggregates/{}_{}.png".format(self.month, purpose))
