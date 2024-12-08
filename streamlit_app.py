import streamlit as st

hello_world = st.Page("hello_world.py", title="Hello World Example", icon=":material/waving_hand:")
bank_support = st.Page("bank_support.py", title="Bank support", icon=":material/account_balance:")

pg = st.navigation([hello_world, bank_support])

st.set_page_config(page_title="Pydantic WebUI", page_icon=":robot_face:")
pg.run()