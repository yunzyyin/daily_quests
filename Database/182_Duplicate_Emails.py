import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person["duplicated"] = person.drop(columns=["id"]).duplicated()
    return person[["email"]][person["duplicated"]==True].drop_duplicates().rename(columns={"email":"Email"})