#%%
import pandas as pd


dataframe = pd.DataFrame(dict(dad=(1, 2, 3), sadf=(5, 6, 7), saf=(43, 5445, 4545), adfs=(3444, 324253, 2352354354)))

dataframe_null = dataframe.isnull().sum()

#%%
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go



aa = px.line(dataframe, x=dataframe.sadf, y=dataframe.saf)

plot(aa)
