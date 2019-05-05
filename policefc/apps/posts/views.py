from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Post, Author, PostView
from .tinymcemodel import PostTiny
from .forms import PostFormSample, CommentForm, PostForm
from apps.marketing.models import Signup


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)


def get_category_count():
    queryset = Post\
        .objects\
        .values('categories__title')\
        .annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True).order_by('-timestamp')[:3]
    latest = Post.objects.order_by('-timestamp')[:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'lastest': latest
    }
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def post(request, id):
    category_count = get_category_count()
    post = get_object_or_404(Post, id=id)
    most_recent = Post.objects.order_by('-timestamp')[:3]
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user,post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': post.pk
            }))
    context = {

        'post': post,
        'most_recent': most_recent,
        'category_count': category_count,
        'form': form,
    }
    return render(request, 'post.html', context)


def add_post_tiny(request):
    if request.method == "POST":
        form = PostFormSample(request.PostTiny)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('index/')
    else:
        form = PostFormSample()
    return render(request, 'post_form.html', {'form': form})


def edit_post_tiny(request, post_tiny_id=None):
    item = get_object_or_404(PostTiny, id=post_tiny_id)
    form = PostFormSample(request.PostTiny or None, instance=item)
    if form.is_valid():
        form.save()
        redirect('index/')
    return render(request, 'post_form.html', {'form': form})


def post_create(request):
    title='Update'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title':title,
        'form': form
    }
    return render(request, "post_create.html", context)


def post_update(request, id):
    title='Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None,
        request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title':title,
        'form': form
    }
    return render(request, "post_create.html", context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("post-list"))
