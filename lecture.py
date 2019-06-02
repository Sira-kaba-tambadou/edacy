import pandas as pd
import numpy as np
import os
import xlrd
import pandas.io.api
import ExcelFile, ExcelWriter, read_excel
import xlsxwriter
import matplotlib.pyplot as plt

try:
      tf = pd.read_excel('test.xlsx','tab1')
      print(tf)
     print(tf.loc[tf['moyenne']>=10,:])
##      print(tf['moyenne'].value_counts())
##   print(tf['moyenne'][10:20])
##      print(tf.loc[tf['moyenne']>=10,:])
##      print(tf.loc[tf['age']>=20,:])
##      moy = pd.ExcelWriter('la_moyenne.xlsx', engine='xlswriter')
##      code = tf['sexe'].eq('M').astype('int')
##      code = tf['sexe'].eq('F').astype('int')
##      print(code.value_counts())
##      df = pd.DataFrame({'Data':[10,20,30,40]})
##      writer = pd.ExcelWriter('pandas.xlsx',engine='xlsxwriter')
##      df.to_excel(writer,sheet_name='sheet1')
##      workbook = writer.book
##      worksheet = writer.sheets['sheet1']
      #tf['moyenne'][10:20]
      #tf.to_excel('pandas.xlsx',index=False)
   
      
      
except xlrd.biffh.XLRDError as xlsx:
      print('FAILURE')

except ModuleNotFoundError:
      print('\nUn module n\'a pas été importé\n')
      


