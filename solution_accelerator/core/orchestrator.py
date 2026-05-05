import json

from solution_accelerator.core.comparison import compare_quotes, load_quotes
from solution_accelerator.core.insights import (
    compute_price_range,
    generate_entity_insights,
    generate_rfq,
)
from solution_accelerator.core.market import get_market_history
from solution_accelerator.core.parser import parse_request
from solution_accelerator.core.reconciliation import check_reconciliation
from solution_accelerator.core.retrieval import load_entities, retrieve_entities
from solution_accelerator.core.scoring import score_entities
from solution_accelerator.core.shipping import get_live_shipping, interpret_shipping
from solution_accelerator.core.tracking import get_tracking_status


def run_pipeline(
    user_input: str, config_path="solution_accelerator/configs/epc_config.json"
):

    if isinstance(user_input, dict):
        parsed = user_input

        # minimal safety
        if "category" not in parsed:
            raise ValueError("Missing category in input")

    else:
        parsed = parse_request(user_input)

    entities = load_entities()
    filtered = retrieve_entities(parsed, entities)

    with open(config_path) as f:
        config = json.load(f)

    ranked = score_entities(filtered, config)

    price_range = compute_price_range(ranked)
    rfq_email = generate_rfq(parsed, ranked)
    entity_insights = generate_entity_insights(ranked)

    quotes = load_quotes()
    category = parsed["category"]
    comparison = compare_quotes(quotes, category)
    best_entity = ranked[0]["name"] if ranked else None

    tracking = get_tracking_status(best_entity) if best_entity else {}
    reconciliation = check_reconciliation()

    market_data = {
        "Steel": get_market_history("SLX"),
        "Copper": get_market_history("HG=F"),
        "Aluminum": get_market_history("ALI=F"),
    }

    shipping = get_live_shipping()
    shipping_summary = interpret_shipping(shipping)

    return {
        "parsed_request": parsed,
        "ranked_entities": ranked,
        "price_range": price_range,
        "rfq_email": rfq_email,
        "entity_insights": entity_insights,
        "quote_comparison": comparison,
        "tracking": tracking,
        "reconciliation": reconciliation,
        "market_data": market_data,
        "shipping": shipping,
        "shipping_summary": shipping_summary,
    }
