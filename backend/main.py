from backend.matching import match_neighborhoods
from backend.data_loader import load_data

def run_backend(user_preferences):
    data = load_data()
    recommendations = match_neighborhoods(data, user_preferences)
    return recommendations
