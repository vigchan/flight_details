from source.attribute_grouper import AttributeGrouper
from source.dataframe_splitter import DataframeSplitter
from source.dataframe_monthwise_splitter import DataframeMonthwiseSplitter
from source.month_attribute_grouper import MonthAttributeGrouper


def generate_attribute_grouper_data():
    attribute_grouper = AttributeGrouper("data/flights.csv")
    #attribute_grouper.plot(["DESTINATION_AIRPORT"], 15, "plots/Busiest_Destination.png")
    #attribute_grouper.plot(["ORIGIN_AIRPORT"], 15, "plots/Busiest_Origin.png")
    #attribute_grouper.plot(["ORIGIN_AIRPORT", "DESTINATION_AIRPORT"], 10, "plots/Busiest_Origin_Destination_Pairs.png")
    #attribute_grouper.export(["ORIGIN_AIRPORT"], "outputFiles/origin_frequency.csv", ['ORIGIN AIRPORT', 'COUNT'])
    #attribute_grouper.export(["DESTINATION_AIRPORT"], "outputFiles/destination_frequency.csv", ['DESTINATION AIRPORT', 'COUNT'])
    #attribute_grouper.carrierPath(["AIRLINE", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"],
     #                            "outputFiles/carrier_statistics.csv",
     #                            ['AIRLINE CARRIER', 'ORIGIN AIRPORT', 'DESTINATION AIRPORT', 'COUNT'])
    #attribute_grouper.plot(["AIRLINE", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"], 20, "plots/Airline_Counts_Path.png")
    #attribute_grouper.export(["AIRLINE"], "outputFiles/airline_frequency.csv", ['AIRLINE', 'COUNT'])
    #attribute_grouper.plot(["AIRLINE"], 15, "plots/Airline_Frequency.png")

    #attribute_grouper.export(["ORIGIN_AIRPORT","MONTH"],"outputFiles/monthwise_origin_frequency.csv",
     #                        ['ORIGIN AIRPORT', 'MONTH', 'COUNT'])
    #attribute_grouper.export(["MONTH", "AIRLINE"], "outputFiles/flight_count_month_airline.csv", ['MONTH','AIRLINE', 'COUNT'])
    attribute_grouper.export(["ORIGIN_AIRPORT", "AIRLINE"], "outputFiles/airline_count_origin_airport.csv",
                             ['ORIGIN AIRPORT', 'AIRLINE', 'COUNT'])

# Class for splitting data
def generate_split_data(is_arrival):
    dataframe_splitter = DataframeSplitter("data/flights.csv")
#
    field_name = "DEPARTURE_DELAY"
    file_prefix = "departure"
    scheduled = "SCHEDULED_DEPARTURE"
    if is_arrival:
        field_name = "ARRIVAL_DELAY"
        file_prefix = "arrival"
        scheduled = "SCHEDULED_ARRIVAL"

    dataframe_splitter.early_event(["AIRLINE", scheduled, "ORIGIN_AIRPORT", field_name],
                                   field_name, "generatedCsv/early_{}.csv".format(file_prefix))

    attribute_grouper_early_event = AttributeGrouper("generatedCsv/early_{}.csv".format(file_prefix))
    #attribute_grouper_early_event.export(["AIRLINE"], "outputFiles/airline_early_{}_count.csv".format(file_prefix),
         #                                ['AIRLINE', 'COUNT'])
    #attribute_grouper_early_event.plot(["AIRLINE"], 30, "plots/Early_{}.png".format(file_prefix))

    #dataframe_splitter.late_event(["AIRLINE", scheduled, "ORIGIN_AIRPORT", field_name],
        #                          field_name, "generatedCsv/late_{}.csv".format(file_prefix))

    attribute_grouper_late_event = AttributeGrouper("generatedCsv/late_{}.csv".format(file_prefix))
    #attribute_grouper_late_event.export(["AIRLINE"], "outputFiles/airline_late_{}_count.csv".format(file_prefix),
       #                                     ['AIRLINE', 'COUNT'])
    #attribute_grouper_late_event.export(["AIRLINE"], "outputFiles/airline_late_{}_count.csv".format(file_prefix),
      #                                      ['AIRLINE', 'COUNT'])
    #attribute_grouper_late_event.plot(["AIRLINE"], 30, "plots/Late_{}.png".format(file_prefix))

    #dataframe_splitter.on_time_event(["AIRLINE", scheduled, "ORIGIN_AIRPORT", field_name],
    #                                 field_name, "generatedCsv/on_time_{}.csv".format(file_prefix))
    #attribute_grouper_on_time_event = AttributeGrouper("generatedCsv/on_time_{}.csv".format(file_prefix))
    #attribute_grouper_on_time_event.export(["AIRLINE"], "outputFiles/airline_on_time_{}_count.csv".format(file_prefix),
     #                                      ['AIRLINE', 'COUNT'])

    #attribute_grouper_on_time_event.export(["AIRLINE"], "outputFiles/airline_on_time_{}_count.csv".format(file_prefix),
     #                                      ['AIRLINE', 'COUNT'])
    #attribute_grouper_on_time_event.plot(["AIRLINE"], 30, "plots/On_Time_{}.png".format(file_prefix))


def generate_split_monthwise():
    dataframe_monthwise_splitter = DataframeMonthwiseSplitter("data/flights.csv")
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in range(0, 12):
        dataframe_monthwise_splitter.split_by_month('MONTH', month+1,
                                                    "generatedCsv/monthwiseFiles/{}.csv".format(month_names[month]))

def generate_analysis_monthwise():
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    month_attribute_groupers = []
    for month in month_names:
        month_attribute_grouper = MonthAttributeGrouper(month)
        month_attribute_groupers.append(month_attribute_grouper)

        #month_attribute_grouper.month_attribute_grouper(["ORIGIN_AIRPORT"], ["ORIGIN", "Count"],
        #                                                "originMaxFrequency", 20)
        month_attribute_grouper.month_attribute_grouper(['AIRLINE'], ["AIRLINE", "Count"],"airlineMaxFrequency", 20)
    # Write the monthly frequency into frequency



if __name__ == "__main__":
    #generate_attribute_grouper_data()
    generate_split_data(is_arrival=True)
    #generate_split_monthwise()
    #generate_analysis_monthwise()
