
from django.contrib import admin
from .models import AdminTable, AttemptTable, DepartmentTable, ExamTable, MedicalInfoTable, MedicalTypeTable, StudentTable, StudentTypeTable, SubjectTable, SuperAdminTable, SyllabusTable

admin.site.register([
    AdminTable,
    AttemptTable,
    DepartmentTable,
    ExamTable,
    MedicalInfoTable,
    MedicalTypeTable,
    StudentTable,
    StudentTypeTable,
    SubjectTable,
    SuperAdminTable,
    SyllabusTable,
])


# Register your models here.
