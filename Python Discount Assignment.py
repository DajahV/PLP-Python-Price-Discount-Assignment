'''In this python assignment python assignment checks if the discount percentage of an item is greater 20% 
and then calculate and return the actual amount, but returns the whole amount if the 
the discount percentage is not up to or greater than 20%
'''
# I create a function named calculate_discount
def calculate_discount(price, discount_percent):
    # Checking if the discount is 20% or higher
    if discount_percent >= 20:
        # Thene final price after applying the discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item here: "))
discount_percentage = float(input("Enter the discount percentage in (%) here: "))

# Calculating the final price using the calculate_discount function if there is any
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or original price based on the discount applied
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"The final price after applying the discount is: {final_price}")
