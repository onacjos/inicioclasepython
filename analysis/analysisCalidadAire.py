import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando un dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna","ica","fecha","id"])
    dataFrameICA.to_csv("datosICA.csv",index=False)
    #dataFrameICA.to_excel("datosICA.xlsx",index=False)
    print(dataFrameICA)

    #generando grafico de los datos por comuna
    datosOrdenadosPorComuna=dataFrameICA.groupby("comuna")["ica"].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadosPorComuna.plot(kind="bar",color="green")
    plt.show()

construirDataICA()