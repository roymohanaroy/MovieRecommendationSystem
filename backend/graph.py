from langgraph.graph import StateGraph, START, END
from backend.state import MovieState
from backend.agents import intent_agent, search_agent, similarity_agent, explanation_agent

builder = StateGraph(MovieState)

builder.add_node("intent", intent_agent)
builder.add_node("search", search_agent)
builder.add_node("similarity", similarity_agent)
builder.add_node("explain", explanation_agent)

builder.add_edge(START, "intent")
builder.add_edge("intent", "search")
builder.add_edge("search", "similarity")
builder.add_edge("similarity", "explain")
builder.add_edge("explain", END)

graph = builder.compile()