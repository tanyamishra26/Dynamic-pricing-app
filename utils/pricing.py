def calculate_price(distance, time_min, surge):
    base_fare = 40          # ₹
    per_km_rate = 12        # ₹ per km
    per_min_rate = 2        # ₹ per min

    estimated = (
        base_fare +
        distance * per_km_rate +
        time_min * per_min_rate
    )

    surged_price = estimated * surge

    low = round(surged_price * 0.95)
    high = round(surged_price * 1.10)

    return low, high
