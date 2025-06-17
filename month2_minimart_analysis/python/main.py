# Entry point for the MiniMart data reporting system
import json

# Sample product & order data
products = [
    {"name": "Milk", "price": "2.5"},
    {"name": "Bread", "price": "1.5"},
    {"name": "Eggs", "price": "0.2"},
]

orders = [
    {"customer": "Alice", "product": "Milk", "quantity": 2},
    {"customer": "Bob", "product": "Eggs", "quantity": 20},
    {"customer": "Charlie", "product": "Bread", "quantity": 5},
]

def generate_report(products, orders):
    # Type conversion & apply discount
    for product in products:
        price_float = float(product["price"])
        discounted = round(price_float * 0.9, 2)
        product["discounted_price"] = discounted

    # Identify large orders
    for order in orders:
        if order["quantity"] > 10:
            print(f"{order['customer']} placed a large order of {order['quantity']} items.")

    # Initialize summary
    summary = {
        "total_sold": 0,
        "product_count": {},
        "revenue_per_customer": {}
    }

    # Build summary data
    for order in orders:
        summary["total_sold"] += order["quantity"]

        # Count per product
        pname = order["product"]
        summary["product_count"][pname] = summary["product_count"].get(pname, 0) + order["quantity"]

        # Revenue per customer
        product_price = next(p for p in products if p["name"] == pname)["discounted_price"]
        amount = order["quantity"] * product_price
        cname = order["customer"]
        summary["revenue_per_customer"][cname] = summary["revenue_per_customer"].get(cname, 0) + amount

    # Most popular product
    most_popular = max(summary["product_count"], key=summary["product_count"].get)
    summary["most_popular_product"] = most_popular

    return summary

# Call the function and print the report
report = generate_report(products, orders)
print(report)

# Save report to JSON file
with open("report.json", "w") as json_file:
    json.dump(report, json_file, indent=4)
