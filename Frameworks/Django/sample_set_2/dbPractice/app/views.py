from django.shortcuts import render
from .models import *

def home(request):
	
	dataset=StudentTable.objects.select_related('dep_id').values('first_name','last_name','index_number','email','dep_id__calling_name')
	dataset_2=StudentTable.objects.select_related('dep_id','std_type_id').values('first_name','last_name','index_number','email','dep_id__calling_name','std_type_id__type_cat')
	dataset_3 = MedicalInfoTable.objects.select_related('subject_id__dep_id').values(
    'exam_date',
    'started_time',  # Corrected the field name from 'start_time' to 'started_time'
    'end_time',
    'exam_location',
    'subject_id__subject_name',
    'subject_id__dep_id__department'
)

	context={'data':dataset,'data_2':dataset_2,'data_3':dataset_3}
	return render(request,'index.html',context)
# Create your views here.
