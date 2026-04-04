def student_averages(data):
    result = {}

    for student, grades in data.items():
        if len(grades) == 0:
            result[student] = 0
        else:
            total = sum(grades.values())
            count = len(grades)
            result[student] = round(total / count)

    return result


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
        result[assignment] = round(totals[assignment] / counts[assignment])

    return result