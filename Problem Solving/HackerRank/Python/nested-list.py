def sort_scores(students: list) -> list:
    # mapping the scores list
    scores_list = list(map(lambda student: student[1], students))
    sorted_scores_list = sorted(scores_list, key= float)
    sorted_unique = []
    for i in sorted_scores_list:
        if i not in sorted_unique:
            sorted_unique.append(i)
    return sorted_unique


def sort_names(students: list) -> list:
    second_lowest_score = sort_scores(students)[1]
    names_list = []
    for student in students:
        if student[1] == second_lowest_score:
            names_list.append(student[0])
    names_list.sort()
    return names_list


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data = [name, score]
        students.append(student_data)
    sorted_students = sort_names(students)
    for student_name in sorted_students:
        print(student_name)
