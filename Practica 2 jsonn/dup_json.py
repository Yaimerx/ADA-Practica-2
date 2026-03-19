import pandas as pd


datos = 'transaction_data.json'

def read_data():
   
    df = pd.read_json(datos)
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

df_limpio = pd.DataFrame(data_sin_dup)


nombre_archivo = 'comparativo_desde_json.xlsx' 

with pd.ExcelWriter(nombre_archivo) as writer:
    data.to_excel(writer, sheet_name='Datos_Originales', index=False)
    df_limpio.to_excel(writer, sheet_name='Sin_Duplicados', index=False)

print(f"Se creó el archivo '{nombre_archivo}' para la comparativa")