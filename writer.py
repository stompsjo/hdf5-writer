import pandas as pd
import numpy as np
import h5py
import os


def make_group(hdf5_file, group_name):
    hdf5_file.create_group(group_name)


def init_dataset(subgrp_name, subgroup, column):
    return subgroup.create_dataset(subgrp_name,
                                   column.shape,
                                   dtype=column.dtypes)


def write_column(group, subgroup):
    for row in enumerate(group[subgroup]):
        group[row[0]] = row[1]


def main():
    # input parameters
    output_name = 'chicago_test.h5'
    ext = '.csv'
    input_name = ['nodes', 'sensors', 'data']

    # open files to be converted
    files = []
    for f in input_name:
        files.append(pd.read_csv(f + ext))

    # init HDF5 file
    ofile = h5py.File(output_name, 'a')

    # main writing script
    for csv, name in zip(files, input_name):
        print('Working on ' + name + ext)
        ofile.create_group(name)
        # each column in a file
        for col in csv:
            print('Working on ' + col)
            if csv[col].dtypes == object:
                # pandas object dtype not compatible w/ h5py
                # switch to utf-8 string encoding instead
                dt = h5py.string_dtype(encoding='utf-8')
                ofile[name].create_dataset(col,
                                           csv[col].shape,
                                           dtype=dt)
            else:
                ofile[name].create_dataset(col,
                                           csv[col].shape,
                                           dtype=csv[col].dtypes)
            for row in enumerate(csv[col]):
                # using h5py-numpy compatible nan for non-string variables
                if pd.isna(row[1]):
                    ofile[name][col][row[0]] = np.nan
                else:
                    ofile[name][col][row[0]] = row[1]

    print('Complete!')


if __name__ == "__main__":
    # for testing, remove file before trying to write
    os.system("rm chicago_test.h5")
    main()