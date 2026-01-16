import os
import json
import requests
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SWAGGER_PATH = os.path.join(BASE_DIR, "swagger", "student_v1.json")

def check_drift(api_url):
    with open(SWAGGER_PATH) as f:
        swagger = json.load(f)

    expected_props = swagger["paths"]["/student"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]
    expected_fields = set(expected_props.keys())

    response = requests.get(api_url).json()
    actual_fields = set(response.keys())

    missing = expected_fields - actual_fields
    extra = actual_fields - expected_fields

    severity = "SAFE"
    issues = []

    if missing:
        severity = "CRITICAL"
        issues.append(f"Missing fields: {list(missing)}")

    if extra:
        if severity != "CRITICAL":
            severity = "WARNING"
        issues.append(f"Extra fields: {list(extra)}")

    return {
        "api_name": "Student API",
        "status": severity,
        "issues": issues,
        "expected_fields": list(expected_fields),
        "actual_fields": list(actual_fields),
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
