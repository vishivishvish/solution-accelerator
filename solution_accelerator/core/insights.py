from solution_accelerator.core.llm import call_llm


def generate_rfq(parsed_request: dict, top_entities: list) -> str:
    entity_names = [e["name"] for e in top_entities[:3]]

    prompt = f"""
    Generate a professional Request for Quotation (RFQ) email.

    Material: {parsed_request.get("material")}
    Category: {parsed_request.get("category")}
    Vendors: {", ".join(entity_names)}

    Include:
    - Subject line
    - Formal greeting
    - Item description
    - Quantity placeholder
    - Delivery timeline request
    - Compliance requirements
    - Closing statement

    Keep tone professional and concise.
    """

    return call_llm(prompt)


def compute_price_range(entities: list) -> dict:
    prices = [e["attributes"]["price"] for e in entities]

    if not prices:
        return {"min": None, "max": None, "avg": None}

    return {
        "min": min(prices),
        "max": max(prices),
        "avg": round(sum(prices) / len(prices), 2),
    }


def generate_entity_insights(entities: list) -> list:
    insights = []

    for e in entities:
        attr = e["attributes"]

        flags = []

        if attr["delivery"] > 55:
            flags.append("Slow delivery risk")

        if attr["reliability"] < 0.85:
            flags.append("Low reliability")

        insights.append({"name": e["name"], "flags": flags})

    return insights
