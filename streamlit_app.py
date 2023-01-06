import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
#Ask user for fruit input and use it to define json
streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()




#Don't run anything past here while we troubleshoot
streamlit.stop()

#Snowflake connector: 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()

#Display results table
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)

#Ask user for fruit input and use it to define json
add_my_fruit = streamlit.text_input('What fruit would you like more information about',' ')
streamlit.write('Thanks for adding ', add_my_fruit)

#Adding data to snowflake
my_cur.execute("insert into fruit_load_list values ('from streamlit')")





