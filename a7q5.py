# Global variable
counter = 0

def outer_function():
    # Enclosing variable (Nonlocal to inner_function)
    count = 10
    
    def inner_function():
        global counter      # Links to the module-level 'counter'
        nonlocal count      # Links to 'count' in outer_function
        
        counter += 1        # Modifies the global variable
        count += 5          # Modifies the enclosing variable
        
        print(f"Inside inner: global counter = {counter}, nonlocal count = {count}")

    inner_function()
    print(f"Inside outer: count after inner call = {count}")

# Execute the functions
print(f"Initial global counter: {counter}")
outer_function()
print(f"Final global counter: {counter}")