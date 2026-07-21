import statistics
import tabulate

def main():

    # Get student data and compile into a list
    data_list = []

    while True:
        user_input = input("Enter student (Name,Scores) or 'done' : ").lower()
        data_list.append(user_input)

        if user_input == "done":
            break
        elif "," not in user_input:
            raise ValueError("Invalid Entry")

    data_list = data_list[:-1]
    

    # Go through the student data list(data_list)
    reports = []

    for data in data_list:
        name,scores = data.split(",")

        name = name.strip().title()
        scores = scores.strip().split()

        for i,score in enumerate(scores):
            scores[i] = int(score)

        student_mean = average(scores)
        grade = letter_grade(student_mean)

        data = [name,student_mean,grade]

        reports.append(data)

    # Create table
    report_header = ["Name","Mean","Grade"]
    print("")
    print(tabulate.tabulate(reports,headers = report_header,tablefmt = "github"))

    
def average(scores):
    avg_score = statistics.mean(scores)
    
    return round(avg_score)

def letter_grade(avg):

    if avg >= 90:
        return "A"
    elif avg >= 80 and avg <= 89:
        return "B"
    elif avg >= 70 and avg <= 79:
        return "C"
    elif avg >= 60 and avg <= 69:
        return "D"
    elif avg <= 60:
        return "F"


main()