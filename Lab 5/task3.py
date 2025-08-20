from typing import List, Dict, Tuple


def _build_user_preferences(
    products: List[Dict], user_history: List[Dict]
) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float]]:
    """Aggregate user preferences from interaction history.

    Returns (category_weights, brand_weights, product_bias)
    where interaction strengths are: purchase=3, cart=2, view=1
    and more recent interactions are weighted slightly higher.
    """
    action_strength = {"purchase": 3.0, "cart": 2.0, "view": 1.0}
    category_weights: Dict[str, float] = {}
    brand_weights: Dict[str, float] = {}
    product_bias: Dict[str, float] = {}

    product_by_id = {str(p["id"]): p for p in products}

    # Recency: later entries in history get a small boost
    history_len = max(1, len(user_history))
    for idx, interaction in enumerate(user_history):
        product_id = str(interaction.get("product_id"))
        action = interaction.get("action", "view").lower()
        product = product_by_id.get(product_id)
        if not product:
            continue
        strength = action_strength.get(action, 1.0)
        recency_boost = 1.0 + (idx / history_len) * 0.2  # up to +20%

        category = str(product.get("category", "unknown")).lower()
        brand = str(product.get("brand", "unknown")).lower()

        category_weights[category] = category_weights.get(category, 0.0) + strength * recency_boost
        brand_weights[brand] = brand_weights.get(brand, 0.0) + strength * recency_boost
        product_bias[product_id] = product_bias.get(product_id, 0.0) + 0.1 * strength

    return category_weights, brand_weights, product_bias


def _score_product(
    product: Dict,
    category_weights: Dict[str, float],
    brand_weights: Dict[str, float],
    product_bias: Dict[str, float],
) -> Tuple[float, str]:
    """Compute a transparent score and an explanation string for a single product."""
    category = str(product.get("category", "unknown")).lower()
    brand = str(product.get("brand", "unknown")).lower()
    pid = str(product.get("id"))

    w_category = category_weights.get(category, 0.0)
    w_brand = brand_weights.get(brand, 0.0)
    w_bias = product_bias.get(pid, 0.0)

    # Popularity dampening: sqrt-like via power 0.5; default 0 if missing
    popularity = float(product.get("popularity", 0.0))
    popularity_term = popularity ** 0.5 * 0.1

    score = w_category + w_brand + w_bias + popularity_term
    explanation = (
        f"category match {w_category:.2f} + brand match {w_brand:.2f} + "
        f"product bias {w_bias:.2f} + popularity {popularity_term:.2f}"
    )
    return score, explanation


def recommend_with_feedback(
    products: List[Dict], user_history: List[Dict], top_n: int = 5
) -> None:
    """Recommend products based on user history with explanations and feedback.

    - Prints top-N recommendations and an explanation for each item.
    - Prompts the user for feedback: like (l), dislike (d), or skip (s) by product id.
    - Updates preferences interactively and re-displays recommendations until the user enters 'done'.
    """
    id_to_product = {str(p["id"]): p for p in products}

    # Exclude products that were already purchased
    purchased_ids = {
        str(h.get("product_id"))
        for h in user_history
        if str(h.get("action", "")).lower() == "purchase"
    }

    category_w, brand_w, product_bias = _build_user_preferences(products, user_history)

    def rank() -> List[Tuple[Dict, float, str]]:
        ranked = []
        for product in products:
            pid = str(product.get("id"))
            if pid in purchased_ids:
                continue
            score, expl = _score_product(product, category_w, brand_w, product_bias)
            ranked.append((product, score, expl))
        ranked.sort(key=lambda t: t[1], reverse=True)
        return ranked[:top_n]

    while True:
        top = rank()
        if not top:
            print("No recommendable products available.")
            return

        print("\nTop recommendations:")
        for product, score, expl in top:
            print(f"- [{product['id']}] {product['name']}  (score={score:.2f})")
            print(f"  Why: {expl}")

        cmd = input(
            "\nEnter feedback as '<product_id> <l/d/s>' (like/dislike/skip), or 'done' to finish: "
        ).strip()
        if cmd.lower() == "done":
            break

        parts = cmd.split()
        if len(parts) != 2:
            print("Please provide feedback in the form: <product_id> <l/d/s>")
            continue

        prod_id, fb = parts[0], parts[1].lower()
        if prod_id not in id_to_product:
            print("Unknown product id.")
            continue

        product = id_to_product[prod_id]
        category = str(product.get("category", "unknown")).lower()
        brand = str(product.get("brand", "unknown")).lower()

        if fb == "l":  # like
            category_w[category] = category_w.get(category, 0.0) + 1.0
            brand_w[brand] = brand_w.get(brand, 0.0) + 1.0
            product_bias[prod_id] = product_bias.get(prod_id, 0.0) + 0.5
        elif fb == "d":  # dislike
            category_w[category] = category_w.get(category, 0.0) - 0.8
            brand_w[brand] = brand_w.get(brand, 0.0) - 0.8
            product_bias[prod_id] = product_bias.get(prod_id, 0.0) - 0.5
        elif fb == "s":  # skip
            # slight exploration bias against repeated skips
            product_bias[prod_id] = product_bias.get(prod_id, 0.0) - 0.1
        else:
            print("Unknown feedback. Use l/d/s or 'done'.")
            continue


if __name__ == "__main__":
    # Small demo catalog and history
    demo_products = [
        {"id": "P1", "name": "Alpha Headphones", "category": "Audio", "brand": "Alpha", "popularity": 120},
        {"id": "P2", "name": "Beta Earbuds", "category": "Audio", "brand": "Beta", "popularity": 95},
        {"id": "P3", "name": "Gamma Phone Case", "category": "Accessories", "brand": "Gamma", "popularity": 60},
        {"id": "P4", "name": "Delta Charger", "category": "Accessories", "brand": "Delta", "popularity": 80},
        {"id": "P5", "name": "Omega Smartwatch", "category": "Wearables", "brand": "Omega", "popularity": 150},
        {"id": "P6", "name": "Zeta Fitness Band", "category": "Wearables", "brand": "Zeta", "popularity": 110},
        {"id": "P7", "name": "Sigma Laptop Sleeve", "category": "Accessories", "brand": "Sigma", "popularity": 30},
        {"id": "P8", "name": "Theta Bluetooth Speaker", "category": "Audio", "brand": "Theta", "popularity": 70},
        {"id": "P9", "name": "Lambda Keyboard", "category": "Peripherals", "brand": "Lambda", "popularity": 50},
        {"id": "P10", "name": "Kappa Mouse", "category": "Peripherals", "brand": "Kappa", "popularity": 65},
    ]

    demo_history = [
        {"product_id": "P2", "action": "view"},
        {"product_id": "P8", "action": "cart"},
        {"product_id": "P1", "action": "purchase"},
        {"product_id": "P4", "action": "view"},
    ]

    recommend_with_feedback(demo_products, demo_history, top_n=5)


