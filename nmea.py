
import math
import matplotlib.pyplot as plt
import pandas as pd
import re


class NMEA(object):

    TARGET_MESSAGE = 'GPGGA'
    # relative indexes, based on regexp I'm using below
    INDEX = {
        'fix': 5,
        'satellites': 6
    }
    # satellite count parameter limited by range 0-12
    MAX_SATELLITE_COUNT = 12

    def __init__(self, file_name='log.txt'):
        self.ttff = None
        self.plot_data = {
            'timestamp': [],
            'satellites': []
        }
        self.df = None

        self.__parse_log(file_name)

    def __data_frame(self):

        if self.df is None:
            self.df = pd.DataFrame(self.plot_data)

    def __parse_log(self, file_name):

        regex = re.compile(r't=(\d+\.?\d?),?\s\$([A-Z]{5}),(.*)')

        file = open(file_name)
        for line in file:

            res = regex.search(line)
            if res is None:
                print('String does not match expected format. Skip it.')
                continue

            if res.group(2) == self.TARGET_MESSAGE:

                timestamp = float(res.group(1))
                data = res.group(3).split(',')

                sat_count = 0
                if data[self.INDEX['satellites']]:
                    sat_count = int(data[self.INDEX['satellites']])

                    if not self.ttff and data[self.INDEX['fix']]:
                        self.ttff = timestamp

                self.plot_data['timestamp'].append(timestamp)
                self.plot_data['satellites'].append(sat_count)

        file.close()

    def print_data(self):

        self.__data_frame()
        print('TTFF = ', self.ttff)
        print(self.df)

    def show_plot(self):

        self.__data_frame()
        self.df.plot(title='Number of satellites F(time)\nTTFF = {}'.format(self.ttff),
                     x='timestamp',
                     y='satellites',
                     xlim=(0, math.ceil(self.plot_data['timestamp'][-1])+1),
                     ylim=(0, self.MAX_SATELLITE_COUNT+1),
                     xlabel='Time',
                     ylabel='Number of Satellites',
                     legend=False)
        plt.show()

    def get_ttff(self):

        return self.ttff
