from django.shortcuts import get_object_or_404, redirect, render

from .forms import RequestForm, CommentForm
from .models import Request, Comment


def list_request(request):
    return render(request, 'request_list.html', {'requests': Request.objects.all()})


def view_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    comments = service_request.comments.all()
    return render(request, 'request_detail.html', {'service_request': service_request, 'comments': comments})


def create_request(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        service_request = form.save()
        return redirect('view_request', pk=service_request.pk)
    return render(request, 'request_form.html', {'form': form})


def update_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    form = RequestForm(request.POST or None, instance=service_request)
    if form.is_valid():
        form.save()
        return redirect('view_request', pk=service_request.pk)
    return render(request, 'request_form.html', {'form': form, 'service_request': service_request})


def delete_request(request, pk):
    service_request = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        service_request.delete()
        return redirect('list_request')
    return render(request, 'request_confirm_delete.html', {'service_request': service_request})

def create_comment(request, pk):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.request = Request.objects.get(pk=pk)
        comment.save()
        return redirect('view_request', pk=pk)
    return render(request, 'comment_form.html', {'form': form, 'request_pk': pk})

def update_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('view_request', pk=pk)
    return render(request, 'comment_form.html', {'form': form, 'request_pk':pk})


def delete_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('view_request', pk=pk)
    return render(request, 'comment_confirm_delete.html', {'comment': comment})