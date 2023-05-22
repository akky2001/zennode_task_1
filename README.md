# zennode_task_1

# Product Catalog and Discount Calculator

This program allows users to input the quantity of products from a catalog and determine the total cost after applying various discount rules. It also calculates shipping and gift wrap fees to provide a comprehensive view of the final total.

## Catalog and Pricing

The catalog consists of three products with their corresponding prices:

- Product A: $20
- Product B: $40
- Product C: $50

## Discount Rules

The program applies the following discount rules based on specific conditions:

- **Flat $10 Discount** (rule: flat_10_discount):
  - If the cart total exceeds $200, a flat $10 discount is applied to the cart total.

- **5% Bulk Discount** (rule: bulk_5_discount):
  - If the quantity of any single product exceeds 10 units, a 5% discount is applied to the total price of that item.

- **10% Bulk Discount** (rule: bulk_10_discount):
  - If the total quantity exceeds 20 units, a 10% discount is applied to the cart total.

- **50% Tiered Discount** (rule: tiered_50_discount):
  - If the total quantity exceeds 30 units and any single product quantity is greater than 15, a 50% discount is applied to the products with a quantity above 15. The first 15 units are charged at the original price.

Please note that only one discount rule can be applied per purchase. In case multiple discounts are applicable, the program determines the most beneficial one for the customer.

## Fees

Apart from the product prices and discounts, the program also accounts for additional fees:

- **Gift Wrap Fee**: $1 per unit. Users can choose to wrap a product as a gift.
- **Shipping Fee**: Each package can accommodate up to 10 units, and the shipping fee for each package is $5.

## Usage

1. Run the program.
2. Input the quantity of each product as prompted.
3. Indicate whether a product should be wrapped as a gift.
4. The program will display the following details:

- The product name, quantity, and total amount for each product.
- The subtotal.
- The discount name applied and the discount amount.
- The shipping fee and the gift wrap fee.
- The total cost.
