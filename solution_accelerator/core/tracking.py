def get_tracking_status(entity_name: str):
    """
    Simulated tracking data
    """

    mock_tracking = {
        "Vendor A": {
            "manufacturing": "Completed",
            "dispatch": "In Progress",
            "delivery_eta_days": 5,
        },
        "Vendor B": {
            "manufacturing": "In Progress",
            "dispatch": "Pending",
            "delivery_eta_days": 12,
        },
        "Vendor C": {
            "manufacturing": "Completed",
            "dispatch": "Completed",
            "delivery_eta_days": 2,
        },
    }

    return mock_tracking.get(entity_name, {})
