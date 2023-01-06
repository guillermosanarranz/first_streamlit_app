import streamlit
import pandas
import snowflake.connector

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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#JSON
import requests

#Ask user for fruit input and use it to define json
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.header("Fruityvice Fruit Advice!")

#Convert json to pandas df
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#Show new pandas df
streamlit.dataframe(fruityvice_normalized)

#Snowflake connection: database context
'''
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
'''

#Snowflake connector: 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.text(my_data_row)





