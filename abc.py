class Student:
    def __init__(self,name,m,j):
        self.name=name
        self.m=m
        self.j=j
    def setMentorOrLearner(self):
        s = input("learner or mentor: ")
        if s == "mentor":
            print(f"{name} is a mentor")
            return s
        else:
            return s

    def setAvailableTime(self):
        j=input("available time: ")
        return j

    def display(self):
        print(self.name, end='\t\t\t')
        print(self.m, end='\t\t\t\t\t\t')
        print(self.j)


st=list()
n=int(input("Enter no of persons: "))
print("details entry...")
for i in range(n):
    name=input("Name:  ")
    m= Student.setMentorOrLearner(name)
    if m=="mentor":
      j=  Student.setAvailableTime(name)
    elif m == "learner":
        print(f"{name} is a learner")
        j=""
    else:
        print("invalid")
        j=""
    st.append(Student(name,m,j))
print("information")
print("Name\t\tMentor_or_Learner\t\tAvailable_time\t\t")
for i in range(n):
    st[i].display()


