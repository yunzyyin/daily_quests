import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values(by="id")
    logs = logs.astype(str)
    consecutive_numbers = []
    previous_id = None
    previous_num = None
    repeat = 1

    for index, row in logs.iterrows():
        if previous_id and previous_num:
            if row["num"] == previous_num and int(row["id"]) == int(previous_id) + 1:
                repeat += 1
                if repeat >= 3:
                    consecutive_numbers.append(row["num"])
            else:
                repeat = 1
        previous_id = row["id"]
        previous_num = row["num"]
        
    return pd.DataFrame({"ConsecutiveNums": pd.Series(list(set(consecutive_numbers))).astype(int)})

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values(by="id")
    logs["next_id"] = logs["id"].shift(periods=-1)
    logs["next_num"] = logs["num"].shift(periods=-1)
    logs["second_id"] = logs["id"].shift(periods=-2)
    logs["second_num"] = logs["num"].shift(periods=-2)
    consecutive_nums = logs[["num"]][(logs["num"] == logs["next_num"]) &
                                     (logs["num"] == logs["second_num"]) &
                                     (logs["id"]+1 == logs["next_id"]) & 
                                     (logs["id"]+2 == logs["second_id"])]
    consecutive_nums = consecutive_nums.drop_duplicates().rename(columns={"num": "ConsecutiveNums"})
    return consecutive_nums