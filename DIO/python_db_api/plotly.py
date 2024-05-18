from pathlib import Path
import plotly_express as px
from sqlalchemy import create_engine
import pandas as pd

ROOTH_PATH = Path(__file__).parent

engine = create_engine("meu_banco.db")
query = "SELECT * FROM clientes"

df = pd.read_sql_query(query, engine)

fig = px.bar(df, x="uf", y="salario", title="Base de Salários")
fig.show()