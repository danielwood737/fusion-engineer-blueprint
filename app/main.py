from pathlib import Path
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "quests.json"

app = FastAPI(title="Fusion Engineer Blueprint")
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")


def load_quests() -> list[dict]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    quests = load_quests()
    completed = sum(1 for quest in quests if quest["status"] == "Complete")
    total_xp = sum(quest["xp"] for quest in quests if quest["status"] == "Complete")
    level = total_xp // 500 + 1
    progress = round((completed / len(quests)) * 100) if quests else 0

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "quests": quests,
            "completed": completed,
            "total": len(quests),
            "total_xp": total_xp,
            "level": level,
            "progress": progress,
            "name": "Daniel",
        },
    )
