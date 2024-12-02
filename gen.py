import pandas as pd

reviews_data = pd.read_json("reviews.jsonl", lines=True)

reviews = reviews_data[['title', 'text']].dropna()




