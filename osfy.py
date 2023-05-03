#import the streamlit as st like anyother python lib, 
#after downloading streamlit in the same folder, 
#useing pip instal streamlit (in terminal), 
#test for successful working using streamlit hello(in terminal)
from email.mime import image
import streamlit as st
import pandas 
import numpy 
from PIL import Image

#save and run app in terminal(command prompt- streamlit run osfy.py) ,
#empty app runs in http://loaclhost:8510 , terminateapp with ctrl+c

st.title("Demo app for open source for you magazine")
st.header("Tutorial on streamlit")
st.subheader("building stunning UI with streamlit")


#rerun app in webpage after saving

st.success("This is a sample success message")
st.info("This is a smaple information message")
st.warning("this is a warning message")
st.error("This is an error message")

st.markdown('Streamlit is an **_Awesome_Library**.')

st.latex(r''' \frac{n!}{k!(n-k)!} = \binom{n}{k}''')

code ='''
st.title(“Demo App for Open Source For You Magazine”)
st.header(“Tutorial on Streamlit”)
st.subheader(“Buidling stunning UI with Streamlit”)
# These are various message types
st.success(“This is a sample success message”)
st.info(“This is a sample Information message”)
st.warning(“This is a Warning message”)
st.error(“This is an Error message ”)
st.markdown(‘Streamlit is an **_Awesome_ Library**.’)'''

st.code(code,language='python')

#import pandas and numpy in the file and in terminal using pip install
chart_data = pandas.DataFrame(
    numpy.random.randn(20,3),
    columns=['Team I', 'Team II', 'Team III'])

st.area_chart(chart_data)
st.bar_chart(chart_data)

#import Image from PIL

image = Image.open('mywindow.jpg')
st.image(image, caption='Rainy day', use_column_width=True)

#intercative button
if st.button("Click me"):
    st.success("successfully completed")

#interactive checkbix
sub = st.checkbox('I Would like to subscribe to OSFY Magazine')
if sub:
    st.write('Thanks for subscribing')

#radio buttons
lang = st.radio("Your Favourite Language", ('Python', 'Julia', 'Java'))

if lang == 'Python':
    st.write('you selected python')
if lang == 'Julia':
    st.write('you selected Julia')
if lang == 'Java':
    st.write('you selected java')
#dropdown selection box
city = st.selectbox('How would u like to be contacted', ('chennai','bangalore','hyderabad','delhi','mumbai','kolkata'))
st.write('you selected',city)

#multiselect using checkbox
options= st.multiselect('what are ur fav colours?', ['green','yellow','orange','blue','white','black'])
st.write('you selected',options)

#slider bar
level = st.slider('select your expertise level', 1,10,6)
st.write("you are at level:",level)


#number, textarea, text i/p

num=st.number_input('Enter a number')
txt=st.text_area("enter your feedback")
inp=st.text_input("Enter your name")

#sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you rate this page?",
    ("1 star","2 star","3 star","4 star","5 star")
)

#to get help information
st.help(st.line_chart)
