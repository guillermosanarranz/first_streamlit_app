import streamlit
import pandas

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('🐔 Eggs & Bacon')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.text('🥣 Yogurt & Berries')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Read csv and convert list to fruit names
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))


# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)







