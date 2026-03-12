from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import pandas as pd
import os
from dotenv import load_dotenv
import json
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini")

def intent_agent(state):

    prompt = f"""
    Return  only the movie genre from the user's query."{state['user_query']}"
    
    
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    
    state["intent"]=response.content
    return state


movies = pd.read_csv("backend/movie_data.csv")

def search_agent(state):

    intent = state["intent"]
    print("----intent----",intent)
    #intent="superhero"
    #results = movies[movies["genre"].str.lower().str.contains(intent)]["title"]
    
    
    results = movies[
        movies["genre"].str.contains(intent)
    ]["title"].tolist()   
    print("--------resukts-----",results)
   
    return {"movies": results}

def similarity_agent(state):

    movies = state["movies"]
     
    recommendations = movies[:3]

    return {"recommendations": recommendations}

def explanation_agent(state):

    recs = ", ".join(state["recommendations"])

    explanation = f"""
    These movies are recommended because they match your interest
    in {state['intent']} movies.
    """

    return {"explanation": explanation}