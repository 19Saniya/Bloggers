from django.shortcuts import render

# Create your views here.
post={
    'first_post':'Loreum Ipsum',
    'second_post':'Lala ipip',
    'third_post':'lala land',
}

def home(request):
    post_title = post.keys()
    return render(request, 'blog/home.html', {
        'posts':posts,
        'post_title':post_title,
    })


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request):
    pass
    # return render(request, 'blog/singlepost.html')