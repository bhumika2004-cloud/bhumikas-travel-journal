# 🗺️ Spatial Travel Journal & Interactive Map

A full-stack web application that automatically parses hidden GPS EXIF metadata from uploaded travel photos, reverse-geocodes raw spatial coordinates into readable locations, and visualizes travel history on an interactive Leaflet.js map with dynamic GeoJSON US state boundary overlays.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-005571?style=flat-square&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![Leaflet.js](https://img.shields.io/badge/Leaflet.js-1.9-199900?style=flat-square&logo=leaflet)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

---

## ✨ Key Features

* **Automated EXIF Ingestion:** Automatically scans uploaded image files using Python's `Pillow` library to extract hidden GPS coordinates (latitude, longitude) and timestamps without manual data entry.
* **Smart Reverse Geocoding:** Integrates OpenStreetMap's Nominatim API via `geopy` to translate raw numeric coordinates into clean, human-readable address strings (city, state, country).
* **Dynamic GeoJSON State Shading:** Loads US state polygon boundaries and dynamically applies translucent purple overlays to highlight states you have visited based on your database records.
* **Interactive Memories Sidebar:** Features real-time text searching, state dropdown filtering, thumbnail previews, and smooth camera flight animations (`map.flyTo`) connecting UI cards directly to map markers.
* **Persistent Storage:** Stores all parsed location records and photo metadata locally using a lightweight SQLite relational database managed via FastAPI.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, SQLite, Pillow, geopy, uvicorn
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), Leaflet.js
* **Spatial Data:** GeoJSON vector boundaries (US States)

---

## 📂 Project Architecture

```text
travel-journal/
│
├── main.py                # FastAPI app, database routing, and reverse geocoding logic
├── extract_gps.py         # Pillow EXIF parser and coordinate extractor
├── travel.db              # SQLite relational database (auto-generated)
├── requirements.txt       # Python package dependencies
├── static/
│   ├── index.html         # Frontend dashboard, sidebar UI, and Leaflet map
│   ├── style.css          # Custom styling and glassmorphic layout
│   └── us-states.json     # GeoJSON file for US state boundary overlays
└── uploads/               # Stored user-uploaded travel photographs
🚀 Getting Started & Local Installation
Follow these steps to run the project locally on your machine:

1. Clone the Repository
Bash
git clone [https://github.com/YOUR_USERNAME/bhumikas-travel-journal.git](https://github.com/YOUR_USERNAME/bhumikas-travel-journal.git)
cd bhumikas-travel-journal
2. Set Up a Python Virtual Environment
Bash
python -m venv venv
Windows (PowerShell): .\venv\Scripts\activate

Mac / Linux: source venv/bin/activate

3. Install Dependencies
Bash
pip install -r requirements.txt
4. Run the Development Server
Bash
uvicorn main:app --reload
5. Open in Your Browser
Navigate to http://127.0.0.1:8000 in your web browser to upload photos and explore your interactive travel map!

💡 How It Works (The Data Pipeline)
Upload: User uploads a travel photo through the web interface.

Extract: Python (Pillow) reads the binary image bytes, targets the EXIF metadata header, and pulls the GPS latitude, longitude, and creation timestamp.

Geocode: geopy queries OpenStreetMap's Nominatim endpoint to convert decimal coordinates into a structured location name.

Persist: FastAPI saves the photo file to disk and records the location metadata inside SQLite.

Visualize: Leaflet.js renders custom pins on the map, and JavaScript overlays GeoJSON polygon layers to shade visited US states.

📄 License
Distributed under the MIT License. See LICENSE for more information.
