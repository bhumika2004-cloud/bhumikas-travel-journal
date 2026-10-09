import sqlite3
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from extract_gps import extract_location

app = FastAPI(title="Automated Travel Map API")

# Initialize SQLite Database Table
def init_db():
    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            location_name TEXT NOT NULL,
            date_taken TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Serve static HTML files from the /static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/api/locations")
def get_locations():
    """Retrieve all stored travel markers from the database."""
    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, latitude, longitude, location_name, date_taken FROM locations")
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "latitude": r[1],
            "longitude": r[2],
            "location_name": r[3],
            "date_taken": r[4]
        }
        for r in rows
    ]

@app.post("/api/upload")
async def upload_photo(file: UploadFile = File(...)):
    """Upload a travel photo, extract GPS data automatically, and store in DB."""
    extracted_data = extract_location(file.file)
    if not extracted_data:
        raise HTTPException(
            status_code=400, 
            detail="No GPS metadata found in photo. Make sure the photo has geotagging enabled."
        )

    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO locations (latitude, longitude, location_name, date_taken) VALUES (?, ?, ?, ?)",
        (
            extracted_data["latitude"],
            extracted_data["longitude"],
            extracted_data["location_name"],
            extracted_data["date_taken"]
        )
    )
    conn.commit()
    conn.close()

    return {"message": "Location saved successfully!", "data": extracted_data}