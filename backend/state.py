from typing_extensions import TypedDict, List

class MovieState(TypedDict):
    user_query: str
    intent: str
    movies: List[str]
    recommendations: List[str]
    explanation: str