
def greeting(name, surname=None):
	if surname:
		print(f"hello {name} {surname}")
	else:
		print(f"hello {name}")

greeting("kennyfer", "otano")  # prints: hello kennyfer otano
greeting("jorge")              # prints: hello jorge

def make_peanut_butter_and_jelly_sandwich(greet_func, name, surname=None):
	print("1. Take two slices of bread.")
	print("2. Spread peanut butter on one slice.")
	print("3. Spread jelly on the other slice.")
	print("4. Put the slices together to make a sandwich.")
	greet_func(name, surname)
	print("Sandwich is ready!")

# Example usage:
make_peanut_butter_and_jelly_sandwich(greeting, "kennyfer", "otano")
make_peanut_butter_and_jelly_sandwich(greeting, "jorge")