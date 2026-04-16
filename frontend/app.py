import streamlit as st
import requests

st.title("AI Movie Recommender")

query = st.text_input("What kind of movie do you want?")

if st.button("Recommend"):
    response = requests.post(
    "https://movierecommendationsystem-l3vs.onrender.com/recommend",
    json={"user_query": query}
)

    st.write("Status Code:", response.status_code)
    st.write("Response Text:", response.text)

    # Only parse JSON if valid
    if response.headers.get("content-type", "").startswith("application/json"):
        data = response.json()

        st.subheader("Recommended Movies")
        for movie in data.get("recommendations", []):
            st.write(movie)

        st.subheader("Why these movies?")
        st.write(data.get("explanation", "No explanation provided"))
    else:
        st.error("Backend did NOT return JSON")