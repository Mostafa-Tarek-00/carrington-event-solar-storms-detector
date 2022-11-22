import numpy as np
import pandas as pd
from netCDF4 import MFDataset

def nc_to_pd(nc_file, csv_name):
    """Converts a netCDF variable to a Pandas DataFrame"""
    nc = MFDataset(nc_file)
    features = list(nc.variables.keys())
    dict_df = {}
    for feature in features:
        dict_df[feature] = nc.variables[feature][:]
    df = pd.DataFrame(dict_df, index=None)
    df.to_csv(f"{csv_name}.csv", index=False)

nc_to_pd('07/oe*nc', "07")