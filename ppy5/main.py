import smtplib
from email.mime.text import MIMEText


def save(write_path, students):
    with open(write_path, "w") as file_write:
        for s in students:
            l = f"{s['email']},{s['name']},{s['lastname']},{s['points']},{s['grade']},{s['status']}\n"
            file_write.write(l)


def grade(students):
    for s in students:
        if s["status"] == "MAILED" or s["status"] == "GRADED":
            print(f"Student {s['name']} is already graded")
        else:
            points = int(s["points"])
            if points < 50:
                s["grade"] = 2
            elif 51 <= points < 60:
                s["grade"] = 3
            elif 61 <= points < 70:
                s["grade"] = 3.5
            elif 71 <= points < 80:
                s["grade"] = 4
            elif 81 <= points < 90:
                s["grade"] = 4.5
            elif 91 <= points <= 100:
                s["grade"] = 5
            s["status"] = "GRADED"
    save("students.txt", students)


def delete(students, email):
    for i, s in enumerate(students):
        if s["email"] == email:
            del students[i]
    save("students.txt", students)


def add(students, new_student):
    email = new_student["email"]
    exists = False
    for s in students:
        if s["email"] == email:
            exists = True
    if exists:
        print("Student already exists")
    else:
        students.append(new_student)
    save("students.txt", students)


def send_email(students):
    for s in students:
        if s["status"] == "MAILED":
            print("Email already sent")
        elif s["status"] == "GRADED":
            msg = MIMEText(f"Twoja ocena z przedmiotu PPY to: {s['grade']}")
            msg['Subject'] = "PPY"
            msg['From'] = "sender"
            msg['To'] = ', '.join("recipients")
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.login("sender", "password")
            smtp_server.sendmail("sender", "recipients", msg.as_string())
            smtp_server.quit()
            s["status"] = "MAILED"
    save("students.txt", students)


filepath = "students.txt"
student_list = []
with open(filepath) as file_object:
    for line in file_object:
        line.strip()
        values = line.rsplit(",")
        student = {
            "email": values[0],
            "name": values[1],
            "lastname": values[2],
            "points": values[3].strip(),
            "grade": "",
            "status": ""
        }
        if len(values) >= 5:
            student["grade"] = values[4]
        if len(values) >= 6:
            student["status"] = values[5]

        student_list.append(student)

print(student_list)
grade(student_list)
print(student_list)
#
# delete(student_list, "test@gmail.com")
# print(student_list)

# new_stud = {
#     "email": "values[0]",
#     "name": "values[1]",
#     "lastname": "values[2]",
#     "points": "values[3]",
#     "grade": "",
#     "status": ""
# }
# add(student_list, new_stud)
# print(student_list)

# send_email(student_list)
# print(student_list)
