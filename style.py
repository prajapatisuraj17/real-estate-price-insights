import streamlit as st


def add_custom_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --bg: #f7faf8;
            --panel: #ffffff;
            --text: #17211d;
            --muted: #66736d;
            --accent: #0f766e;
            --accent-2: #d97706;
            --border: #dce7e2;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(15, 118, 110, 0.10), transparent 34rem),
                linear-gradient(180deg, #f7faf8 0%, #eef6f2 100%);
            color: var(--text);
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        section[data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid var(--border);
        }

        h1 {
            color: var(--text);
            font-size: 2.3rem !important;
            font-weight: 800 !important;
            padding-bottom: 0.2rem;
        }

        h2, h3 {
            color: #21332d;
            font-weight: 700 !important;
        }

        p, label, .stMarkdown {
            color: var(--text);
        }

        div[data-testid="stSelectbox"],
        div[data-testid="stNumberInput"],
        div[data-testid="stTextInput"] {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.55rem 0.7rem;
            box-shadow: 0 8px 22px rgba(23, 33, 29, 0.04);
        }

        div[data-testid="stMetric"] {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 12px 28px rgba(23, 33, 29, 0.07);
        }

        div[data-testid="stDataFrame"],
        div[data-testid="stTable"],
        div[data-testid="stPlotlyChart"],
        div[data-testid="stPyplot"] {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.7rem;
            box-shadow: 0 12px 28px rgba(23, 33, 29, 0.06);
        }

        .stButton > button {
            background: linear-gradient(135deg, var(--accent), #159b8e);
            color: #ffffff;
            border: 0;
            border-radius: 8px;
            padding: 0.6rem 1.1rem;
            font-weight: 700;
            box-shadow: 0 10px 22px rgba(15, 118, 110, 0.25);
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #0b615a, var(--accent));
            color: #ffffff;
            border: 0;
        }

        div[data-testid="stAlert"] {
            border-radius: 8px;
            border: 1px solid rgba(15, 118, 110, 0.18);
        }

        hr {
            border-color: var(--border);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
