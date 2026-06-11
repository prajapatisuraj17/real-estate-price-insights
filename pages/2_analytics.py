import streamlit as st
import plotly.express as px
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from style import add_custom_css
st.set_page_config(
    page_title='viz demo'
)

add_custom_css()

st.title('page 2')
st.write('Explore real estate trends using location, area, price, and property type visualizations.')

with open('pikle_files/loc_df.pkl','rb') as file:
    location=pickle.load(file)
#st.dataframe(location)
df=pd.read_csv('datasets/perfect_df.csv')

group_df=location.groupby('locality')[['price','area','price_per_sqft','Latitude','Longitude']].mean()

st.header('Location-wise Price per Sqft Map')
st.write('This map shows each locality with color based on average price per sqft and size based on average area.')
fig = px.scatter_mapbox(
    group_df,
    lat="Latitude",
    lon="Longitude",
    color="price_per_sqft",
    size='area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index
)
st.plotly_chart(fig,use_container_width=True)

st.header('Area vs Price by BHK')
st.write('This chart compares property area and price. Color shows the number of bedrooms.')

property_type=st.selectbox('Select Property _type',['Flat','House'])
if property_type=='Flat':
            fig1=px.scatter(df[df['property_type']=='flat'],x='area',y='price',color='bedrooms',title='Flat Area vs Price')
            st.plotly_chart(fig1,use_container_width=True)
else:
            fig1=px.scatter(df[df['property_type']=='house'],x='area',y='price',color='bedrooms',title='House Area vs Price')
            st.plotly_chart(fig1,use_container_width=True)            

st.header('Price Distribution by Property Type')
st.write('This distribution compares price spread for houses and flats.')
fig4=plt.figure(figsize=(10,4))
sns.distplot(df[df['property_type'] == 'house']['price'],label='house')
sns.distplot(df[df['property_type'] == 'flat']['price'],label='flat')
plt.legend()
st.pyplot(fig4) 

