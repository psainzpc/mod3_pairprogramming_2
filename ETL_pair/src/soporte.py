def fillna(dataframe, columna, valor):
    """
    Rellena los valores nulos (NaN) de una columna de un DataFrame con un valor específico.

    Parameters:
    -----------
    dataframe : pandas.DataFrame
        El DataFrame en el que se realizará la operación de rellenado.
    
    columna : str
        El nombre de la columna en la que se desea rellenar los valores nulos.
    
    valor : 
        El valor con el que se reemplazarán los valores nulos en la columna especificada.
        Puede ser un valor escalar, como un número, cadena, o incluso un valor más complejo,
        dependiendo de los datos de la columna.

    Returns:
    --------
    None
        La función modifica el DataFrame en su lugar, por lo que no retorna ningún valor.
    """
    dataframe[columna] = dataframe[columna].fillna(valor)
    return