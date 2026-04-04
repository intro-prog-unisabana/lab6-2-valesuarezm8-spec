datos = {
    "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
    "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
    "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}
def assignment_averages(data):
    totals = {}
    counts = {}

    for student, grades in data.items():
        for assignment, score in grades.items():

            if assignment not in totals:
                totals[assignment] = 0
                counts[assignment] = 0

            totals[assignment] += score
            counts[assignment] += 1

    result = {}

    for assignment in totals:
        average = round(totals[assignment] / counts[assignment])
        result[assignment] = average

    return result