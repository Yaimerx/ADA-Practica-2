import pandas as pd


datos = 'transaction_data.xlsx'

def read_data():
    df = pd.read_excel(datos, sheet_name='transaction_data')
    return df

def remove_dup(data):
    df_sin_dup = data.drop_duplicates(subset=['transaction_id'], keep='first')
    return df_sin_dup


data = read_data()
print("--- Datos Originales ---")
print(data.head()) 

data_limpia = remove_dup(data)
print("\n--- Datos Sin Duplicados ---")
print(data_limpia.head())


lista_final = data_limpia.to_dict(orient='records')


nombre_nuevo_archivo = 'comparacion_transacciones.xlsx'


with pd.ExcelWriter(nombre_nuevo_archivo) as writer:
    
    data.to_excel(writer, sheet_name='Datos_Originales', index=False)
    
    
    data_limpia.to_excel(writer, sheet_name='Sin_Duplicados', index=False)

print(f"Se creo un archivo comparativo '{nombre_nuevo_archivo}' con ambas hojas.")