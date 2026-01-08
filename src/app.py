"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the basketball team and compete in local tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer Club": {
        "description": "Practice soccer skills and participate in matches",
        "schedule": "Tuesdays and Thursdays, 5:00 PM - 7:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Art Club": {
        "description": "Explore various art techniques and create projects",
        "schedule": "Fridays, 3:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Participate in theater productions and improve acting skills",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Debate Team": {
        "description": "Engage in debates and improve public speaking skills",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    "Math Club": {
        "description": "Solve challenging math problems and participate in competitions",
        "schedule": "Tuesdays, 3:00 PM - 4:30 PM",
        "max_participants": 10,
        "participants": []
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Additional sports activities
    "Swimming Team": {
        "description": "Train and compete in swimming events",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Tennis Club": {
        "description": "Learn tennis skills and play friendly matches",
        "schedule": "Wednesdays, 5:00 PM - 6:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Volleyball Team": {
        "description": "Practice volleyball and compete in inter-school tournaments",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 14,
        "participants": []
    },
    "Track and Field": {
        "description": "Train for running, jumping, and throwing events",
        "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    # Additional artistic activities
    "Photography Club": {
        "description": "Explore photography techniques and participate in photo walks",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Music Band": {
        "description": "Join the school band and perform at events",
        "schedule": "Thursdays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": []
    },
    "Dance Crew": {
        "description": "Learn and perform various dance styles at school events",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Creative Writing Club": {
        "description": "Write stories, poems, and participate in writing contests",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    # Additional intellectual activities
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Robotics Club": {
        "description": "Build robots and compete in robotics competitions",
        "schedule": "Mondays, 4:00 PM - 6:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Quiz Bowl": {
        "description": "Compete in academic quiz competitions covering various subjects",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Astronomy Club": {
        "description": "Explore the universe through telescopes and discussions",
        "schedule": "Fridays, 5:30 PM - 7:00 PM",
        "max_participants": 15,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    # Validate student is not already signed up

    
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
