import json


def load_quotes(path="solution_accelerator/data/epc_quotes.json"):
    with open(path) as f:
        return json.load(f)


def compute_completeness(quote, required_items):
    present = set(quote["items"])
    required = set(required_items)

    missing = required - present

    # 🔥 FIX: avoid division by zero
    if len(required) == 0:
        return 1.0, []  # treat as fully complete (safe default)

    completeness_score = len(present) / len(required)

    return completeness_score, list(missing)


def normalize(values):
    min_v = min(values)
    max_v = max(values)
    return [(v - min_v) / (max_v - min_v + 1e-6) for v in values]


def compare_quotes(quotes, category):
    category = category.lower()
    weights = {"price": 0.5, "delivery": 0.3, "completeness": 0.2}

    required_map = {
        "piping": ["pipe", "elbow", "flange"],
        "pipes": ["pipe", "elbow", "flange"],
        "pumps": ["pump"],
        "valves": ["valve"],
        "electrical": ["cable"],
    }

    required_items = required_map.get(category.lower(), ["generic_item"])
    if not required_items:
        required_items = ["generic_item"]

    prices = [q["price_per_unit"] for q in quotes]
    deliveries = [q["delivery_days"] for q in quotes]

    norm_price = normalize(prices)
    norm_delivery = normalize(deliveries)

    results = []

    for i, q in enumerate(quotes):
        completeness, missing = compute_completeness(q, required_items)

        score = (
            weights["price"] * (1 - norm_price[i])
            + weights["delivery"] * (1 - norm_delivery[i])
            + weights["completeness"] * completeness
        )

        results.append(
            {
                "entity": q["entity"],
                "price": q["price_per_unit"],
                "delivery": q["delivery_days"],
                "completeness": round(completeness, 2),
                "missing_items": missing,
                "score": round(score, 3),
            }
        )

    return sorted(results, key=lambda x: x["score"], reverse=True)
