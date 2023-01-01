import streamlit
import pandas as pd

fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits.set_index('Fruit', inplace=True)
streamlit.dataframe(fruits_to_show)

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach, and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')

streamlit.header('Build Your Own Fruit Smoothie')
fruit_selected = streamlit.multiselect("Pick some fruits:", list(fruits.index), ['Avocado', 'Strawberries'])
fruits_to_show = fruits.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)
