response = requests.post(
    "https://movierecommendationsystem-l3vs.onrender.com/recommend",
    json={"user_query": query}
)

if response.status_code != 200:
    st.error(f"Error: {response.status_code}")
    st.text(response.text)
else:
    try:
        data = response.json()

        st.subheader("Recommended Movies")
        for movie in data.get("recommendations", []):
            st.write(movie)

        st.subheader("Why these movies?")
        st.write(data.get("explanation", "No explanation provided"))

    except Exception:
        st.error("Invalid JSON response")
        st.text(response.text)