import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salary_max = employee.groupby("departmentId")["salary"].max()
    output = []
    for row in employee.iterrows():
        if row[1]["salary"] == salary_max.loc[row[1]["departmentId"]]:
            output.append([department["name"][department["id"]==row[1]["departmentId"]].values[0],
                           row[1]["name"],
                           row[1]["salary"]])

    return pd.DataFrame(output, columns=["Department", "Employee", "Salary"])