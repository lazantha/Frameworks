from django.shortcuts import render
from .forms import PostForm  # Import your PostForm here

def home(request):
    data=PostForm.objects.values()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'index.html', context)
