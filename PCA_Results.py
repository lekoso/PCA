import PCA
import os

fil_loc = 'A:\Lekan\Miscellaneous\python\modules\PCA'
dt = PCA.Analys(fil_loc)

res = os.path.join(fil_loc,'Result.xlsx')
dt.to_excel(res, sheet_name='Result', index = True)

os.system(res)

#print(dt)