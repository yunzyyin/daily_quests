import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_with_orders = set(orders["customerId"].values)
    customers_without_orders = []
    for row in customers.iterrows():
        if row[1]["id"] not in customers_with_orders:
            customers_without_orders.append(row[1]["name"])
    return pd.DataFrame({"Customers": pd.Series(customers_without_orders)})