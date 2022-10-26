from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import numpy as np

"""Check for all bands that the differences with respect to the output TOA (ism_toa_isrf) are <0.01% for at least
 3-sigma of the points."""

directory_mine = '/Users/luciamarssanchez/Documents/Earth_Observation/lsm_out'
directory_ls = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-ISM/output'

## Detection
file_detection = ['ism_toa_detection_VNIR-0.nc','ism_toa_detection_VNIR-1.nc','ism_toa_detection_VNIR-2.nc','ism_toa_detection_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_detection)):
    toa_mine_detection = readToa(directory_mine, file_detection[i])
    toa_ls_detection = readToa(directory_ls, file_detection[i])

    substraction_detection = np.zeros((toa_mine_detection.shape[0], toa_mine_detection.shape[1]))

    for ii in range(toa_mine_detection.shape[0]):
        for jj in range(toa_mine_detection.shape[1]):
            substraction_detection[ii,jj] = toa_mine_detection[ii,jj] - toa_ls_detection[ii,jj]



##### Ds
file_ds = ['ism_toa_ds_VNIR-0.nc','ism_toa_ds_VNIR-1.nc','ism_toa_ds_VNIR-2.nc','ism_toa_ds_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_ds)):
    toa_mine_ds = readToa(directory_mine, file_ds[i])
    toa_ls_ds = readToa(directory_ls, file_ds[i])

    substraction_ds = np.zeros((toa_mine_ds.shape[0], toa_mine_ds.shape[1]))

    for ii in range(toa_mine_ds.shape[0]):
        for jj in range(toa_mine_ds.shape[1]):
            substraction_ds[ii,jj] = toa_mine_ds[ii,jj] - toa_ls_ds[ii,jj]


##### e

file_e = ['ism_toa_e_VNIR-0.nc','ism_toa_e_VNIR-1.nc','ism_toa_e_VNIR-2.nc','ism_toa_e_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_detection)):
    toa_mine_e = readToa(directory_mine, file_detection[i])
    toa_ls_e = readToa(directory_ls, file_detection[i])

    substraction_e = np.zeros((toa_mine_e.shape[0], toa_mine_e.shape[1]))

    for ii in range(toa_mine_e.shape[0]):
        for jj in range(toa_mine_e.shape[1]):
            substraction_e[ii,jj] = toa_mine_e[ii,jj] - toa_ls_e[ii,jj]


#### PRNU

file_PRNU = ['ism_toa_PRNU_VNIR-0.nc','ism_toa_PRNU_VNIR-1.nc','ism_toa_PRNU_VNIR-2.nc','ism_toa_PRNU_VNIR-3.nc']
tolerance = 0.0001

for i in range(len(file_PRNU)):
    toa_mine_PRNU = readToa(directory_mine, file_PRNU[i])
    toa_ls_PRNU = readToa(directory_ls, file_PRNU[i])

    substraction_PRNU = np.zeros((toa_mine_PRNU.shape[0], toa_mine_PRNU.shape[1]))

    for ii in range(toa_mine_PRNU.shape[0]):
        for jj in range(toa_mine_PRNU.shape[1]):
            substraction_PRNU[ii,jj] = toa_mine_PRNU[ii,jj] - toa_ls_PRNU[ii,jj]



## Results

if max(map(max,substraction_detection)) <= tolerance:
    print('Test Detection: PASS')
else:
    print('Test Detection: FAIL')


if max(map(max,substraction_ds)) <= tolerance:
    print('Test Ds: PASS')
else:
    print('Test Ds: FAIL')


if max(map(max,substraction_e)) <= tolerance:
    print('Test e: PASS')
else:
    print('Test e: FAIL')


if max(map(max,substraction_PRNU)) <= tolerance:
    print('Test PRNU: PASS')
else:
    print('Test PRNU: FAIL')

