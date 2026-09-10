school = {
    "Favour": {"score": [40, 77, 85]},
    "Blessing": {"score": [79, 58, 36]},
    "Peace": {"score": [55, 89, 43]}
}
for student in school:
    print("")
    print(student)
    total = 0
    for score in school[student]["score"]:
        total += score
    print(f"Total: {total}")

    average = total / len(school[student]["score"])
    print(f"Average: {average:.2f}")
    if average >= 50:
        print("status: PASS")
    else:
        print("status: FAIL")

