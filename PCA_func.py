# Routine to calculate Principal Component Analysis 
# given data in an excel format with a tab named 'Prices'

def PCA_Calc(loc):
    import pandas as pd
    import numpy as np
    import math as mh
    import os

    pd.options.display.float_format = '{:.6f}'.format
    pd.set_option('display.min_rows', 10)
    pd.set_option('display.max_columns', 100)
    np.set_printoptions(formatter={'float': '{: 0.8f}'.format})
    
    found = False
    
    for f in os.listdir(loc):
        if 'input' in f:
            found = True
            os.path.abspath(loc)
            loca = os.path.join(loc,f)
            data = pd.read_excel(loca, sheet_name='Prices')
            #date = data['Date']

            del data['Date']

            returns = np.log((data/data.shift(periods=1)))
            returns = returns.dropna()

            PL = data - data.shift(periods=1)
            PL = PL.dropna()

            cov_data = returns.cov()
            corr_data = returns.corr()

            #np.set_printoptions(precision=3)

            eigen = np.linalg.eig(cov_data)
            eigenVal = (np.array(eigen[0]).T)
            eigenVec = (np.array(eigen[1]))

            #Get percentage ranking of EigneValues
            hold = []
            for i in eigenVal:
                val = i * 100 / eigenVal.sum()
                hold.append(val)

            #sort columns in terms of eigenValues    
            result = pd.DataFrame(data=eigenVec, columns=hold, index=cov_data.index)
            #list = result.columns
            #result = result.reindex(columns=list)
            break
    return result