import funciones as f
import pandas as pd
import os
import numpy as np
import time
# link = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ausa/flujo-vehicular-por-radares-ausa/flujo-vehicular-por-radares-2024.csv '
t0 = time.time()
if __name__ == '__main__':
    url = 'https://data.buenosaires.gob.ar/dataset/flujo-vehicular-por-radares-ausa'; year = '2024'
    if f.status_url(url):
        last_date = f.get_last_update(url, year) 
        df_name = list(filter(lambda x: x.endswith('.csv') and year in x, os.listdir(os.getcwd())))
        if df_name != []:
            if not f.check_last_update(last_date):
                df = pd.read_csv(df_name[0]) #Abro el dataset que voy a actualizar
                href = f.get_href(url,year) #Obtengo el archivo para descargar. 
                df_new = f.create_dataframe(f.download_dataset(href,last_date)) #Descargo el archivo y creo el nuevo dataframe 
                f.update_dataset(df,df_new,df_name[0],last_date)
                print('¡Dataset actualizado!')
            else:
                print('No hay actualizaciones nuevas.')
        else:
            href = f.get_href(url,year) 
            df_new = f.create_dataframe(f.download_dataset(href,last_date))
            os.remove('dataset'+last_date+'.csv')
            df_new.to_csv('dataset'+last_date+'.csv', index = False)
            print('¡Dataset descargado!')
    else:
        print('Status url: ',False)
print(time.time() - t0)
