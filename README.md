# 🗺️ Bhumika's Travel Journal

An interactive, map-based travel journal application built to log trips, visualize visited regions, and automatically organize memories using geospatial data and EXIF metadata extraction.

---

## ✨ Key Features

* **📸 Automated EXIF Metadata Ingestion:** Built a Python processing pipeline using the `Pillow` library to extract latitude, longitude, and timestamps directly from uploaded photos, using OpenStreetMap's Nominatim API for reverse-geocoding into clean location records.
* **📍 Interactive Leaflet.js Mapping:** Loaded GeoJSON boundary data to render visited U.S. states with translucent overlays and interactive tooltips.
* **🕒 Dynamic Timeline & Sidebar:** Features live text search, state-based filtering, thumbnail previews, and smooth `flyTo` animations connecting sidebar entries directly to map markers.
* **⚡ Robust Backend API:** Powered by FastAPI endpoints and SQLite schemas to efficiently handle image uploads, return structured location data, and track state visit history.

---

## 🛠️ Tech Stack

* **Backend & API:** Python, FastAPI, SQLite
* **Geospatial & Mapping:** Leaflet.js, GeoJSON, OpenStreetMap Nominatim API
* **Data Processing:** Pillow (Python Imaging Library)
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)

---

## 🚀 Getting Started Locally

To set up and run this project locally on your machine:

### 1. Clone the repository
```bash
git clone [https://github.com/bhumika2004-cloud/bhumikas-travel-journal.git](https://github.com/bhumika2004-cloud/bhumikas-travel-journal.git)
cd bhumikas-travel-journal
2. Set up a virtual environment & install dependencies
Bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
3. Run the FastAPI backend server
Bash
uvicorn main:app --reload
4. Open the application
Open index.html or access the local server endpoint in your browser to interact with the map and timeline.

👩‍💻 Connect with Me
GitHub: @bhumika2004-cloud

LinkedIn: Bhumika Khadka
