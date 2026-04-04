def initialize_dict(student_name, subject_grades):
    return{student_name: subject_grades}

def add_student(student_grades={}):
    student_name= input("Enter student name: \n").title()
    materias={}
    while True:
       eleccion = input("Enter subject and grade (or 'exit' to finish):\n").lower()
       if eleccion == "exit":
          break
       materia_nota = eleccion.find(",")
       materia=eleccion[:materia_nota].title()
       nota= float(eleccion[materia_nota+1:])
       materias[materia]=nota
    student_grades[student_name]=materias
    print(f"Student {student_name} successfully added to the grades management system.")
    return student_grades
def get_students(student_grades, keys):
    resultado={}
    for estudiante in keys:
        found = False
        for student in student_grades:
            if student.lower()==estudiante.lower():
                resultado[student] = student_grades[student]
                found==True
                break

    if not found:
        print(f"{estudiante.title()} not found!")
    return resultado

    

