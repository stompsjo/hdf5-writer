import pandas as pd
import time
import os


def main():
    # input parameters
    data_directory = 'AoT_Chicago.complete.2020-05-04/'
    output_name = 'chicago_test.h5'
    ext = '.csv'
    input_name = ['nodes', 'sensors', 'data']

    # open files to be converted
    files = []
    for f in input_name:
        files.append(pd.read_csv(data_directory + f + ext))

    # main writing script
    for csv, name in zip(files, input_name):
        print('Working on ' + name + ext)

        # use pandas to add each csv to hdf5 file
        csv.to_hdf(output_name, name, mode='a')

    print('Complete!')


if __name__ == "__main__":
    # for testing, remove file before trying to write
    os.system("rm chicago_test.h5")
    start_time = time.time()
    main()
    print('File writer took %.2f seconds for this file size.'
          % (time.time() - start_time))
