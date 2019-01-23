from scipy import stats
import pandas as pd
import sys

filename = sys.argv[1]
df = pd.read_csv(filename, usecols=[1, 2]).values
slope, intercept, r_value, p_value, std_err = stats.linregress(df[:, 0], df[:, 1])
print slope, intercept, r_value, p_value, std_err
