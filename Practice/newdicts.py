class student():

    def __init__(Self, name, age, gender, dmarks = [50,50,50]):
        Self.student_name = name
        Self.student_age = age
        Self.student_gender = gender
        Self.default_marks = dmarks
    
    def total_marks(Self, mark_list):
        if sum(mark_list) > 100:
            result = "PASS"
        else:
            result = "FAIL"
        return sum(mark_list), result

students_list = {
  "student_ID_1" : {
    "name" : "Jia",
    "age" : 12,
    "gender" : "Female",
    "marks" : [500,200]
  },
    "student_ID_2" : {
    "name" : "Arjun",
    "age" : 12,
    "gender" : "Male",
    "marks" : [100,200]
  },
   "student_ID_3" : {
    "name" : "Nethra",
    "age" : 18,
    "gender" : "Female",
    "marks" : [100,200]
  }
}

print ("*****************class report************************************")
for student_id, student_details in students_list.items():
    cstudent= student(student_details["name"],student_details["age"], student_details["gender"],student_details["marks"]) ## create a class with the required attributes...
    cstudent.id = student_id ##  dynamically create an attribute...
    #cstudent.__default_marks = [0,0,0]
    a, b = cstudent.total_marks(student_details["marks"])[0],cstudent.total_marks(student_details["marks"])[1]
    print (cstudent.id,cstudent.student_name, cstudent.student_age, cstudent.student_gender,cstudent.default_marks,a,b )
print ("*****************class report************************************")

