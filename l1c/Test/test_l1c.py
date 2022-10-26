from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np

"""Check for all bands that the differences with respect to the output TOA (ism_toa_isrf) are <0.01% for at least
 3-sigma of the points."""

directory_mine = '/Users/luciamarssanchez/Documents/Earth_Observation/l1c_out'
directory_ls = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1C/output'

file = ['l1c_toa_VNIR-0.nc','l1c_toa_VNIR-1.nc','l1c_toa_VNIR-2.nc','l1c_toa_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file)):
    toa_mine = readToa(directory_mine, file[i])
    toa_ls = readToa(directory_ls, file[i])

    toa_mine_sorted = np.sort(toa_mine)
    toa_ls_sorted = np.sort(toa_ls)

    substraction = np.zeros((toa_mine_sorted.shape[0]))

    substraction = toa_mine_sorted - toa_ls_sorted

if max(substraction) <= tolerance:
    print('Test L1B: PASS')
else:
    print('Test L1B: FAIL')

print(max(substraction))
