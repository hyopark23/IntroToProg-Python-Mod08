# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Hyo Park, 08.29.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
product_objects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products' name
        product_price: (float) with the products' standard price
    methods:
        to_string(): (string) return class data as string implicitly
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Hyo Park, 08.29.2020,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name: str, product_price: float):
        """ Set name and price of a new object. """
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

    # Properties
    @property
    def product_name(self):  # Getter
        return str(self.__product_name.title())  # Title case

    @product_name.setter
    def product_name(self, value):  # Setter
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers!")

    @property
    def product_price(self):  # Getter
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # Setter
        try:
            self.__product_price = float(value)  # Convert to float if number
        except Exception as e:
            raise Exception("Price must be numbers!")

    # Methods
    def __str__(self):  # Formatted string method to implicitly call values
        return self.product_name + ", " + str(self.product_price)

    def to_string(self):  # Formatted string method to explicitly call values
        return self.product_name + ", " + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Hyo Park, 08.29.2020, Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, product_objects):
        """ Writes data from a list of dictionary rows to a file

        :param file_name: (string) with name of file:
        :param product_objects: (list) you want filled with file data:
        :return: product_objects
        """
        file = open(file_name, "w")
        for product in product_objects:
            file.write(product.__str__() + "\n")  # Returns data as string
        file.close()
        print("Data Saved!")

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return (list) of dictionary rows
        """
        product_objects = []
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = Product(product, price)
            product_objects.append(row)
        file.close()
        return product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

    methods:
        print_menu_tasks()
        input_menu_choice()
        input_new_product_and_price()
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_tasks():
        """ Display a menu of choices to user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show current products and prices
            2) Enter new product and price
            3) Save Data to File        
            4) Exit Program
            ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from user

        :return: (string) choice input by user
        """
        choice = str(input("Which option would you like to perform? [1 t 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_products(product_objects: list):
        """ Shows the current tasks in the list of dictionary rows

        :param: list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("Current products and prices are: ")
        for row in product_objects:
            print(row.product_name + " - $" + str(row.product_price))
        print("------------------")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """ Returns product and price to be removed from list of rows

        :return: (string) of product and price as a variable
        """
        print("Please enter a new product and its price.")
        name = input("Product: ")
        price = float(input("Price: "))
        row = Product(name, price)
        return row


# Presentation (Input/Output)  -------------------------------------------- #

# # Main Body of Script  ---------------------------------------------------- #
# # TODO: Add Data Code to the Main body
# # Load data from file into a list of product objects when script starts
product_objects = FileProcessor.read_data_from_file(file_name)
# # Show user a menu of options
while True:
    IO.print_menu_tasks()
    # Get user's menu option choice
    choice = IO.input_menu_choice()
    # Show user current data in the list of product objects
    if choice.strip() == "1":
        IO.print_current_products(product_objects)
        continue
    # Let user add data to the list of product objects
    elif choice.strip() == "2":
        product_objects.append(IO.input_new_product_and_price())
        continue
    # let user save current data to file and exit program
    elif choice.strip() == "3":
        FileProcessor.save_data_to_file(file_name, product_objects)
    elif choice.strip() == '4':
        print("Goodbye!")
        break

# Main Body of Script  ---------------------------------------------------- #

# Test Code
# product1 = Product('mop', 9.99)
# product2 = Product('vacuum', 199.99)
# product_objects = [product1, product2]
# print(product_objects)
# for object in product_objects:
#     print(f"{object.product_name}, {object.product_price}")
# for object in product_objects:
#     print(object)
# for object in product_objects:
#     print(object.to_string())
# FileProcessor.save_data_to_file(file_name, product_objects)
# f = FileProcessor.read_data_from_file(file_name)
# print(f)
# IO.print_current_products(product_objects)