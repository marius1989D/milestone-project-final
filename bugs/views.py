from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Bug, Comment
from .forms import BugCommentForm, BugPostForm



def bugs_list(request):
	"""
	This view will list all bugs starting with the most recent ones
	"""
	bugs = Bug.objects.order_by('-created_on').all()
	paginator = Paginator(bugs, 4)
	page = request.GET.get('page')
	bugs = paginator.get_page(page)
	return render(request, 'bugs/bugs.html', {'bugs': bugs})

def bug_detail(request, pk):
	"""
	This view allow users to see a specific bug report in a separate window
	and also to add comments to it
	"""
	# Retrive bug details
	bug = get_object_or_404(Bug, pk=pk)
	bug.views += 1
	bug.save()
	comments = bug.comments.filter(active=True)
	new_comment = None
	# Comments functionality *** credit for the code to https://djangocentral.com
	if request.method == 'POST':
		comment_form = BugCommentForm(data=request.POST)
		if comment_form.is_valid:
			new_comment = comment_form.save(commit=False)
			new_comment.bug = bug
			new_comment.save()
	else:
		comment_form = BugCommentForm
	return render(request, 'bugs/bug_detail.html', {'bug': bug, 
											'comments': comments,
											'new_comment': new_comment,
											'comment_form': comment_form})


@login_required
def bug_likes(request, pk):
	"""
	This view allow users to like bug reports
	"""
	bug = get_object_or_404(Bug, pk=pk)
	bug.likes += 1
	bug.save()

	return redirect('bugs:bug_detail', pk=bug.pk)


@login_required
def bug_add(request):
	"""
	This view allow users to submit their bug reports
	"""
	if request.method == 'POST':
		bug_form = BugPostForm(request.POST)
		if bug_form.is_valid:
			bug = bug_form.save(commit=False)
			bug.author = request.user
			bug.save()
			messages.success(request, 'Successfully created!')
			return redirect('bugs:bug_detail', pk=bug.pk)
	else:
		bug_form = BugPostForm()
	return render(request, 'bugs/bug_add.html', {'bug_form': bug_form})


@login_required
def bug_delete(request, pk):
	"""
	This view allow a user to delete a bug report, but only if is the author 
	"""
	bug = get_object_or_404(Bug, pk=pk)
	if request.user == bug.author:
		bug.delete()
		messages.success(request, 'Successfully deleted!')
	else:
		messages.error(request, 'You can\'t delete this!')
		return redirect('bugs:bug_detail', pk=bug.pk)

	return redirect('bugs:bugs_list')


@login_required
def bug_edit(request, pk):
	"""
	This view allow users to edit a previously submited bug report
	"""
	bug = get_object_or_404(Bug, pk=pk)
	if request.user == bug.author:
		if request.method == "POST":
			bug_form = BugPostForm(request.POST, instance=bug)
			if bug_form.is_valid:
				bug_form.save()
				return redirect('bugs:bug_detail', pk=bug.pk)
		else:
			bug_form = BugPostForm(instance=bug)
		return render(request, "bugs/bug_add.html", {"bug_form": bug_form})
	else:
		messages.error(request, 'You can\'t edit this!')
		bug_form = BugPostForm()
	return redirect('bugs:bug_detail', pk=bug.pk)


