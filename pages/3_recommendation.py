import streamlit as st
import plotly.express as px
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from style import add_custom_css


st.set_page_config(
    page_title='Recommend Apartment'
)

add_custom_css()

df=pickle.load(open('pikle_files/location_df.pkl','rb'))
cosine_sim1=pickle.load(open('pikle_files/cosine_sim1.pkl','rb'))
cosine_sim2=pickle.load(open('pikle_files/cosine_sim2.pkl','rb'))
cosine_sim3=pickle.load(open('pikle_files/cosine_sim3.pkl','rb'))

def recommend_properties_with_scores(property_name, top_n=247):
    
    cosine_sim_matrix = 0.8*cosine_sim1 + 0.6*cosine_sim2 + 1*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df.head(5)

# Test the recommender function using a property name
recommend_properties_with_scores('Sobha City')


st.title('Location and Apartment Recommendation')
st.write('Find nearby apartments within a selected radius and get similar apartment recommendations.')

st.header('Nearby Property Search')
st.write('Select a location and radius to see properties available nearby.')
selected_location=st.selectbox('Select Location',df.columns.to_list())
radius=st.number_input('Radius in KM')

if st.button('Search'):
    result_str=df[df[selected_location]<radius*1000][selected_location].sort_values().to_dict()
    for i,j in result_str.items():
        st.text(str(i)+ '->' + str(round(j/1000))+'km')

st.header('Similar Apartment Recommendation')
st.write('Select an apartment to view similar properties based on distance and similarity scores.')
selected_apartment=st.selectbox('Select Apartment',df.index.to_list()) 

if  st.button('Search_Recommendation'):
    result=recommend_properties_with_scores(selected_apartment)
    st.dataframe(result)
  
