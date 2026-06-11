import streamlit as st
from style import add_custom_css

st.set_page_config(
    page_title='Hello',
    page_icon='##'
)

add_custom_css()

st.title('Real Estate Price Intelligence')
st.write(
    'This project helps users explore real estate prices, predict property value, '
    'analyze location trends, get similar apartment recommendations, and understand '
    'how price changes when property features are upgraded.'
)

st.header('Project Modules')
st.write('Price Predictor: estimate property price from location, area, BHK, bathroom, floor, age, and property type.')
st.write('Analytics: view location-wise price patterns, area vs price behavior, and property type distribution.')
st.write('Recommendation: find nearby properties and similar apartments based on selected property or location.')
st.write('Insights: compare feature changes such as 1 BHK to 2 BHK and see estimated price impact.')

st.info('Use the sidebar to open any module.')
st.sidebar.success('select demo')
