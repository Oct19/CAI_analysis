import numpy as np
import pandas as pd
from matplotlib import pyplot

# Read reference data from excel sheets
xls_ref = pd.ExcelFile('Data/reference.xlsx')
df_ref_knee = pd.read_excel(xls_ref, 'knee')
df_ref_ankle = pd.read_excel(xls_ref, 'ankle')
df_ref_TA = pd.read_excel(xls_ref, 'TA')
df_ref_GAL = pd.read_excel(xls_ref, 'GAL')
df_ref_BF = pd.read_excel(xls_ref, 'BF')
df_ref_VM = pd.read_excel(xls_ref, 'VM')

# Read Anybody data from excel sheets
xls_any = pd.ExcelFile('Data/anybody.xlsx')
df_any_knee = pd.read_excel(xls_any, 'knee')
df_any_ankle = pd.read_excel(xls_any, 'ankle')
df_any_TA = pd.read_excel(xls_any, 'TA')
df_any_GAL = pd.read_excel(xls_any, 'GAL')
df_any_BF = pd.read_excel(xls_any, 'BF')
df_any_VM = pd.read_excel(xls_any, 'VM')

# Get Pearson value
corr_knee = df_ref_knee['mean'].corr(df_any_knee['healthy'])
corr_ankle = df_ref_ankle['mean'].corr(df_any_ankle['healthy'])
corr_TA = df_ref_TA['mean'].corr(df_any_TA['healthy'])
corr_GAL = df_ref_GAL['mean'].corr(df_any_GAL['healthy'])
corr_BF = df_ref_BF['mean'].corr(df_any_BF['healthy'])
corr_VM = df_ref_VM['mean'].corr(df_any_VM['healthy'])

# Create Pearson value dataframe
corr_all = {'Name':['Knee','Ankle','TA','GAL','BF','VM'],'Value':[corr_knee, corr_ankle, corr_TA, corr_GAL, corr_BF, corr_VM]}
df_corr_all = pd.DataFrame(corr_all)

print(df_corr_all)

""" # plot
df_ref_knee['mean'].plot()
df_any_knee['healthy'].plot()
pyplot.show() """
