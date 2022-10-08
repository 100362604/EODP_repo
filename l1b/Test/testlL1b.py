from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import matplotlib.pyplot as plt

#for band in globalConfig.bands:

    #my toa
directory_mine = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_mine = readToa(directory_mine, 'l1b_toa_eq_VNIR-0.nc')

    #toa lucia soto
directory_ls = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/output'
toa_ls = readToa(directory_ls,'l1b_toa_eq_VNIR-0.nc')

substraction = (toa_mine - toa_ls)
print(substraction)

#max and min value of the substraction

print(max(map(max, substraction)))
print(min(map(min, substraction)))





