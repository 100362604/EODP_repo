from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np

"""Check for all bands that the differences with respect to the output TOA (ism_toa_isrf) are <0.01% for at least
 3-sigma of the points."""

directory_mine = '/Users/luciamarssanchez/Documents/Earth_Observation/lsm_out'
directory_ls = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-ISM/output'

file_isrf = ['ism_toa_isrf_VNIR-0.nc','ism_toa_isrf_VNIR-1.nc','ism_toa_isrf_VNIR-2.nc','ism_toa_isrf_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_isrf)):
    toa_mine_isrf = readToa(directory_mine, file_isrf[i])
    toa_ls_isrf = readToa(directory_ls, file_isrf[i])

    substraction_isrf = np.zeros((toa_mine_isrf.shape[0], toa_mine_isrf.shape[1]))

    for ii in range(toa_mine_isrf.shape[0]):
        for jj in range(toa_mine_isrf.shape[1]):
            substraction_isrf[ii,jj] = toa_mine_isrf[ii,jj] - toa_ls_isrf[ii,jj]

if max(map(max,substraction_isrf)) <= tolerance:
    print('Test 1 ISRF: PASS')
else:
    print('Test 1 ISRF: FAIL')

""" Check for all bands that the differences with respect to the output TOA (ism_toa_optical) 
are <0.01% for at least 3-sigma of the points."""

file_optical =['ism_toa_optical_VNIR-0.nc','ism_toa_optical_VNIR-1.nc','ism_toa_optical_VNIR-2.nc','ism_toa_optical_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_optical)):
    toa_mine_optical = readToa(directory_mine, file_optical[i])
    toa_ls_optical = readToa(directory_ls, file_optical[i])

    substraction_optical = np.zeros((toa_mine_optical.shape[0], toa_mine_optical.shape[1]))

    for ii in range(toa_mine_optical.shape[0]):
        for jj in range(toa_mine_optical.shape[1]):
            substraction_optical[ii,jj] = toa_mine_optical[ii,jj] - toa_ls_optical[ii,jj]

if max(map(max,substraction_optical)) <= tolerance:
    print('Test 1 OPTICAL: PASS')
else:
    print('Test 1 OPTICAL: FAIL')


