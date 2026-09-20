def normalize(values):
    min_v = min(values)
    max_v = max(values)
    return [(v - min_v) / (max_v - min_v + 1e-6) for v in values]


def score_entities(entities: list, config: dict) -> list:
    weights = config["weights"]

    prices = [e["attributes"]["price"] for e in entities]
    deliveries = [e["attributes"]["delivery"] for e in entities]
    reliability = [e["attributes"]["reliability"] for e in entities]

    norm_price = normalize(prices)
    norm_delivery = normalize(deliveries)

    scored = []

    for i, e in enumerate(entities):
        score = (
            weights["price"] * (1 - norm_price[i])  # lower is better
            + weights["delivery"] * (1 - norm_delivery[i])
            + weights["reliability"] * reliability[i]
        )

        e_copy = e.copy()
        e_copy["score"] = round(score, 3)
        scored.append(e_copy)

    return sorted(scored, key=lambda x: x["score"], reverse=True)
