from django.shortcuts import render

# Create your views here.
#creating the view, post_list, from /blog/urls.py
def post_list(request):
    return render(request, 'blog/post_list.html', {})
