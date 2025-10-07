# Repo Badge - FastAPI

This project is a **dynamic SVG badge generator** for GitHub repositories, showing the number of views for each repository.  

The badge can be embedded in your README file or shared publicly.

## Features

- Dynamic counter for repository views
- Compact SVG style (Shields.io style)
- Customizable badge color via query parameter
- Self-hosted using Python FastAPI
- Ready for Vercel deployment

## Usage

### Local

1. Install dependencies:

```bash
pip install fastapi uvicorn
```
Run the server:

uvicorn main:app --reload


## Open in browser:

    http://127.0.0.1:8000/badge/<username>/<repo>

- (With color parameter
http://127.0.0.1:8000/badge/<username>/<repo>?color=%23007ec6)

## Embed in GitHub README
 
![Repo Views]            (http://127.0.0.1:8000/badge/prince0xdev/yt-downloader-guit?color=green)