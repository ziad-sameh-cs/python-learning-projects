"""Learning project: Pandas data analysis.

A small practice script from my Python Programming Basics course.
It builds a tiny sample dataset in code (no real client data),
then uses Pandas to summarise it.

Run:  python pandas_data_analysis.py
Requires: pandas
"""

import pandas as pd

# Sample practice data: weekly study hours and quiz scores.
data = {
    "topic": ["Python", "Python", "Cloud", "Cloud", "Security", "Security"],
    "hours": [5, 7, 4, 6, 3, 5],
    "quiz_score": [82, 91, 74, 88, 79, 85],
}

df = pd.DataFrame(data)

print("Data:")
print(df)
print("\nSummary statistics:")
print(df.describe())
print("\nAverage hours and score by topic:")
print(df.groupby("topic")[["hours", "quiz_score"]].mean())
print("\nBest quiz score:", df["quiz_score"].max())
print("Total study hours:", df["hours"].sum())
