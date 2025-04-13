from django.shortcuts import render, redirect
from Blogs.models import BlogModel
from Blogs.forms import BlogForm
from django.contrib import messages

def CreateBlog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            s = form.save()
            messages.success(request, f"{s.name} is added.")
            return redirect ('create_blogs')
        else:
            messages.error(request, "Something is wrong", form.errors)
    
    context = {
        'form': form
    }
    return render(request, 'Blogs/createBlog.html', context)

def ReadBlog(request):
    blog = BlogModel.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'Blogs/readBlog.html', context)

def DeleteBlog(request, id):
    blog = BlogModel.objects.get(id=id)
    blog.delete()
    return redirect('read_blogs')

def UpdateBlog(request, id):
    data = BlogModel.objects.get(id=id)
    form = BlogForm(instance=data)
    if request.method == 'POST':
       form = BlogForm(request.POST, request.FILES, instance=data)

       if form.is_valid():
           form.save()
           return redirect('read_blogs')
       else:
           messages.error(request, "Something is wrong", form.errors)

    context = {'data':data, 'form':form}
    return render(request, 'Blogs/update_blog.html', context)

def ViewBlog(request, id):
    data = BlogModel.objects.get(id=id)
    context = {'data':data}
    return render(request, 'Blogs/view_blog.html', context)
        