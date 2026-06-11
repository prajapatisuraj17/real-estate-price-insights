import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
from style import add_custom_css


st.set_page_config(
    page_title='insights demo'
)

add_custom_css()

st.title('page 4')
st.header('BHK Upgrade Insights')
st.write('Use this page to understand how price changes when one feature or a full property configuration is upgraded.')


with open('pikle_files/model_artifacts.pkl', 'rb') as file:
    artifacts = pickle.load(file)

lr = artifacts['lr']
ss = artifacts['ss']
feature_cols = artifacts['feature_cols']


property_type_map = {
    'Apartment/Flat': 0,
    'independent_house/villa': 1
}

area_type_map = {
    'Carpet Area': 0,
    'Built-up Area': 1,
    'Super Built-up Area': 2
}


default_data = {
    'area': 650,
    'bedrooms': 1,
    'bathroom': 1,
    'property_type': 0,
    'area_type': 0
}


def predict_price(data):
    one_df = pd.DataFrame([data], columns=feature_cols)
    scaled_data = ss.transform(one_df)
    price = np.expm1(lr.predict(scaled_data))[0]
    return price


def show_value(feature, value):
    if feature == 'property_type':
        for key, val in property_type_map.items():
            if val == value:
                return key

    if feature == 'area_type':
        for key, val in area_type_map.items():
            if val == value:
                return key

    return value


def feature_input(feature, label, default_value):
    if feature == 'area':
        return st.number_input(label, min_value=100, value=int(default_value), step=50)

    if feature == 'bedrooms':
        values = [1, 2, 3, 4, 5]
        return st.selectbox(label, values, index=values.index(int(default_value)))

    if feature == 'bathroom':
        values = [1, 2, 3, 4, 5]
        return st.selectbox(label, values, index=values.index(int(default_value)))

    if feature == 'property_type':
        labels = list(property_type_map.keys())
        old_label = show_value(feature, default_value)
        return property_type_map[st.selectbox(label, labels, index=labels.index(old_label))]

    if feature == 'area_type':
        labels = list(area_type_map.keys())
        old_label = show_value(feature, default_value)
        return area_type_map[st.selectbox(label, labels, index=labels.index(old_label))]


st.write('Compare full property upgrade or check price change from only one feature.')

compare_type = st.radio(
    'Select Insight Type',
    ['One Feature Only', 'Full Property Comparison'],
    horizontal=True
)


if compare_type == 'One Feature Only':
    st.subheader('Single Feature Price Impact')
    st.write('Change only one selected feature. All other features are filled with default values.')

    feature = st.selectbox(
        'Which feature do you want to check?',
        ['bedrooms', 'area', 'bathroom', 'property_type', 'area_type']
    )

    col1, col2 = st.columns(2)

    with col1:
        from_value = feature_input(feature, 'From Value', default_data[feature])

    with col2:
        to_default = default_data[feature]
        if feature == 'bedrooms':
            to_default = 2
        elif feature == 'area':
            to_default = 1000
        elif feature == 'bathroom':
            to_default = 2
        elif feature == 'property_type':
            to_default = 1
        elif feature == 'area_type':
            to_default = 1

        to_value = feature_input(feature, 'To Value', to_default)

    st.write('Other features are automatically taken as default values:')
    st.write(default_data)

    if st.button('Check Impact'):
        from_data = default_data.copy()
        to_data = default_data.copy()

        from_data[feature] = from_value
        to_data[feature] = to_value

        from_price = predict_price(from_data)
        to_price = predict_price(to_data)

        increase = to_price - from_price
        increase_per = (increase / from_price) * 100

        st.success(f'Base Price: {from_price:.2f} Cr')
        st.success(f'Changed Price: {to_price:.2f} Cr')
        st.info(f'{feature} impact: {increase:.2f} Cr ({increase_per:.2f}%)')

        result_df = pd.DataFrame(
            [[feature, show_value(feature, from_value), show_value(feature, to_value), increase, increase_per]],
            columns=['Feature', 'From', 'To', 'Price Increase', 'Increase %']
        )

        st.dataframe(result_df, use_container_width=True)

        fig = px.bar(
            result_df,
            x='Feature',
            y='Price Increase',
            text='Price Increase',
            title='Selected Feature Price Impact'
        )
        st.plotly_chart(fig, use_container_width=True)

    st.stop()


st.subheader('Full Property Upgrade Comparison')
st.write('Compare current and upgraded property details to see total and feature-wise price increase.')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Current Property')
    from_bhk = st.selectbox('From BHK', [1, 2, 3, 4], index=0)
    from_area = st.number_input('From Area', min_value=100, value=650, step=50)
    from_bathroom = st.selectbox('From Bathroom', [1, 2, 3, 4, 5], index=0)
    from_property_type = st.selectbox('From Property Type', list(property_type_map.keys()))
    from_area_type = st.selectbox('From Area Type', list(area_type_map.keys()))

with col2:
    st.subheader('Upgraded Property')
    to_bhk = st.selectbox('To BHK', [1, 2, 3, 4, 5], index=1)
    to_area = st.number_input('To Area', min_value=100, value=1000, step=50)
    to_bathroom = st.selectbox('To Bathroom', [1, 2, 3, 4, 5], index=1)
    to_property_type = st.selectbox('To Property Type', list(property_type_map.keys()))
    to_area_type = st.selectbox('To Area Type', list(area_type_map.keys()))


if st.button('Compare'):
    if to_bhk <= from_bhk:
        st.error('To BHK should be greater than From BHK.')
        st.stop()

    from_data = {
        'area': from_area,
        'bedrooms': from_bhk,
        'bathroom': from_bathroom,
        'property_type': property_type_map[from_property_type],
        'area_type': area_type_map[from_area_type]
    }

    to_data = {
        'area': to_area,
        'bedrooms': to_bhk,
        'bathroom': to_bathroom,
        'property_type': property_type_map[to_property_type],
        'area_type': area_type_map[to_area_type]
    }

    from_price = predict_price(from_data)
    to_price = predict_price(to_data)

    increase = to_price - from_price
    increase_per = (increase / from_price) * 100

    st.success(f'Current Price: {from_price:.2f} Cr')
    st.success(f'Upgraded Price: {to_price:.2f} Cr')
    st.info(f'Price Increase: {increase:.2f} Cr ({increase_per:.2f}%)')

    rows = []
    temp_data = from_data.copy()
    old_price = from_price

    for col in feature_cols:
        before = temp_data[col]
        temp_data[col] = to_data[col]

        new_price = predict_price(temp_data)
        impact = new_price - old_price

        rows.append([col, before, to_data[col], impact, (impact / from_price) * 100])

        old_price = new_price

    result_df = pd.DataFrame(
        rows,
        columns=['Feature', 'From', 'To', 'Price Increase', 'Increase %']
    )

    st.subheader('Feature Wise Comparison')
    st.write('This table shows how each feature contributes to the total estimated price change.')
    st.dataframe(result_df, use_container_width=True)

    fig = px.bar(
        result_df,
        x='Feature',
        y='Price Increase',
        text='Price Increase',
        title='How much each feature increases price'
    )
    st.plotly_chart(fig, use_container_width=True)
