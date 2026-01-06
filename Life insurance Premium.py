import pandas as pd
import numpy as np
from scipy.linalg import qr
data = { 
    "age": list(range(20,101)),
    "qx": [ 0.0006, 0.0006,0.0007,0.0007,0.0007,0.0007,0.0008,0.0008,0.0009,0.0010,0.0011,0.0012,0.0013,0.0014,0.0016,
           0.0018,0.0020,0.0022,0.0025,0.0028,0.0030,0.0035,0.0040,0.0045,0.0050,0.0057,0.0065,0.0075,0.0088,0.0102,0.0120,
           0.0140,0.0165,0.0195,0.0230,0.0270,0.0320,0.0380,0.0450,0.0530,0.0630,0.0750,0.0900,0.1100,0.1300,0.1550,0.1850,0.2200,0.2600,0.3100,0.3600,
           0.4200,0.4800,0.5400,0.6000,0.6500,0.6900,0.7300,0.7700,0.8000,0.8300,0.8600,0.8900,0.9200,0.9400,0.9600,0.9700,0.9800,0.9850,0.9900,0.9950,
           0.9990,0.9999,0.9999,0.9999,0.9999,0.9999,0.9999,0.9999,0.9999
    ]
    }

mort_table = pd.DataFrame(data)

mort_table["px"]=1 - mort_table["qx"]

def net_single_premium(age,sum_assured = 100000,interest = 0.05):
    v = 1/(1+interest)
    pv = 0
    survival_prob = 1

    for i in range(age,100):
        qx = mort_table.loc[mort_table["age"] ==i, "qx"].values[0]
        px = 1 -qx
        death_prob_this_year = survival_prob * qx

        year = i - age + 1
        pv += death_prob_this_year * (v**year)*sum_assured

        survival_prob *= px

    return pv

#calling the function
age = 30
sum_assured = 100000
interest = 0.05

nsp = net_single_premium(age,sum_assured,interest)

print(f"Net single premium for age {age}:R{nsp:,.2f}")