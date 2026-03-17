import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtragem = animals[animals['weight'] > 100]
    animais_ordenados = filtragem.sort_values('weight', ascending=False)
    names = animais_ordenados[['name']]
    return names