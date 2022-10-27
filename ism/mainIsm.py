
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = '/Users/luciamarssanchez/Documents/EODP_repo/auxiliary'
#indir = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-ISM/input/gradient_alt100_act150' # small scene
#outdir = '/Users/luciamarssanchez/Documents/Earth_Observation/lsm_out'
indir = '/Users/luciamarssanchez/Documents/Earth_Observation/EODP_TER_2021/EODP-TS-E2E/sgm_out'
outdir = '/Users/luciamarssanchez/Documents/Earth_Observation/lsm_out_touluse'


#Clear the File Rad"Irrad
#file = open('')

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
