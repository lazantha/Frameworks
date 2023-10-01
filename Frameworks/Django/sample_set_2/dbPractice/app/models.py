from django.db import models
from datetime import datetime  # Import datetime module correctly

class AdminTable(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class AttemptTable(models.Model):  # Corrected the typo in the model name
    attempt_id = models.AutoField(primary_key=True)
    attempt = models.IntegerField()  # Removed unnecessary max_length parameter

class DepartmentTable(models.Model):
    dep_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    calling_name = models.CharField(max_length=50)

# Corrected typos in ForeignKey references (Foreign Key references should be defined below the referenced models)
class SubjectTable(models.Model):
    subject_id = models.AutoField(primary_key=True)
    dep_id = models.ForeignKey(DepartmentTable, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=20)
    year = models.IntegerField()
    semester = models.IntegerField()

# Corrected the typo in ForeignKey references
class SyllabusTable(models.Model):
    syll_id = models.AutoField(primary_key=True)
    syll_cat = models.CharField(max_length=10)


class SuperAdminTable(models.Model):
    admin_id = models.AutoField(primary_key=True)
    dep_id = models.ForeignKey(DepartmentTable, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=200)



class ExamTable(models.Model):
    ex_id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(SubjectTable, on_delete=models.CASCADE)
    syll_id = models.ForeignKey(SyllabusTable, on_delete=models.CASCADE)
    super_admin_id = models.ForeignKey(SuperAdminTable, on_delete=models.CASCADE)
    held_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=20)


class MedicalTypeTable(models.Model):
    type_id = models.AutoField(primary_key=True)
    medical_type = models.CharField(max_length=10)


class MedicalInfoTable(models.Model):  # Corrected the typo in the model name
    med_id = models.AutoField(primary_key=True)
    med_type_id = models.ForeignKey(MedicalTypeTable, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(SubjectTable, on_delete=models.CASCADE)
    attempt_id = models.ForeignKey(AttemptTable, on_delete=models.CASCADE)
    exam_date = models.DateField()
    started_time = models.TimeField()
    end_time = models.TimeField()
    exam_location = models.CharField(max_length=10)
    issued_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    doc_name = models.CharField(max_length=50)
    medical_sheet = models.FileField(blank=True)
    is_confirm = models.BooleanField()
    is_authenticate = models.BooleanField()
    recorded_time = models.TimeField(default=datetime.now)  # Use callable function for default value


class StudentTypeTable(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_cat = models.CharField(max_length=10)



class StudentTable(models.Model):
    std_id = models.AutoField(primary_key=True)
    dep_id = models.ForeignKey(DepartmentTable, on_delete=models.CASCADE)
    std_type_id = models.ForeignKey(StudentTypeTable, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    index_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    id_card = models.ImageField(blank=True,null=True,upload_to='templates/images/')




