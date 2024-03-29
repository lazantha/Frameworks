# Generated by Django 4.2.3 on 2023-09-28 15:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTable',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AttemptTable',
            fields=[
                ('attempt_id', models.AutoField(primary_key=True, serialize=False)),
                ('attempt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentTable',
            fields=[
                ('dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=100)),
                ('calling_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTypeTable',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('medical_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTypeTable',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_cat', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusTable',
            fields=[
                ('syll_id', models.AutoField(primary_key=True, serialize=False)),
                ('syll_cat', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SuperAdminTable',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departmenttable')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTable',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_code', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departmenttable')),
            ],
        ),
        migrations.CreateModel(
            name='StudentTable',
            fields=[
                ('std_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('index_number', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('id_card', models.FileField(upload_to='')),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departmenttable')),
                ('std_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studenttypetable')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalInfoTable',
            fields=[
                ('med_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_date', models.DateField()),
                ('started_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('exam_location', models.CharField(max_length=10)),
                ('issued_date', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('doc_name', models.CharField(max_length=50)),
                ('medical_sheet', models.FileField(upload_to='')),
                ('is_confirm', models.BooleanField()),
                ('is_authenticate', models.BooleanField()),
                ('recorded_time', models.TimeField(default=datetime.datetime.now)),
                ('attempt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attempttable')),
                ('med_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicaltypetable')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subjecttable')),
            ],
        ),
        migrations.CreateModel(
            name='ExamTable',
            fields=[
                ('ex_id', models.AutoField(primary_key=True, serialize=False)),
                ('held_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=20)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subjecttable')),
                ('super_admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.superadmintable')),
                ('syll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.syllabustable')),
            ],
        ),
    ]
