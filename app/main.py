from pathlib import Path
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "quests.json"
MISSION = (
    "Contribute to the commercialization of fusion energy "
    "by developing technologies that make fusion power "
    "practical, efficient, and scalable."
)
app = FastAPI(title="Fusion Engineer Blueprint")
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")


def load_quests() -> list[dict]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)
def save_quests(quests: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(quests, file, indent=2)
def get_title(level: int) -> str:
    if level == 1:
        return "Programming Beginner"
    elif level == 2:
        return "Programming Apprentice"
    elif level == 3:
        return "Engineering Student"
    elif level == 4:
        return "Engineering Apprentice"
    elif level == 5:
        return "Nuclear Engineering Scholar"
    elif level == 6:
        return "Simulation Apprentice"
    elif level == 7:
        return "Research Candidate"
    elif level == 8:
        return "Fusion Candidate"
    elif level == 9:
        return "National Lab Candidate"
    else:
        return "Fusion Systems Engineer"

@app.post("/quests/{quest_id}/complete")
def complete_quest(quest_id: str):
    quests = load_quests()
    for quest in quests:
        if quest["id"] == quest_id:
            quest["status"] = "Complete"
            break
    save_quests(quests)
    return RedirectResponse(url="/", status_code=303)

@app.post("/quests/{quest_id}/reopen")
def reopen_quest(quest_id: str):
    quests = load_quests()
    for quest in quests:
        if quest["id"] == quest_id:
            quest["status"] = "Not Started"
            break
    save_quests(quests)
    return RedirectResponse(url="/", status_code=303)

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    quests = load_quests()
    completed = sum(1 for quest in quests if quest["status"] == "Complete")
    total_xp = sum(quest["xp"] for quest in quests if quest["status"] == "Complete")
    level = total_xp // 500 + 1
    title = get_title(level)
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
            "mission": MISSION,
            "title": title,
        },
    )
