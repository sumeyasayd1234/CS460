# defining attributes
class Product:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration


    def __repr__(self):
        return f"Product(name='{self.name}', expiration={self.expiration})"

# implemmenation of bubble sort algorithm to sort 
def bubble_sort_products(products, attribute):
    n = len(products)
    for i in range(n):
        swapped = False
        # elements in palce
        for j in range(0, n-i-1):
            # comparing products
            if getattr(products[j], attribute) > getattr(products[j+1], attribute):
                products[j], products[j+1] = products[j+1], products[j]
                swapped = True
        #if no elements are swapped, list is sorted
        if not swapped:
            break

# function to check if a list is sorted based on a given attribute
def is_sorted(products, attribute):
    n = len(products)
    for i in range(1, n):
        if getattr(products[i-1], attribute) > getattr(products[i], attribute):
            return False
    return True

# example of implemenation of the code
if __name__ == "__main__":
    products = [
        Product("Milk", 10232024),
        Product("Bread", 11292024),
        Product("Cheese", 12162024)
    ]

    # sort products by expiration date using Bubble Sort
    attribute = 'expiration'
    bubble_sort_products(products, attribute)

    # checking if the products are sorted correctly
    if is_sorted(products, attribute):
        print(f"{attribute}:")
        for product in products:
            print(product)
    else:
        print("unable to sort")
