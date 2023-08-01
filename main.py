
from nmea import NMEA

file_name = 'log.txt'
nmea_log = NMEA(file_name)
nmea_log.print_data()
nmea_log.show_plot()
