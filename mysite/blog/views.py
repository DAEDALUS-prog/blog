from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

        else:
            comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                              {'post': post,
                               'comments': comments,
                               'comment_form': comment_form,
                               'new_comment': new_comment})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading " {}"'\
                .format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'\
                .format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'tdubinchik3@gmail.com', [cd['to']])
            sent = True
        return render(request, 'blog/post/share.html',
                      {'post': post, 'form': form, 'sent': sent},
                      )
    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html',
                          {'post': post, 'form': form, 'sent': sent},
                      )


