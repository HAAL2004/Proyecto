import pandas as pd

def creardf():
    d = {'nombre' : ['Juan'],
         'puesto' : ['Jefe']}
    return pd.DataFrame(d)


if __name__ == "__main__":
    df = creardf()
    print(df)