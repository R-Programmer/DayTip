import datetime
import random
import streamlit as st

tips=['never say “ I can’t😒 “ always say “I’ll try😊”.',
         'don’t let your dreams ... \n be dreams💤.',
         ' nothing changes \n if nothing changes.',
         'work hard in silence, let success make the noise💥.',
         'whatever you do, [do it well].']
today= datetime.datetime.today().strftime('%d %m %Y')
message=random.choice(tips)
st.title('Tip of the day💡:')
st.write('Date: {today}')
st.subheader(message)
if st.button('Get another tip'):
    newMessage=random.choice(tips)
    st.subheader(newMessage)



