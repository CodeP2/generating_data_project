import eq_explore_data

import plotly.express as px


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=eq_explore_data.lats, lon=eq_explore_data.lons, title=title)
fig.show()
