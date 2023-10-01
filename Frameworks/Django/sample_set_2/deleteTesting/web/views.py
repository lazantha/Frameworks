from django.shortcuts import render,get_object_or_404, redirect
from .models import PostTable
from .forms import PostForm


def home(request):
	data=PostTable.objects.all()
	
	context={'data':data}
	return render(request,'index.html',context)


def about(request):

	context={}
	return render(request,'about.html',context)


def deletePost(request,post_id):
	post = get_object_or_404(PostTable, post_id=post_id)
	if request.method=='POST':
		post.delete()
		return redirect('home')
	return render(request,'delete.html')




def updatePost(request,post_id):
	post = get_object_or_404(PostTable, post_id=post_id)
	if request.method=='POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = PostTableForm(instance=post)
	
	context={'form':form}
	return render(request,'update.html',context)
# Create your views here.
