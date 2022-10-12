"""Do another run of the L1B with the equalization enabled to false. Plot the restored signal for this case and
for the case with the equalization set to True. Compare."""

from common.io.writeToa import readToa
import matplotlib.pyplot as plt

directory_eq_true = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out'
directory_eq_false = '/Users/luciamarssanchez/Documents/Earth_Observation/lib_out_eq_false'
toa_eq_true = readToa(directory_eq_true, 'l1b_toa_VNIR-0.nc')
toa_eq_false = readToa(directory_eq_false, 'l1b_toa_VNIR-0.nc')

plt.figure()
plt.plot(toa_eq_true[50,:])
plt.plot(toa_eq_false[50,:])
#plt.show()
plt.savefig('/Users/luciamarssanchez/Documents/Earth_Observation/Figures/l1b_test3/comparison_VNIR0.eps')

#im = plt.imshow(toa_out_l1b)
#plt.colorbar(im)
#plt.show()
