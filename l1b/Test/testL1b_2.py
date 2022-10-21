"""For the central ALT position, plot the restored signal (l1b_toa),
and the TOA after the ISRF (ism_toa_isrf). Explain the differences."""

from common.io.writeToa import readToa
import matplotlib.pyplot as plt

directory_restored0 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored0 = readToa(directory_restored0, 'l1b_toa_VNIR-0.nc')

directory_ISRF0 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/input'
toa_ISRF0 = readToa(directory_ISRF0, 'ism_toa_isrf_VNIR-0.nc')

plt.figure()
plt.plot(toa_restored0[50,:],'r-', label = "Restored Signal",linewidth=1.0)
plt.plot(toa_ISRF0[50,:],'b-', label = "TOA after ISRF",linewidth=1.0)
plt.legend()
#plt.title("")
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test2/comparison_VNIR0.eps')

###################
directory_restored1 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored1 = readToa(directory_restored1, 'l1b_toa_VNIR-1.nc')

directory_ISRF1 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/input'
toa_ISRF1 = readToa(directory_ISRF1, 'ism_toa_isrf_VNIR-1.nc')

plt.figure()
plt.plot(toa_restored1[50,:],'r-', label = "Restored Signal",linewidth=1.0)
plt.plot(toa_ISRF1[50,:],'b-', label = "TOA after ISRF",linewidth=1.0)
plt.legend()
#plt.title("")
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test2/comparison_VNIR1.eps')

###################
directory_restored2 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored2 = readToa(directory_restored2, 'l1b_toa_VNIR-2.nc')

directory_ISRF2 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/input'
toa_ISRF2 = readToa(directory_ISRF2, 'ism_toa_isrf_VNIR-2.nc')

plt.figure()
plt.plot(toa_restored2[50,:],'r-', label = "Restored Signal",linewidth=1.0)
plt.plot(toa_ISRF2[50,:],'b-', label = "TOA after ISRF",linewidth=1.0)
plt.legend()
#plt.title("")
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test2/comparison_VNIR2.eps')

###################
directory_restored3 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
toa_restored3 = readToa(directory_restored3, 'l1b_toa_VNIR-3.nc')

directory_ISRF3 = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-L1B/input'
toa_ISRF3 = readToa(directory_ISRF3, 'ism_toa_isrf_VNIR-3.nc')

plt.figure()
plt.plot(toa_restored3[50,:],'r-', label = "Restored Signal",linewidth=1.0)
plt.plot(toa_ISRF3[50,:],'b-', label = "TOA after ISRF",linewidth=1.0)
plt.legend()
#plt.title("")
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test2/comparison_VNIR3.eps')
