import pandas as pd

# Load raw dataset
df = pd.read_csv("../data/ecommerce_data.csv", encoding="ISO-8859-1")

# Remove cancelled transactions
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Save cleaned dataset
df.to_csv("../data/cleaned_ecommerce_data.csv", index=False)

print("✅ Data cleaned successfully and saved.")
