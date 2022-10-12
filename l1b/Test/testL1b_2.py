"""For the central ALT position, plot the restored signal (l1b_toa),
and the TOA after the ISRF (ism_toa_isrf). Explain the differences."""

from common.io.writeToa import readToa
import matplotlib.pyplot as plt

directory_restored = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored = readToa(directory_restored, 'l1b_toa_VNIR-0.nc')

directory_ISRF = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/input'
toa_ISRF = readToa(directory_ISRF, 'ism_toa_isrf_VNIR-0.nc')

plt.plot(toa_restored[50,:])
plt.plot(toa_ISRF[50,:])
plt.show()


