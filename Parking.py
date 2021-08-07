# Session 13 - Assignment - Ganesan Thiagarajan - Parking ticket records processing

from collections import namedtuple
from datetime import date

#
# Create the namedtuple templates for the parking record and date format
#
parking_record = namedtuple('record','summon_num, plate_no, plate_state, plate_type, issue_date, violation_code, veh_type, veh_make, reason')
date_of_record = namedtuple('date','day month year')

def read_file(file):
    """
    Reads a give file lazily - i.e., creates generator to reac one record at a time
    :param file: Filename as a string
    :return: One line from the file for each call.
    """
    with open(file, encoding='utf8', errors='ignore') as f:
        for line in f:
            yield line.strip('\n')

def find_violation_stats_from_file(file, make):
    """
    Computes the statistics for the parking violation from the records in the file 'file' for the given car make 'make'
    It skips the first line as the header for the data records description
    :param file:  Filename as a string with full path
    :param make: Car make for which statistics are obtained
    :return: Statistics on how many violations
    """
    num_violations = 0
    header_read = 1
    for rec in read_file('nyc_parking_tickets_extract.csv'):
        if header_read == 1:
            header_read = 0
        else:
            data = rec.split(",")
            date_mm_yy_yyyy = [int(i) for i in data[4].split("/")]
            # date_in_format = date(date_mm_yy_yyyy[2],date_mm_yy_yyyy[0], date_mm_yy_yyyy[1])    # Date as date object
            date_in_format = date_of_record(date_mm_yy_yyyy[1], date_mm_yy_yyyy[0],
                                            date_mm_yy_yyyy[2])  # Date as namedtuple
            record = parking_record(int(data[0]), data[1], data[2], data[3], date_in_format, int(data[5]), data[6],
                                    data[7], data[8])
            if record.veh_make == make:
                num_violations += 1
    return num_violations

def read_from_records(records):
    """
    Lazy iterator for reading one record at a time from the given list of namedtuples
    :param records: List of namedtuples
    :return: One namedtuple record
    """
    for rec in records:
        yield rec

def find_violation_stats_from_records(records, make):
    """
    Computes the statistics for the parking violation from the list of records 'records' for the given car make 'make'
    :param records:  list of namedtuples
    :param make: Car make for which statistics are obtained
    :return: Statistics on how many violations
    """
    num_violations = 0
    record = read_from_records(records)
    for _ in range(len(records)):
        #record = parking_record(int(data[0]), data[1], data[2], data[3], date_in_format, int(data[5]), data[6],
        #                        data[7], data[8])
        rec = record.__next__()
        if rec.veh_make == make:
            num_violations += 1
    return num_violations

# Goal 1 Solution
def create_record_generator(file):
    """
    Generates a list of namedtuples from the records in the file 'file'
    :param file: Filename as a string with fullpath
    :return: List of namedtuples
    """
    header_read = 1
    records = []
    for rec in read_file(file):
        if header_read == 1:
            header_read = 0
        else:
            data = rec.split(",")
            date_mm_yy_yyyy = [int(i) for i in data[4].split("/")]
            #date_in_format = date(date_mm_yy_yyyy[2],date_mm_yy_yyyy[0], date_mm_yy_yyyy[1])    # Date as date object
            date_in_format = date_of_record(date_mm_yy_yyyy[1], date_mm_yy_yyyy[0], date_mm_yy_yyyy[2])  # Date as namedtuple
            records.append(parking_record(int(data[0]), data[1], data[2], data[3], date_in_format, int(data[5]), data[6], data[7], data[8]))
    return records


# Goal 1 solution
violation_recs = create_record_generator('nyc_parking_tickets_extract.csv')
#print(violation_recs)

# Goal 2 Solution
car_make = 'HONDA'
num_violations1 = find_violation_stats_from_records(violation_recs, car_make)
print(f'Number of violations mades by {car_make} is {num_violations1} -- by method 1')
num_violations2 = find_violation_stats_from_file('nyc_parking_tickets_extract.csv', car_make)
print(f'Number of violations mades by {car_make} is {num_violations2} -- by method 2')

car_make = 'CHEVR'
num_violations1 = find_violation_stats_from_records(violation_recs, car_make)
print(f'Number of violations mades by {car_make} is {num_violations1} -- by method 1')
num_violations2 = find_violation_stats_from_file('nyc_parking_tickets_extract.csv', car_make)
print(f'Number of violations mades by {car_make} is {num_violations2} -- by method 2')
