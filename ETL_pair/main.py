from src import soporte as sp
from src import variable as va

print("aplicamos la funcion para nulos del df clientes")
sp.fillna(va.df_clientes, "Country", "Spain")
