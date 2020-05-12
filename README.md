# hdf5-writer

Python script for writing csv files as hdf5 files using Pandas, Numpy, and H5PY.
Originally intended for Waggle, but sufficiently modular to be changed for other CSV files.

## Dependencies

This script uses the following Python packages: Pandas, Numpy, and H5PY.
These can be installed easilly with `pip install --user <PACKAGE_NAME>`.
This should be used with Python 3.

## Running

Change the input parameters in `main()` for the desired names/structure of CSV files.
Make sure that the CSV files to convert are in the running directory, then execute
`python writer.py`. Once complete, an `.h5` file should be available.
