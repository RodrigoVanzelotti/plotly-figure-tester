from plotly_figure_tester import PlotlyFigureTester
import plotly.express as px

Tester = PlotlyFigureTester()

df1 = px.data.iris()
fig1 = px.scatter(df1, x="sepal_width", y="sepal_length", color="species")

df2 = px.data.tips()
fig2 = px.bar(df2, x="day", y="total_bill", color="sex")

Tester.add_chart(fig1, label="Iris Dataset")
Tester.add_chart(fig2, label="Tips Dataset")

Tester.run_server()