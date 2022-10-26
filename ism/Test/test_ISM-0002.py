from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np

"""Check for all bands that the differences with respect to the output TOA (ism_toa_isrf) are <0.01% for at least
 3-sigma of the points."""

directory_mine = '/Users/luciamarssanchez/Documents/Earth_Observation/lsm_out'
directory_ls = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-ISM/output'

file = ['ism_toa_VNIR-0.nc','ism_toa_VNIR-1.nc','ism_toa_VNIR-2.nc','ism_toa_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file)):
    toa_mine = readToa(directory_mine, file[i])
    toa_ls = readToa(directory_ls, file[i])

    substraction = np.zeros((toa_mine.shape[0], toa_mine.shape[1]))

    for ii in range(toa_mine.shape[0]):
        for jj in range(toa_mine.shape[1]):
            substraction[ii,jj] = toa_mine[ii,jj] - toa_ls[ii,jj]


if max(map(max,substraction)) <= tolerance:
    print('Test 1 ISRF: PASS')
else:
    print('Test 1 ISRF: FAIL')

print(max(map(max,substraction)))