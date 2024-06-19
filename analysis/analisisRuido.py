import pandas as pd

from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido():
    datosRuido=generarDatosRuido()
    dataFrameRuido=pd.DataFrame(datosRuido,columns=["id","nivelRuido","comuna"])
    dataFrameRuido.to_csv("datosRuido.csv",index=False)
    print(dataFrameRuido)

construirDataRuido()