def match_neighborhoods(data, preferences):
    scores = []
    for neighborhood in data:
        score = 0
        for key, weight in preferences.items():
            score += weight * int(neighborhood.get(key, 0))
        scores.append((neighborhood["name"], score))
    return sorted(scores, key=lambda x: x[1], reverse=True)[:5]
