# CUSTOMER LIFETIME VALUE ANALYSIS

import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Reading the csv file
data = pd.read_csv(r"C:\Users\rajve\Downloads\customer_acquisition_data.csv")

# Displaying  first five rows of data
print(data.head())


# Distribution of customer acquisition data
fig = px.histogram(data , x='cost',nbins=20,title='Distribution of Acquisition Cost')
fig.show()


#Cost revenue genrated by the customers
fig = px.histogram(data,x='revenue',nbins=20,title='Distribution of Revenue')
fig.show()


# Channel is More Profitable
cost_by = data.groupby('channel')['cost'].mean().reset_index()
fig = px.bar(cost_by,x='channel',y='cost',title="Customer Acquisation cost by channel")
fig.show()


# Conversion By channel
conversion_by = data.groupby('channel')['conversion_rate'].mean().reset_index()
fig = px.bar(conversion_by,x='channel',y='conversion_rate',title='Conversion rate by channel')
fig.show()

# Calculate total revenue by channel and profitable channel genrating revnues
revenue_by = data.groupby('channel')['revenue'].sum().reset_index()
fig = px.pie(revenue_by,values='revenue',names='channel',title='Total Revenue Genrated By channel')
fig.show()

# return on investment (ROI)
data['roi'] = data['revenue']/data['cost']
roi_by = data.groupby('channel')['roi'].mean().reset_index()
fig = px.bar(roi_by,x='channel',y='roi',title='Return on Investment (ROI) by channel')
fig.show()
