import matplotlib.pyplot as plt

students_name = ["avinash", "arshita", "govind",
                 "aarvi", "aarav", "vishal", "rajkumar", "rajinder"]

students_marks = [35, 50, 20, 45, 25, 40, 25, 40]
marks_percentage = [35*100/50, 50*100/50, 20*100/50, 45 *
                    100/50, 25*100/50, 40*100/50, 25*100/50, 40*100/50]


def line_chart_of_students_and_marks():
    plt.plot(students_name, students_marks)
    plt.title("Students Marks Graph")

    plt.xlabel("students Names")
    plt.ylabel("Students Marks")
    plt.xlim(xmin=0, xmax=8)
    plt.ylim(ymin=1, ymax=50)
    plt.grid(True)

    plt.show()


def bar_chart_of_students_and_their_percentage():
    left_edges = students_name
    height = marks_percentage
    plt.bar(left_edges, height)
    plt.title("students percentage graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students percentage Marks")

    plt.show()


line_chart_of_students_and_marks()
bar_chart_of_students_and_their_percentage()
