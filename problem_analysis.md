# 🧠 Problem Analysis & Research – NeighborFit

## 🏠 Problem Definition
Many individuals struggle to find a neighborhood that matches their lifestyle — be it safety, schools, nightlife, or green space. The decision is often based on vague impressions or incomplete data. NeighborFit solves this by recommending neighborhoods based on user preferences using a lightweight scoring algorithm.

## 💡 Hypotheses
1. Users who prioritize **parks** are also likely to value **safety**.
2. People moving with families care more about **school ratings** than **nightlife**.
3. A simple scoring algorithm using weighted preferences is sufficient for a first-level match.

## 🔍 Existing Solutions & Gaps
| Platform       | Strengths                            | Gaps                                   |
|----------------|---------------------------------------|----------------------------------------|
| WalkScore      | Real-time walk, transit, bike scores | No personalized matching or filtering  |
| Niche.com      | School and neighborhood ratings      | Static data, limited user interaction  |
| Realtor.com    | Home search filters                  | No lifestyle-based suggestions         |

## ⚖️ Design Trade-offs
- **CSV vs Database**: Chose CSV for simplicity and offline support. Can scale to DB later.
- **No login**: Prioritized simplicity; can add auth if app scales.
- **Streamlit UI**: Great for quick deployment and input/output controls.

## 🔄 Future Enhancements
- Integrate live data from public APIs (e.g., OpenStreetMap, WalkScore API)
- Add user registration + preference history
- Visualize on interactive map
- Use machine learning for more accurate match prediction
