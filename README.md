# Introduction-To-Problem-Solving
#  Student Record Analyzer (Python)

A simple, menu-driven Python console application designed to manage, track, and analyze student academic records. This tool allows users to add new students, display all records, search by roll number, sort by marks, and delete records.

##  Features

* *Add Student: Input Roll Number, Name, and Marks, with automatic **Grade Calculation*.
* *Display Records*: View all stored student records.
* *Search: Find a student record quickly using their unique **Roll Number*.
* *Sort: Display all students sorted in descending order of **Marks* (Highest to Lowest).
* *Delete*: Remove a student record using the Roll Number.
* *Menu Interface*: Easy-to-use numbered console menu for navigation.

## ⚙ Grade Calculation Logic

The application automatically calculates the grade based on the following marks criteria:

| Marks Range | Grade Assigned |
| :---------: | :------------: |
| 90 - 100    | *A+* |
| 80 - 89     | *A* |
| 70 - 79     | *B* |
| 60 - 69     | *C* |
| 50 - 59     | *D* |
| 0 - 49      | *F* |

