
# ==========================================
# WEEK 7 ASSIGNMENT
# QUESTION 2: THE REPORT BUILDER
# Author: Amiir Abdi
# Description: Reads learner data and generates a report
# ==========================================

import csv

# Read learner data from the CSV file
try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
        


except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

# Initialize counters
total = 0
passed = 0

# Process each learner's record
for row in rows:
    score = int(row["score"])

    total += score

    if score >= 50:
        passed += 1

# Calculate the average score
average = round(total / len(rows), 1) if rows else 0.0

# Generate the learner report
with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(len(rows) - passed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")
