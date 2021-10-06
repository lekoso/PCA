import sys
import os
sys.path.append('A:\Lekan\Miscellaneous\python\modules')
import PCA

fil_loc = r'C:\Users\lekan\Downloads'
try:
    dt = PCA.Analys(fil_loc)
    res = os.path.join(fil_loc,'Result.xlsx')
    dt.to_excel(res, sheet_name='Result', index = True)
    os.system(res)
except:
    print('Input Data possibly does not exist, or wrong directory')