from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
from geopy.geocoders import Nominatim

def convert_to_degrees(value):
    """Convert GPS coordinates (Degrees, Minutes, Seconds) to decimal format."""
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

def extract_location(image_file):
    """Parse EXIF GPS data from an image file and reverse-geocode to location names."""
    try:
        image = Image.open(image_file)
        exif_data = image._getexif()
        if not exif_data:
            return None

        gps_info = {}
        date_taken = "Unknown Date"

        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'GPSInfo':
                for gps_tag_id in value:
                    sub_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    gps_info[sub_tag] = value[gps_tag_id]
            elif tag == 'DateTimeOriginal':
                date_taken = value

        if 'GPSLatitude' not in gps_info or 'GPSLongitude' not in gps_info:
            return None

        # Calculate Latitude
        lat = convert_to_degrees(gps_info['GPSLatitude'])
        if gps_info.get('GPSLatitudeRef', 'N') != 'N':
            lat = -lat

        # Calculate Longitude
        lon = convert_to_degrees(gps_info['GPSLongitude'])
        if gps_info.get('GPSLongitudeRef', 'E') != 'E':
            lon = -lon

        # Reverse Geocode (Coordinates -> Address)
        geolocator = Nominatim(user_agent="travel_tracker_app")
        location = geolocator.reverse((lat, lon), language="en")
        address = location.address if location else "Unknown Location"

        return {
            "latitude": round(lat, 6),
            "longitude": round(lon, 6),
            "location_name": address,
            "date_taken": date_taken
        }
    except Exception as e:
        print(f"Error parsing image EXIF data: {e}")
        return None