# 🐍 Python Comprehension Master Lab
# Phase 1: The Foundations (Lists & Filtering)
# Exercise 1: Take a list of names and create a new list with the length of each name.
names = ["Alice", "Bob", "Charlie", "Danielle"]

length_of_names = [len(name) for name in names]

# Exercise 2: Create a list of squares for numbers 1–10, but only for even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_evens = [number ** 2 for number in numbers if number % 2 == 0]


# Exercise 3: Extract only the names that start with the letter "A" from a list.
clients = ["Apple", "Microsoft", "Amazon", "Facebook", "Alphabet"]

letter_a = [name for name in clients if name.startswith("A")]

# Phase 2: Dictionaries & Logic
# Exercise 4: Create a dictionary from two lists (one for keys, one for values).
keys = ["id", "username", "role"]
values = [1001, "jdoe_data", "admin"]

two_list_dict = {key:value for key, value in zip(keys, values)}

# Exercise 5 (The Schema Pivot): Take db_columns = [("username", "TEXT"), ("age", "INT")] and create a map where the value is True if the type is "TEXT", otherwise False.
db_columns = [("username", "TEXT"), ("age", "INT"), ("bio", "TEXT"), ("created_at", "TS")]

dict_mapping = {i[0]:True if i[1] == 'TEXT' else False for i in db_columns}

# Exercise 6 (The Ternary): Categorize a list of temperatures: if > 80, label it "High", else "Low".
temps = [65, 90, 72, 100, 55]

temp_category = ["High" if temp > 80 else "Low" for temp in temps]

# Phase 3: Nested Data & JSON Cleaning
# Exercise 7 (The Matrix Flatten): Extract all string values from a list of dictionaries, regardless of the key.
transactions = [
    {"vendor": "Amazon", "amount": 50, "city": "NYC"},
    {"vendor": "Netflix", "amount": 15, "city": "LA"},
    {"vendor": "Amazon", "amount": 20, "city": "CHI"}
]
string_transactions = {i[k] for i in transactions for k in i if type(i[k]) == str}

# Exercise 8 (The JSON Cleaner): From api_data, extract the city only if the user status is "active" and the score is >= 80.
api_data = [
    {"id": 1, "status": "active", "meta": {"city": "NYC", "score": 90}},
    {"id": 2, "status": "inactive", "meta": {"city": "LA", "score": 95}},
    {"id": 3, "status": "active", "meta": {"city": "Chicago", "score": 75}},
    {"id": 4, "status": "active", "meta": {"city": "Miami", "score": 82}}
]

user_data = [data['meta']['city'] for data in api_data if data['status'] == 'active' and data['meta']['score'] >= 80]

# Exercise 9a: REMOVE negatives (Filter)
# Goal: [[22.5, 23.0], [21.8, 22.1], [20.5, 20.9]]
hourly_readings = [
    [22.5, -99, 23.0],
    [-1, 21.8, 22.1],
    [20.5, 20.9]
]

filtered_readings = [
    [reading for reading in readings if reading > 0] #list comprehension where expression is another list comprehension
    for readings in hourly_readings
]

# Exercise 9b: REPLACE negatives with 0 (Map)
# Goal: [[22.5, 0, 23.0], [0, 21.8, 22.1], [20.5, 20.9]]
normalized_readings = [
    [reading if reading > 0 else 0 for reading in readings] #filtering logic with if else statement
    for readings in hourly_readings
]

# Phase 4: The Advanced Tier
# Exercise 10 (Matrix Normalizer): In a 3 X 3 grid, replace negative numbers with 0 and double all positive numbers. Keep the nested structure.
raw_matrix = [
    [1, -2, 3],
    [-5, 0, 4],
    [6, 7, -1]
]

doubled_positives = [
     [i * 2 if i > 0 else 0 for i in row]
    for row in raw_matrix
]


# Exercise 11 (Generator Expression): Create a memory-efficient generator that filters for "ERROR" in a log list and converts the message to uppercase.
logs = ["INFO: System ok", "ERROR: Disk full", "INFO: Loading", "ERROR: Access denied"]

filtered_generator = (i.split(':')[1].strip().upper() for i in logs if i.split(':')[0] == 'ERROR')

# Exercise 12 (Matrix Transpose): Flip a 2 X 3 matrix into a 3 X 2 matrix (rows become columns).
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed_matrix = [
    [i for i in row] 
    for row in zip(matrix[0], matrix[1])
]


