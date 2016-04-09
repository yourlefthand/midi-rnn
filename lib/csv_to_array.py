import csv

def convert(filepath):
    out_arr = []
    with open(filepath,'rb') as csvfile:
        rd = csv.reader(csvfile, delimiter=',')
        for row in rd:
            out_arr.append(row)
    return out_arr
