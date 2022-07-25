import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Use Command Prompt instead of PowerShell to run the py file

st.set_page_config(page_title="Most Popular Languages for Data Professionals", page_icon="👨‍💻", layout="wide")

st.markdown("# Most Popular Languages for Data Professionals")
st.markdown("---")

with st.sidebar:
    data_role = st.radio("Choose data role: ",
                         ("Data Scientist", "Data Analyst", "Data Engineer", "Database Administrator"))
    number_lang = st.slider("Choose number of languages: ", 1, 10, 5)
    st.markdown("---")
    st.markdown("Created by Timotius Marselo")
    st.markdown("Source code for the data analysis and visualization steps is available on [my website](https://tmtsmrsl.github.io/project02.html).")

# Data source

normalize_df = pd.read_csv(
    "https://raw.githubusercontent.com/tmtsmrsl/popular_languages/main/streamlit/normalized_popular_language.csv")
normalize_df = normalize_df.set_index("Unnamed: 0")
normalize_df.index.name = None

top_df = normalize_df[[data_role, "Color"]].sort_values(data_role, ascending=False)[:number_lang].sort_index()

top_df.columns = ["Total", "Color"]

# Visualization

fig = go.Figure(go.Barpolar(
    r=top_df["Total"],
    theta=top_df.index,
    width=0.45,
    marker_color=top_df["Color"],
    marker_line_color="black",
    marker_line_width=2,
    opacity=0.7
))

fig.update_traces(hovertemplate='%{theta}: %{r:.0%}<extra></extra>')

fig.update_layout(
    title="Top {} Languages for {}".format(number_lang, data_role),
    font_color="darkblue",
    font_family="Tahoma",
    font_size=18,
    title_font_color="darkblue",
    title_font_family="Tahoma",
    title_font_size=24,
    paper_bgcolor='#DEDCC6',
    height=500,
    width=500,
    template="ggplot2",
    polar=dict(
        radialaxis=dict(range=[0, 1.0], showline=False, showticklabels=False, ticks=''),
        angularaxis=dict(showticklabels=True, ticks='', linecolor='black', linewidth=1.5)
    )
)

blank1, chart, blank2 = st.columns([1,5,1])
with chart:
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""Hover over the chart to see the percentage of {} that have worked with the corresponding language. 
                Data are based on Stack Overflow Developer Survey 2021 results.""".format(data_role))
st.markdown("""Here are some key points from the visualization above:  
                - Data scientist, data analyst, and data engineer have similarity in which Python is the most used language followed by SQL.  
                - For database administrator, SQL is the most used language followed by Python.  
                - Java is quite popular among all data professionals, although not as popular as Python and SQL.  
                **- Learn Python and SQL if you want to have a data-related career.**""")
