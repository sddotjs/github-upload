
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = make_subplots(
    rows = 2, cols = 1,
    column_widths = [0.4, 0.4],
    specs = [[{'type': 'treemap', 'rowspan': 2}, {'type': 'treemap'}]]
)

fig.add_trace(
    go.Treemap(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents),
    col = 1, row = 1)

fig.add_trace(
    go.Treemap(
        ids = df2.ids,
        labels = df2.labels,
        parents = df2.parents,
        maxdepth = 3),
    col = 1, row = 2)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

#app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
if __name__ == '__main__':
    app.run_server(debug=True)
