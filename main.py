from fastapi import FastAPI, Response, Query
import json
import os

app = FastAPI()

DATA_FILE = os.path.join(os.path.dirname(__file__), "views.json")

# Créer le fichier si inexistant
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def get_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.get("/badge/{user}/{repo}")
def badge(user: str, repo: str, color: str = Query("#28a745")):
    data = get_data()
    key = f"{user}/{repo}"
    data[key] = data.get(key, 0) + 1
    save_data(data)
    views = data[key]

    # Badge SVG compact + paramètre couleur
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="90" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="90" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <rect width="55" height="20" fill="#555"/>
    <rect x="55" width="35" height="20" fill="{color}"/>
    <rect width="90" height="20" fill="url(#b)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">
    <text x="27" y="14" fill="#010101" fill-opacity=".3">views</text>
    <text x="27" y="13">views</text>
    <text x="72" y="14" fill="#010101" fill-opacity=".3">{views}</text>
    <text x="72" y="13">{views}</text>
  </g>
</svg>
"""
    return Response(content=svg, media_type="image/svg+xml")
