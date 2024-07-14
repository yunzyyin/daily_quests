import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].sort_values(ascending=False).unique()
    if N > 0 and len(salary) >= N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [pd.Series(salary).iloc[N-1]]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
