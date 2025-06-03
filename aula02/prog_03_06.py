import pandas as pd
import numpy as np

def data_set ( fname ):
    resultado = {}
    resultado['nome-arquivo'] = fname
    data = pd.read_csv(fname)
    cols = data.columns
    ultima = cols[-1]

    classes = data[ultima]
    df = data.drop(columns=ultima)
    print(classes)
    print(df)
    resultado['dados'] = df

    return resultado

FNAME = 'iris.data.csv'
if __name__ == '__main__':
    data = data_set(FNAME)
    print(data)
    print('-'*40)
    print('nome-arquivo --> ', data['nome-arquivo'])