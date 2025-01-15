import pandas as pd

# 2. Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Joachim"],
    "Age": [24, 27, 22, 32, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data)


df = df.replace("Alice", "Alice Smith")
