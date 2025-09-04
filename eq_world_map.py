import eq_explore_data

import plotly.express as px


title = 'Global Earthquakes'
fig = px.scatter_geo(
    lat=eq_explore_data.lats, lon=eq_explore_data.lons,
    size=eq_explore_data.mags, title=title,
    color=eq_explore_data.mags,
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth')
fig.show()
