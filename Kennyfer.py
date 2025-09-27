
def greeting(name, surname=None):
	if surname:
		print(f"hello {name} {surname}")
	else:
		print(f"hello {name}")

greeting("kennyfer", "otano")  # prints: hello kennyfer otano
greeting("jorge")              # prints: hello jorge