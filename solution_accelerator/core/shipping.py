import json
import os

import requests


def get_live_shipping():

    try:
        # Fallback to cached JSON (MAIN PATH)
        with open("solution_accelerator/data/shipping_sample.json") as f:
            data = json.load(f)

        return {
            "vessel_name": data.get("vesselName"),
            "status": data.get("status"),
            "location": data.get("area"),
            "port": data.get("currentPort", {}).get("name"),
            "speed": data.get("speedKnots"),
            "coordinates": {"lat": data.get("latitude"), "lon": data.get("longitude")},
        }

    except Exception as e:
        print("Shipping error:", e)
        return {"error": "Live tracking unavailable"}


def interpret_shipping(data):

    if not data or "error" in data:
        return "Tracking unavailable"

    if data["status"] == "Moored":
        return "Shipment currently at port, awaiting dispatch"

    if data["speed"] > 0:
        return f"In transit via sea, currently in {data['location']}"

    return "Status unclear"
