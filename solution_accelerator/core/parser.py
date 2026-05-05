def parse_request(user_input: str) -> dict:
    text = user_input.lower()

    if "316" in text:
        return {"material": "SS316L", "category": "piping"}
    elif "carbon" in text:
        return {"material": "CS", "category": "piping"}
    elif "pump" in text:
        return {"material": "centrifugal", "category": "pumps"}
    elif "valve" in text:
        return {"material": "control", "category": "valves"}
    elif "cable" in text:
        return {"material": "cable", "category": "electrical"}
    else:
        return {"material": "unknown", "category": "general"}
