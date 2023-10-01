from django.shortcuts import render

def index(request):

	request.session['name']='lasantha'
	request.session['email']='sglasanthapradeep@gmail.com'
	print('session set')

	context={}
	return render(request,'index.html',context)


def user(request):

	name=request.session.get('name')
	print("session",name)
	context={}
	return render(request,'user.html',context)
