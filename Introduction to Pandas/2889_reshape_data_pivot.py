import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    resultado = weather.pivot_table(index='month', columns='city', values='temperature')
    return resultado