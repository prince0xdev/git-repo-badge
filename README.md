
## Dynamic GitHub Repo Badge Generator (FastAPI + MongoDB)

A dynamic SVG badge generator for GitHub repositories that shows live view counts.
Built with Python FastAPI, MongoDB Atlas, and fully deployable on Vercel.

---

## 🚀 Features

* Dynamic counter for repository views
* Compact SVG style (similar to Shields.io)
* Customizable badge color via query parameter
* Self-hosted using Python **FastAPI**
* Ready for deployment on **Vercel**

---

## 🛠 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/princeOxdev/repo-badge.git
cd repo-badge
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

### 3. Setup environment variables

Create a `.env` file in the project root:

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
```

> **Important:** Never commit `.env` to GitHub. Add it to `.gitignore`.

### 4. Run the server locally

```bash
uvicorn main:app --reload
```

### 5. Access badges in browser

```
http://127.0.0.1:8000/badge/<username>/<repo>
```

Optional: customize the color:

```
http://127.0.0.1:8000/badge/<username>/<repo>?color=%23007ec6
```

---

## 📌 Embed in GitHub README

```markdown
![Repo Views](https://your-deployed-url.vercel.app/badge/<username>/<repo>?color=green)
```

> Example (local testing):
> ![Repo Views](http://127.0.0.1:8000/badge/prince0xdev/yt-downloader-gui?color=green)

---

## ⚡ Deployment on Vercel

1. Push your code to GitHub.
2. Create a project on [Vercel](https://vercel.com/) and link your repo.
3. Add **Environment Variables** on Vercel (`MONGO_URI`).
4. Deploy the project.
5. Your badge URL will be:

```
https://your-vercel-project.vercel.app/badge/<username>/<repo>
```

---

## 🔧 Customization

* Change badge width, height, or style directly in `main.py`.
* Add multiple badge styles (light/dark, flat, gradient).
* Implement caching for high-traffic repos.

---

## 📜 License

MIT License – free to use and modify.

---

Si tu veux, je peux te **préparer directement un `requirements.txt` + `.gitignore` + `.env.example`** pour que ton repo soit **prêt à push sur GitHub et Vercel** sans fuite de credentials.