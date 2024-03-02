class student():

    def __init__(Self, name, age, gender):
        Self.student_name = name
        Self.student_age = age
        Self.student_gender = gender
    
    def total_marks(Self, mark_list):
        if sum(mark_list) > 100:
            result = "PASS"
        else:
            result = "FAIL"
        return sum(mark_list), result
    
    #def pass_fail(self,mark_list):
    #    a = total_marks(mark_list)
    #    if a > 100:
    #        result = "PASS"
    #    else:
    #        result = 'FAIL'
    #    return result


students_list = {
  "student_ID_1" : {
    "name" : "Jia",
    "age" : 12,
    "gender" : "Female",
    "marks" : [100,200]
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

for st_id, st_details in students_list.items():
    #print (st_id)
    for st_name, st_ran in st_details.items():
        print(st_name, st_ran)


for al in students_list.items():
    print (al[1])
    a = student(students_list["name"], students_list["age"], students_list["gender"])
    print(a)

final_marks, pass_fail = a.total_marks([10,50,50])[0], a.total_marks([10,50,50])[1]

print("the studend name is : ", a.student_name, "and she scored total marks of:", 
      final_marks, "final result is :", pass_fail )
