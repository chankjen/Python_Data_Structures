#Staff & Patient Records -Key-value pairs for instant lookups
# Staff Directory (ID → Details)
staff = {
    101: {"name": "Dr. Smith", "role": "Cardiologist", "station": "ER"},
    202: {"name": "Nurse Lee", "role": "ICU", "station": "Ward 3B"},
    303: {"name": "Dr. Patel", "role": "Radiologist", "station": "Lab 2"}, 
    404: {"name": "Dr. Hussain", "role" "Supervisor", "station", "theater"}
}

# Patient Records (ID → Medical History)
patients = {
    "P881": {"name": "John Munae", "allergies": ["Penicillin"], "ward": "ICU"},
    "P882": {"name": "Maria Garcia", "allergies": ["Smoke"], "ward": "Ward 4A"},
    "p882": {"name": "Hassana Musa", "allergies": ["Maternity"], "ward": "Maternity ward"]
}

# Access data
print("Cardiologist on duty:", staff[101]['name'])  # Dr. Smith
print("John's allergies:", patients["P881"]["allergies"])  # ['Penicillin']

# Add new patient
patients["P883"] = {"name": "Alex Kim", "allergies": ["Latex"], "ward": "ER"}
