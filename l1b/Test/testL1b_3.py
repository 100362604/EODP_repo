"""Do another run of the L1B with the equalization enabled to false. Plot the restored signal for this case and
for the case with the equalization set to True. Compare."""

from common.io.writeToa import readToa
import matplotlib.pyplot as plt

directory_eq_true0 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
directory_eq_false0 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out_eq_false'
toa_eq_true0 = readToa(directory_eq_true0, 'l1b_toa_VNIR-0.nc')
toa_eq_false0 = readToa(directory_eq_false0, 'l1b_toa_VNIR-0.nc')

plt.figure()
plt.plot(toa_eq_true0[50,:],'r-', label = "Equalization = True",linewidth=1.0)
plt.plot(toa_eq_false0[50,:],'b-', label = "Equalization = False",linewidth=1.0)
plt.legend()
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test3/comparison_VNIR0.eps')

######################
directory_eq_true1 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
directory_eq_false1 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out_eq_false'
toa_eq_true1 = readToa(directory_eq_true0, 'l1b_toa_VNIR-1.nc')
toa_eq_false1 = readToa(directory_eq_false0, 'l1b_toa_VNIR-1.nc')

plt.figure()
plt.plot(toa_eq_true1[50,:],'r-', label = "Equalization = True",linewidth=1.0)
plt.plot(toa_eq_false1[50,:],'b-', label = "Equalization = False",linewidth=1.0)
plt.legend()
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test3/comparison_VNIR1.eps')

################
directory_eq_true2 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
directory_eq_false2 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out_eq_false'
toa_eq_true2 = readToa(directory_eq_true2, 'l1b_toa_VNIR-2.nc')
toa_eq_false2 = readToa(directory_eq_false2, 'l1b_toa_VNIR-2.nc')

plt.figure()
plt.plot(toa_eq_true2[50,:],'r-', label = "Equalization = True",linewidth=1.0)
plt.plot(toa_eq_false2[50,:],'b-', label = "Equalization = False",linewidth=1.0)
plt.legend()
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test3/comparison_VNIR2.eps')

######################
directory_eq_true3 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
directory_eq_false3 = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out_eq_false'
toa_eq_true3 = readToa(directory_eq_true3, 'l1b_toa_VNIR-3.nc')
toa_eq_false3 = readToa(directory_eq_false3, 'l1b_toa_VNIR-3.nc')

plt.figure()
plt.plot(toa_eq_true3[50,:],'r-', label = "Equalization = True",linewidth=1.0)
plt.plot(toa_eq_false3[50,:],'b-', label = "Equalization = False",linewidth=1.0)
plt.legend()
plt.xlabel("ACT [-]")
plt.ylabel("TOA [mW/m2/sr]")
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test3/comparison_VNIR3.eps')