import streamlit as st

pg = st.navigation([
    st.Page("hello_world.py"),
    ])
st.set_page_config(page_title="Pydantic WebUI", page_icon=":robot_face:")
pg.run()