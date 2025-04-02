# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price

# Main program to interact with the user
def main():
    try:
        # Prompt the user to enter the original price
        price = float(input("Enter the original price of the item: "))

        # Prompt the user to enter the discount percentage
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price using the function
        final_price = calculate_discount(price, discount_percent)

        # Print the result
        if final_price < price:
            print(f"The final price after applying the discount is: {final_price:.2f}")
        else:
            print(f"No discount applied. The original price remains: {price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()
