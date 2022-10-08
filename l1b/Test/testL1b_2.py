"""For the central ALT position, plot the restored signal (l1b_toa),
and the TOA after the ISRF (ism_toa_isrf). Explain the differences."""

from common.io.writeToa import readToa
import matplotlib.pyplot as plt

directory_restored = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored = readToa(directory_restored, 'l1b_toa_VNIR-0.nc')

directory_ISRF = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/output'
toa_ISRF = readToa(directory_ISRF, 'l1b_toa_VNIR-0.nc')

print(toa_restored[49,:])
print(toa_ISRF[49,:])

plt.plot(toa_restored[49,:],toa_ISRF[49,:])
plt.show()


