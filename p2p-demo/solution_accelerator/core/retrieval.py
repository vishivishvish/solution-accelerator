import json


def load_entities(path="solution_accelerator/data/epc_entities.json"):
    with open(path) as f:
        return json.load(f)


def retrieve_entities(parsed_request: dict, entities: list) -> list:
    material = parsed_request["material"].lower()
    category = parsed_request["category"].lower()

    results = []

    for entity in entities:
        entity_category = entity["category"].lower()
        entity_materials = [m.lower() for m in entity["materials"]]

        if category == entity_category and material in entity_materials:
            results.append(entity)

    # Fallback (IMPORTANT for demo)
    if not results:
        return entities[:3]

    return results
