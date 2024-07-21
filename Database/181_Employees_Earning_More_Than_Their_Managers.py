import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    output = []
    for row in employee.iterrows():
        salary_of_manager = employee["salary"][row[1]["managerId"] == employee["id"]].values
        if len(salary_of_manager) != 0 and row[1]["salary"] > salary_of_manager[0]:
            output.append(row[1]["name"])
    return pd.DataFrame({"Employee": pd.Series(output)})
