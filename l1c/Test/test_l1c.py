"""Check for all bands that the differences with respect to the output TOA (l1b_toa_)
are <0.01% for at least 3-sigma of the points."""

from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import matplotlib.pyplot as plt

#for band in globalConfig.bands:
################################
#my toa
directory_mine0 = '/Users/luciamarssanchez/Documents/Earth_Observation/l1c_out'
toa_mine0 = readToa(directory_mine0, 'l1c_toa_VNIR-0.nc')

#toa lucia soto
directory_ls0 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1C/output'
toa_ls0 = readToa(directory_ls0,'l1c_toa_VNIR-0.nc')

substraction0 = (toa_mine0 - toa_ls0)
print(substraction0)
#max and min value of the substraction

#print(max(map(max, substraction0)))
#print(min(map(min, substraction0)))

###################################
directory_mine1 = '/Users/luciamarssanchez/Documents/Earth_Observation/l1c_out'
toa_mine1 = readToa(directory_mine1, 'l1c_toa_VNIR-1.nc')

directory_ls1 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1C/output'
toa_ls1 = readToa(directory_ls1,'l1c_toa_VNIR-1.nc')

substraction1 = (toa_mine1 - toa_ls1)
print(substraction1)

print(max(map(max, substraction1)))
print(min(map(min, substraction1)))

#############################
directory_mine2 = '/Users/luciamarssanchez/Documents/Earth_Observation/l1c_out'
toa_mine2 = readToa(directory_mine2, 'l1c_toa_VNIR-2.nc')

directory_ls2 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1C/output'
toa_ls2 = readToa(directory_ls2,'l1c_toa_VNIR-2.nc')

substraction2 = (toa_mine2 - toa_ls2)
print(substraction2)

print(max(map(max, substraction2)))
print(min(map(min, substraction2)))

####################################
directory_mine3 = '/Users/luciamarssanchez/Documents/Earth_Observation/l1c_out'
toa_mine3 = readToa(directory_mine3, 'l1c_toa_VNIR-3.nc')

directory_ls3 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1C/output'
toa_ls3 = readToa(directory_ls3,'l1c_toa_VNIR-3.nc')

substraction3 = (toa_mine3 - toa_ls3)
print(substraction3)

print(max(map(max, substraction3)))
print(min(map(min, substraction3)))

###############################





