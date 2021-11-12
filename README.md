# Student Performance advisor

The project repository can be found at the following link : https://github.com/songmaxime/student_performance_advisor

The objective of this python project is to deploy a solution that can give personalized advice
to student in order to improve their grade (G3 variables in the dataset).

Two datasets are available at "data/student-mat.csv" and "data/student-por.csv"

"data/student.yaml" is the file containing all the information related to the student we wish to give advice.
This application will read this yaml file and get the background profile of the student. Then it will search in the dataset all students with similar profile and observe what variables affect the school achievement of this group of students.
By ranking these variables, we can give personalized advices that can benefit the student.

A notebook is also available and explains the data analysis part and the solution.

### Installation
Before running main.py, please first install all the required python packages by running the following line : 

pip install -r requirements.txt

### How to use this application
1) Install the required python packages
2) Fill "data/student.yaml"
3) Run main.py

