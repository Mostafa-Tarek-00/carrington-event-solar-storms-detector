import pandas as pd
from spacepy import pycdf
import os
import numpy as np

params_list = ['Alpha_Na_nonlin', 'Alpha_VX_nonlin', 'Alpha_VY_nonlin', 'Alpha_VZ_nonlin', 'Alpha_V_nonlin', 'Alpha_W_nonlin', 'Alpha_Wpar_nonlin', 'Alpha_Wperp_nonlin', 'Alpha_sigmaNa_nonlin', 'Alpha_sigmaVX_nonlin', 'Alpha_sigmaVY_nonlin', 'Alpha_sigmaVZ_nonlin', 'Alpha_sigmaV_nonlin', 'Alpha_sigmaW_nonlin', 'Alpha_sigmaWpar_nonlin', 'Alpha_sigmaWperp_nonlin', 'Ang_dev', 'BX', 'BY', 'BZ', 'ChisQ_DOF_nonlin', 'EW_flowangle', 'Epoch', 'NS_flowangle', 'Peak_doy', 'Proton_Np_moment', 'Proton_Np_nonlin', 'Proton_VX_moment', 'Proton_VX_nonlin', 'Proton_VY_moment', 'Proton_VY_nonlin', 'Proton_VZ_moment', 'Proton_VZ_nonlin', 'Proton_V_moment', 'Proton_V_nonlin', 'Proton_W_moment', 'Proton_W_nonlin', 'Proton_Wpar_moment', 'Proton_Wpar_nonlin', 'Proton_Wperp_moment', 'Proton_Wperp_nonlin', 'Proton_sigmaNp_nonlin', 'Proton_sigmaVX_nonlin', 'Proton_sigmaVY_nonlin', 'Proton_sigmaVZ_nonlin', 'Proton_sigmaV_nonlin', 'Proton_sigmaW_nonlin', 'Proton_sigmaWpar_nonlin', 'Proton_sigmaWperp_nonlin', 'SigmaEW_flowangle', 'SigmaNS_flowangle', 'dev', 'doy', 'fit_flag', 'sigmaPeak_doy', 'xgse', 'year', 'ygse', 'ygsm', 'zgse', 'zgsm']

#cdf_to_df = lambda cdf: pd.DataFrame({param: cdf[param][:] for param in params_list})

def cdf_to_df():
    narr = np.array([])
    dict_df = dict.fromkeys(params_list, narr)
    years = os.listdir("testdata")
    for year in years:
        print(year)
        files = os.listdir(f"testdata/{year}")
        for file in files:
            cdf = pycdf.CDF(f"testdata/{year}/{file}")
            for param in params_list:
                dict_df[param] = np.append(dict_df[param], cdf[param][:])
    df = pd.DataFrame(dict_df, index=None)
    df.to_csv("norm_test.csv", index=False)
    return

cdf_to_df()