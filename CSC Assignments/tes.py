# ---------------------------------------------
# Object Oriented Example: Fractions
# ---------------------------------------------
# This example is based on the Interactive Textbook.
# ---------------------------------------------


# -------- Fraction Class ---------------------

class Fraction:

    def __init__(self):
        """Constructor with default values"""
        self.numerator = 1      # the numerator is on top
        self.denominator = 1    # the denominator is on the bottom

    def __str__(self):
        """ Convert object to a string"""
        return str(self.numerator) + "/" + str(self.denominator)

    def simplify(self):
        """ Use Euclid's algorithm to simplify fraction via gcd """
        m = self.numerator
        n = self.denominator

        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n

        self.numerator = self.numerator // n
        self.denominator = self.denominator // n

    def __add__(self, other_fraction):
        """ Add two fractions """
        result = Fraction()
        result.numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        result.denominator = self.denominator * other_fraction.denominator
        result.simplify()
        return result

    def __mul__(self, other):
        """Multiply two fractions"""
        result = Fraction()
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        result.simplify()
        return result

    def user_fraction(self):
        """ Modify fraction with user supplied values """
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))
        self.simplify()
    

# ---------- End of Fraction Class ------------


# ---------------------------------------------
# Print a menu of choices
# ---------------------------------------------

def print_menu():
    print()
    print("1. Enter Fraction 1.")
    print("2. Enter Fraction 2.")
    print("3. Add Fraction 2 to Fraction 1.")
    print("4. Add Fraction 1 to Fraction 2.")
    print("5. Print Fraction 1.")
    print("6. Print Fraction 2.")
    print("7. Multiply Fraction 1 by Fraction 2")
    print("8. Multiply Fraction 2 by Fraction 1")
    print("9. Quit.")
    print()

# ---------------------------------------------
# Enable the user to create a fraction
# ---------------------------------------------

def create_fraction(message):
    result = Fraction()
    print(message)
    result.user_fraction()
    return result

# ---------------------------------------------
# main application
# ---------------------------------------------

def main():

    fraction_1 = create_fraction("Enter Fraction 1")
    fraction_2 = create_fraction("Enter Fraction 2")

    choice = 0

    while choice != 9:
        print_menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            fraction_1.user_fraction()
        elif choice == 2:
            fraction_2.user_fraction()
        elif choice == 3:
            # fraction_1.add(fraction_2)
            fraction_1 += fraction_2
        elif choice == 4:
            # fraction_2.add(fraction_1)
            fraction_2 += fraction_1
        elif choice == 5:
            print(fraction_1)
        elif choice == 6:
            print(fraction_2)
        elif choice == 7:
            fraction_1 *= fraction_2
            print(fraction_1)
        elif choice == 8:
            fraction_2 *= fraction_1
            print (fraction_2)
        elif choice == 9:
            print("Goodbye!")
        else:
            print("Invalid choice.  Please try again.")

# ---------------------------------------------

main()
print(3 + 4)
