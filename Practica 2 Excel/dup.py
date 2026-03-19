import pandas as pd

datos = 'transaction_data.xlsx'

def read_data():
    df = pd.read_excel(datos, sheet_name='transaction_data')
    return df
data = read_data()

def elim_dup(data):
    lista_transacciones = data.to_dict(orient='records')

    ids_vistos= set()
    data_sin_dup = []

    for fila in lista_transacciones:
        id_actual = fila['transaction_id']
        if id_actual not in ids_vistos:
            ids_vistos.add(id_actual)
            data_sin_dup.append(fila)
    return data_sin_dup

data_sin_dup = elim_dup(data)


if len(data['transaction_id']) == len(set(data['transaction_id'])):
    print("El archivo NO tiene duplicados")
    df_limpio = data.copy() 
else:
    print("Se encontraron duplicados")
    data_sin_dup = elim_dup(data)
    df_limpio = pd.DataFrame(data_sin_dup)

nombre_archivo = 'comparativo_for.xlsx'

with pd.ExcelWriter(nombre_archivo) as writer:
 
    data.to_excel(writer, sheet_name='Datos_Originales', index=False)
    
    df_limpio.to_excel(writer, sheet_name='Sin_Duplicados', index=False)

print(f"Se creó el archivo '{nombre_archivo}' para la comparativa")