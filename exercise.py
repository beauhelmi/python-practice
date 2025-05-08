# Write a function called calculate_discounted_price
# The function will take two arguments, one a price (float)
# Second is discount (percentage as a float, eg 10 for 10%)
# If the discount is more than 50%, return "Discount too high!"
# Otherwise, return final price after discount (rounded to 2 decimal places)

def calculate_discounted_price(price, discount):
    if discount > 50:
        return "Discount too high!"
    final_price = price - (price * (discount / 100))

    return round(final_price, 2)

def main():
    # Step 1: Ask the user input for price and discount

    price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    # Step 2: Call the function and store the result
    result = calculate_discounted_price(price, discount)

    # Step 3: Print the result
    print(f"Final price after discount: {result}")


if __name__ == "__main__":
    main()
