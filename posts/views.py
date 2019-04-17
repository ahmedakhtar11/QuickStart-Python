from django.http import Http404, HttpResponse

from django.shortcuts import redirect, render

from django.views.generic import DetailView, ListView

from.models import Posts

def index(request):
  response = """
    <h1>Home Page</h1>
    <p>Welcome to the Home Page.</p>
    <div>Website made in Django</div>
  """
  return HttpResponse(response)

def test1(request):
  response = """
    <h1>Test Page 1</h1>
    <p>Testing HttpResponse</p>
  """
  return HttpResponse(response)

def test2(request):
  response = """
    <h1>Test Page 2</h1>
    <p>Testing HttpResponse</p>
  """
  return HttpResponse(response)

def app(request):
  # return render(request, 'posts/app.html')

  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'posts/app.html', context

  #  {
  #    'title': 'Latest Posts'
  #  }
  
  )


def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)