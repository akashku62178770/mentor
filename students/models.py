from enum import unique
from django.contrib.auth.models import User
from django.db import models

# User = settings.AUTH_USER_MODEL  # auth.user

# Create your models here.
Department = (
    ("CSE", "CSE"),
    ("ISE", "ISE"),
    ("ECE", "ECE"),
    ("ME", "ME"),
    ("CIV", "CIV"),
    ("EEE", "EEE"),
    ("MAT", "MAT"),
    ("PHY", "PHY"),
    ("CHE", "CHE"),
    ("ENG", "ENG"),
    ("KAN", "KAN"),
)
sem = (
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
    ("VIII", "VIII"),
)
Designation = (
    ("HOD", "HOD"),
    ("PRINCIPAL", "PRINCIPAL"),
    ("AST. PROF", "AST. PROF"),
    ("PROF", "PROF"),
    ("L. INSTR", "L. INSTR"),
)
# Degree = (
#     (B)
# )
Masters = (
    ("M.TECH", "M.TECH"),
    ("M.SC", "M.SC"),
    ("M.TECH", "M.TECH"),
)

# 1
class Student(models.Model):
    usn = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=3, choices=Department)
    sem = models.CharField(max_length=4, choices=sem)
    section = models.CharField(max_length=1)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.usn)

# 2
class StudentProfile(models.Model):
    usn = models.OneToOneField(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="students")
    fatherName = models.CharField(max_length=50)
    fatherOccupation = models.CharField(max_length=50)
    fatherPhone = models.CharField(max_length=50)
    fatherMail = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    motherOccupation = models.CharField(max_length=50)
    motherPhone = models.CharField(max_length=50)
    motherMail = models.CharField(max_length=50)
    currentAddress = models.CharField(max_length=200)
    permanentAddress = models.CharField(max_length=200)
    hobby = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    ambition = models.CharField(max_length=50)
    health = models.CharField(max_length=50, help_text="Any health issue!")

    def __str__(self):
        return str(self.usn)

# 3
class Mentor(models.Model):
    user = models.ManyToManyField(User)
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=10, choices=Designation)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.name)

# 4
class ParentInteraction(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    remark = models.CharField(max_length=500)

    def __str__(self):
        return str(self.usn)

# 5
class MentorGeneralRemark(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem = models.CharField(max_length=4, choices=sem)
    remark = models.CharField(max_length=500)

    def __str__(self):
        return str(self.usn)

# 6
# class StudentAcademicPerformance(models.Model):
#     usn = models.ForeignKey(Student, on_delete=models.CASCADE)
#     sem = models.CharField(max_length=4, choices=sem)
#     sub1 = models.CharField(max_length=20)
#     code1 = models.CharField(max_length=10)
#     int1a = models.DecimalField(decimal_places=2, max_digits=3)
#     int1b = models.DecimalField(decimal_places=2, max_digits=3)
#     int1c = models.DecimalField(decimal_places=2, max_digits=3)
#     act1 = models.DecimalField(decimal_places=2, max_digits=3)
#     finalIa1 = models.DecimalField(decimal_places=2, max_digits=3)
#     ext1 = models.DecimalField(decimal_places=2, max_digits=3)
#     att1 = models.DecimalField(decimal_places=2, max_digits=3)
#     remarks1 = models.CharField(max_length=10)



    def __str__(self):
        return str(self.usn)



"""
sub1
code1
int1
"""


"""
sub1
code1
int1a
int1b
int1c
act1
finalIa1
att1
ext 1
remarks1
"""

# 7
class StudentInteraction(models.Model):
    usn = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem = models.CharField(max_length=4, choices=sem)
    date = models.DateField()
    time = models.TimeField()
    concern = models.CharField(max_length=500)
    remark = models.CharField(max_length=500)

    def __str__(self):
        return str(self.usn)
