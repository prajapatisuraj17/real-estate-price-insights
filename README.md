# Real Estate Price Insights

A Streamlit-based real estate analytics project that helps users predict property prices, explore market trends, find similar apartments, and understand how feature upgrades affect estimated price.

## Features

- **Price Predictor**: Predicts property price using inputs such as location, area, BHK, bathroom, floor type, property age, area type, and property type.
- **Analytics Dashboard**: Shows location-wise price patterns, area vs price trends, and property type price distribution.
- **Recommendation System**: Recommends nearby and similar apartments based on selected location or apartment.
- **Upgrade Insights**: Compares property feature changes, such as 1 BHK to 2 BHK, and shows feature-wise price impact using a Linear Regression model.

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn

## Project Structure

```text
Capstone_Streamlit/
|-- home.py
|-- style.py
|-- pages/
|   |-- 1_price_predictor.py
|   |-- 2_analytics.py
|   |-- 3_recommendation.py
|   `-- 4_insights.py
|-- datasets/
|   `-- project data files
|-- pikle_files/
|   `-- trained models and similarity files
|-- .streamlit/
|   `-- config.toml
`-- README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/real-estate-price-insights.git
cd real-estate-price-insights
```

2. Install required libraries:

```bash
pip install streamlit pandas numpy scikit-learn plotly matplotlib seaborn
```

3. Run the Streamlit app:

```bash
streamlit run home.py
```

4. Open the local URL shown in the terminal.

## Dataset and Model Files

The app uses prepared dataset files from the `datasets/` folder and trained model files from the `pikle_files/` folder. These files are required for prediction, analytics, recommendation, and insight modules.

## Modules

### Price Predictor

Takes property details from the user and predicts the estimated property price in crore.

### Analytics

Displays real estate visualizations such as:

- Location-wise price per sqft map
- Area vs price comparison
- Price distribution by property type

### Recommendation

Helps users find:

- Properties near a selected location within a given radius
- Similar apartments based on similarity scores

### Insights

Allows users to compare:

- One selected feature only
- Full property upgrade configuration

It shows the estimated price increase and feature-wise impact.

## Future Improvements

- Add more advanced filters for locality and budget.
- Improve model accuracy with more training data.
- Add user-friendly charts for model explanation.
- Deploy the app on Streamlit Community Cloud.

## Author

Created as a real estate capstone project using machine learning and Streamlit.
