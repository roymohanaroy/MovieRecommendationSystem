import streamlit as st
import requests

st.title("AI Movie Recommender")

query = st.text_input("What kind of movie do you want?")

if st.button("Recommend"):
    print("----------inside------------")
    response = requests.post(
        "http://localhost:8000/recommend",
        json={"user_query": query}
    )

    data = response.json()

    st.subheader("Recommended Movies")

    for movie in data["recommendations"]:
        st.write(movie)

    st.subheader("Why these movies?")
    st.write(data["explanation"])