import streamlit as st
import pickle
import pandas as pd
import numpy as np
from style import add_custom_css

st.set_page_config(
    page_title='ploting demo'
)

add_custom_css()

st.title('page 1')
st.write('Predict the estimated property price by entering the required property details.')

with open('pikle_files/df.pkl','rb') as file:
    df=pickle.load(file)
#st.dataframe(df)
with open('pikle_files/pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)

st.header('Property Price Prediction Input')

select_placeholder='-- Select --'

locality=st.selectbox('Choose Location',[select_placeholder]+df['locality'].unique().tolist())
property_type=st.selectbox('Property_Type',[select_placeholder,'Flat','House'])
bedroom=st.selectbox('Bedroom',[select_placeholder]+sorted(df['bedrooms'].unique().tolist()))
bathroom=st.selectbox('Bathroom',[select_placeholder]+sorted(df['bathroom'].unique().tolist()))
floor_cat=st.selectbox('Floor_Type',[select_placeholder]+sorted(df['floor_number'].unique().tolist()))
area_type=st.selectbox('Area_Type',[select_placeholder]+sorted(df['area_type'].unique().tolist()))
property_age=st.selectbox('Property_Age',[select_placeholder]+sorted(df['property_age'].unique().tolist())) 

area=int(st.number_input('Area',min_value=0,value=0,step=1))   


if st.button('Predict'):
    errors=[]

    if locality == select_placeholder:
        errors.append('Please choose a location.')
    if property_type == select_placeholder:
        errors.append('Please choose a property type.')
    if bedroom == select_placeholder:
        errors.append('Please choose bedroom count.')
    if bathroom == select_placeholder:
        errors.append('Please choose bathroom count.')
    if floor_cat == select_placeholder:
        errors.append('Please choose floor type.')
    if area_type == select_placeholder:
        errors.append('Please choose area type.')
    if property_age == select_placeholder:
        errors.append('Please choose property age.')
    if area <= 0:
        errors.append('Area must be greater than 0.')

    if errors:
        for error in errors:
            st.error(error)
        st.stop()

    bedroom=float(bedroom)
    bathroom=int(bathroom)

    # form a dataframe
    data=[[property_type,bedroom,bathroom,floor_cat,area_type,property_age,area,locality]]

    columns=['property_type','bedrooms','bathroom','floor_number',
             'area_type','property_age','area','locality']

    one_df=pd.DataFrame(data,columns=columns)

    st.dataframe(one_df)

    # predict
    pred_value = np.expm1(pipeline.predict(one_df))[0]

    # display
    st.success(f"The Price Of the independent_house/villa is {pred_value:.2f} Cr")
