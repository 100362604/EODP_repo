from common.io.writeToa import readToa
from config.globalConfig import globalConfig
import matplotlib.pyplot as plt

for band in globalConfig.bands:

    #my output
    #toa_mine = readToa(directory, filename)

    #lucia soto toa
    #toa = readToa(directory, filename)

    #(toa_mine - toa_lucia)/toa_lucia tiene que ser menos que el valor que pone

    #max_rel_dif = np.max(np.abs(toa_mine -toa))

    #print("Max rel dif", max_rel_dif, "band", band)

    #plot

