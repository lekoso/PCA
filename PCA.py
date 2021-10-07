import sys
import os
sys.path.append('A:\Lekan\Miscellaneous\python\modules\PCA')
import PCA_func

fil_loc = 'A:\Lekan\Miscellaneous\python\modules\PCA'

try:
    dt = PCA_func.PCA_Calc(fil_loc)
    res = os.path.join(fil_loc,'Result.xlsx')
    dt.to_excel(res, sheet_name='Result', index = True)
    os.system(res)
except:
    print('Input Data possibly does not exist, or wrong directory')