import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df=pd.read_excel("C:/Users/Luis/Downloads/Consolidado de ventas abril 2024.xlsx",sheet_name="Consolidado de ventas")

rd = df[['Proyecto','Fecha Fin Venta']]

rd['Fecha Fin Venta'] = pd.to_datetime(df['Fecha Fin Venta'])

rd.set_index('Fecha Fin Venta', inplace=True)

rd.iloc[0,0]

######################################################################
######################################################################NO SE QUE COÑO HE HECHO AQUÍ

df=pd.read_excel("C:/Users/Luis/Downloads/Consolidado de ventas abril 2024.xlsx",sheet_name="Consolidado de ventas",parse_dates=['Fecha Fin Venta'])

conteo = df['Fecha Fin Venta'].value_counts()

conteom = conteo.resample('m').sum()

conteom

df = pd.DataFrame(conteom)

df

df.index

plt.figure(figsize=(20,6))
plt.plot(df.index, df['count'], marker='o')
plt.title('VENTAS SPVs MES')
plt.xlabel('Fecha')
plt.ylabel('Número de Unidades Vendidas')
plt.grid()
plt.show()

