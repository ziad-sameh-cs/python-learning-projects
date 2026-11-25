"""Learning project: Matplotlib chart.

A small practice script from my Python Programming Basics course.
It draws a bar chart of weekly study hours (sample data only).

Run:  python matplotlib_chart.py
Requires: matplotlib
The chart is saved as study_hours.png.
"""

import matplotlib.pyplot as plt

topics = ["Python", "Cloud", "Security", "HTML"]
hours = [12, 10, 8, 6]

plt.figure()
plt.bar(topics, hours)
plt.title("Weekly study hours (practice data)")
plt.xlabel("Topic")
plt.ylabel("Hours")
plt.tight_layout()
plt.savefig("study_hours.png")
print("Chart saved as study_hours.png")
