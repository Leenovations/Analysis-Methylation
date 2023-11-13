#!/usr/bin/python3

import pandas as pd
import glob
#------------------------------------------------------------------------#
Coverage = glob.glob('Results/01.Normalized/*txt')
Coverage.sort()
#------------------------------------------------------------------------#
def trimming(Cov):
    Header = Cov.split('/')[-1]
    Header = Header.split('.')[0]

    Data = pd.read_csv(Cov, 
                       sep='\t', 
                       header=None,
                       dtype={'5': int, '4':int})

    Data[Header] = round(Data.iloc[0:,5] / Data.iloc[0:,4] * 100, 2)
    Data = Data.drop([3,4,5,6], axis=1)

list(map(trimming, Coverage))    
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#

#------------------------------------------------------------------------#