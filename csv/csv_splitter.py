"""
Runs on Python2.7
The csv input file must contain atleast 3 columns in the following order: Easting, Northing, Height.
The splitted csv files will be renamed according to the data columns they contain.  
"""


import argparse
import sys
import csv

parser = argparse.ArgumentParser(description='Splitting an input csv file into multiple output csv files in desired format.')
parser.add_argument('-s', '--sensorpoints', help='Path to file with input sensor points data')
parser.add_argument('-fo', '--outputfilename', help='The name of the output files names generated from file splitting')
parser.add_argument('-sp', '--separator', help='The Separator between columns of the input CSV file')


sensordatafile="samplelidardata.csv"
csv_delimiter=" "
out_filename='output'

# Iterate through the arguments
arguments=[]
for arg_pos in range(1,len(sys.argv)):
    t_argument=sys.argv[arg_pos].split('=')[0]
    arguments=arguments+[t_argument]

# No more than three arguments is accepted
if(len(arguments)>3):
    raise ValueError("Only three arguments expected")

args = parser.parse_args()

# Parse the argument into sensor data file
if ('-s' in arguments):
    if args.sensorpoints:
        sensordatafile=args.sensorpoints

# Parse the argument into outputfilename
if ('-fo' in arguments):
    if args.outputfilename:
        out_filename=args.outputfilename

# Parse the argument into csv_separator
if ('-sp' in arguments):
    if args.separator:
        csv_delimiter=args.separator


# Gives the number of columns in a csv file
def check_collumns(filename, csv_separator):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=csv_separator)
        return len(next(readCSV))


def csv_splitter(filename, outputfile, csv_separator):
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=csv_separator)
        collumns = check_collumns(filename, csv_separator)
        # XYZ
        if (collumns == 3):
            with open(outputfile + '_XYZ.csv', 'w') as writeFile:
                writer = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in readCSV:
                    O_ROW = [(float(row[0])), (float(row[1])), (float(row[2]))]
                    writer.writerow(O_ROW)
            writeFile.close()
        # XYZL
        elif (collumns == 4):
            with open(outputfile + '_XYZL.csv', 'w') as writeFile:
                writer = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in readCSV:
                    O_ROW = [(float(row[0])), (float(row[1])), (float(row[2])), (float(row[3]))]
                    writer.writerow(O_ROW)
            writeFile.close()
        # XYZRGB
        elif (collumns == 6):
            with open(outputfile + '_XYZ.csv', 'w') as writeFile:
                writer_xyz = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(outputfile + '_RGB.csv', 'w') as writeFile:
                    writer_rgb = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in readCSV:
                        XYZ_ROW = [(float(row[0])), (float(row[1])), (float(row[2]))]
                        RGB_ROW = [(float(row[3])), (float(row[4])), (float(row[5]))]
                        writer_xyz.writerow(XYZ_ROW)
                        writer_rgb.writerow(RGB_ROW)
                writeFile.close()
            writeFile.close()
        # XYZRGBL
        elif (collumns == 7):
            with open(outputfile + '_XYZL.csv', 'w') as writeFile:
                writer_xyzl = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(outputfile + '_RGB.csv', 'w') as writeFile:
                    writer_rgb = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in readCSV:
                        XYZL_ROW = [(float(row[0])), (float(row[1])), (float(row[2])), (float(row[6]))]
                        RGB_ROW = [(float(row[3])), (float(row[4])), (float(row[5]))]
                        writer_xyzl.writerow(XYZL_ROW)
                        writer_rgb.writerow(RGB_ROW)
                writeFile.close()
            writeFile.close()
        # XYZRGBAL
        elif (collumns >= 8):
            with open(outputfile + '_XYZL.csv', 'w') as writeFile:
                writer_xyzl = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                with open(outputfile + '_RGBA.csv', 'w') as writeFile:
                    writer_rgba = csv.writer(writeFile, delimiter=csv_separator, quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in readCSV:
                        XYZL_ROW = [(float(row[0])), (float(row[1])), (float(row[2])), (float(row[7]))]
                        RGBA_ROW = [(float(row[3])), (float(row[4])), (float(row[5])), (float(row[6]))]
                        writer_xyzl.writerow(XYZL_ROW)
                        writer_rgba.writerow(RGBA_ROW)
                writeFile.close()
            writeFile.close()
        else:
            raise NameError('Unknown file format used!')
    csvfile.close()

# Main operation starts here
csv_splitter(sensordatafile, out_filename, csv_delimiter)
