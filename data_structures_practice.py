"""Learning project: data structures practice.

Small practice exercises from my Python Programming Basics course
using lists, dictionaries, sets and a stack.

Run:  python data_structures_practice.py
"""

# 1. Lists: sort and filter scores.
scores = [82, 91, 74, 88, 79, 85]
print("Sorted scores:", sorted(scores))
print("Scores above 85:", [s for s in scores if s > 85])

# 2. Dictionaries: count topics studied.
topics = ["Python", "Cloud", "Python", "Security", "Cloud", "Python"]
counts = {}
for topic in topics:
    counts[topic] = counts.get(topic, 0) + 1
print("Topic counts:", counts)

# 3. Sets: unique skills.
skills = {"Python", "HTML", "Python", "Cloud Computing"}
print("Unique skills:", sorted(skills))

# 4. A simple stack (list used as a stack).
stack = []
for task in ["learn lists", "learn dicts", "learn sets"]:
    stack.append(task)
print("Stack:", stack)
print("Completed:", stack.pop())
print("Remaining:", stack)
