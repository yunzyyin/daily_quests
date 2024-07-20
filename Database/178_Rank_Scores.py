import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(ascending=False, by="score")
    previous_score = scores["score"].max()
    ranks = []
    rank = 1
    for index, row in scores.iterrows():
        if row["score"] < previous_score:
            rank += 1
            ranks.append(rank)
            previous_score = row["score"]
        else:
            ranks.append(rank)
    scores["rank"] = ranks
    return scores[["score", "rank"]]

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(ascending=False, method="dense")
    return scores[["score", "rank"]].sort_values(ascending=False, by="score")