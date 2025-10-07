from fastapi import FastAPI, Response, Query
from pymongo import MongoClient
import os
import logging

# --- Logging simple ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
client = None
collection = None


def get_db():
    global client, collection
    if client is None:
        try:
            client = MongoClient(os.getenv("MONGO_URI"), serverSelectionTimeoutMS=5000)
            db = client["viewsDB"]
            collection = db["repos"]
            logger.info("✅ Connexion MongoDB réussie")
        except Exception as e:
            logger.error("❌ Erreur connexion MongoDB: %s", e)
            raise e
    return collection


@app.get("/badge/{user}/{repo}")
def badge(user: str, repo: str, color: str = Query("#28a745")):
    key = f"{user}/{repo}"

    try:
        coll = get_db()  # Utiliser la connexion ici
        entry = coll.find_one({"repo": key})
        if entry and "views" in entry:
            views = entry["views"] + 1
            coll.update_one({"repo": key}, {"$set": {"views": views}})
        else:
            views = 1
            coll.update_one({"repo": key}, {"$set": {"views": views}}, upsert=True)

        # Génération du badge SVG
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

    except Exception as e:
        logger.error("❌ Erreur badge pour %s: %s", key, e)
        error_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="90" height="20">
  <rect width="90" height="20" fill="#e05d44"/>
  <text x="45" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">
    ERROR
  </text>
</svg>
"""
        return Response(content=error_svg, media_type="image/svg+xml", status_code=500)
