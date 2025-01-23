#semicolon = {"cohort": [24,23,22,21],
             #"duration": ["4mth","5mth","6mth","7mth","8mth"]
            # }
#print(semicolon["cohort"][1])

school_records = {
    "class_1":{
        "students":[
    {"name": "Harry", "scores":{"Math": 88,"English": 76}},
    {"name": "Solomon", "scores":{"Math": 95,"English": 89}},
]
},
"class_2":{
    "students":[
        {"name": "Daniel", "scores":{"Math": 78,"English": 72}},
        {"name": "Samuel", "scores":{"Math": 85,"English": 80}},
    ]

    }
}
#print(school_records["class_2"]["students"][1])
#for class_1 in school_records["class_1"]["students"]:
  #  print(class_1)
for class_name, class_data in school_records.items():
    print(f"class name: {class_name}")
    for student in class_data["students"]:
       print(f"{student['name']}")

total_students_math_score = 0
total_number_of_students = 0

for class_name, class_data in school_records.items():
    for student in class_data["students"]:
        total_students_math_score += student["scores"]["Math"]
        total_number_of_students += 1

average_score = total_students_math_score / total_number_of_students
print(f"This is the: {average_score}")