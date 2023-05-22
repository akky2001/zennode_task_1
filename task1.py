#python code

def apply_discount(catalog, cart):
    cart_total = 0
    quantities = {}

    # Step 1: Calculate total price for each item and update cart total
    for product, quantity in cart.items():
        price = catalog[product]
        total_price = price * quantity
        cart_total += total_price
        quantities[product] = quantity

    discount_amount = 0
    discount_name = ""

    # Step 2-7: Check each discount rule and update discount amount if applicable
    if cart_total > 200:
        discount_amount = max(discount_amount, 10)
        discount_name = "flat_10_discount"

    for product, quantity in quantities.items():
        if quantity > 10:
            discount = catalog[product] * quantity * 0.05
            if discount > discount_amount:
                discount_amount = discount
                discount_name = "bulk_5_discount"

    if sum(quantities.values()) > 20:
        discount = cart_total * 0.1
        if discount > discount_amount:
            discount_amount = discount
            discount_name = "bulk_10_discount"

    if sum(quantities.values()) > 30 and any(quantity > 15 for quantity in quantities.values()):
        above_15_total = sum(max(0, quantity - 15) for quantity in quantities.values())
        discount = catalog[product] * above_15_total * 0.5
        if discount > discount_amount:
            discount_amount = discount
            discount_name = "tiered_50_discount"

    # Step 8: Apply the best discount and update the final price
    final_price = cart_total - discount_amount

    # Gift wrap fee
    gift_wrap_fee = sum(quantities.values())

    # Step 3: Calculate shipping fee
    num_packages = sum(quantities.values()) // 10
    shipping_fee = num_packages * 5

    # Display details
    print("Product Details:")
    for product, quantity in quantities.items():
        total_price = catalog[product] * quantity
        print(f"{product}: Quantity: {quantity}, Total Amount: ${total_price}")

    print("------------------------")
    print("Subtotal: $" + str(cart_total))
    print("Discount Applied: " + discount_name)
    print("Discount Amount: $" + str(discount_amount))
    print("Shipping Fee: $" + str(shipping_fee))
    print("Gift Wrap Fee: $" + str(gift_wrap_fee))
    print("------------------------")
    print("Total: $" + str(final_price))

# Example usage:
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

cart = {
    "Product A": 5,
    "Product B": 10,
    "Product C": 20
}

apply_discount(catalog, cart)
