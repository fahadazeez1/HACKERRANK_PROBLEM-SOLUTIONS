import itertools

def cartesian_product(list1, list2):
    # Compute Cartesian product of list1 and list2
    product = itertools.product(list1, list2)
    
    # Format each tuple in the product as (x, y) and join them with space
    result = ' '.join(f'({x}, {y})' for x, y in product)
    
    return result

if __name__ == '__main__':
    # Read input lists
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    
    # Compute Cartesian product
    result = cartesian_product(list1, list2)
    
    # Output the result
    print(result)
