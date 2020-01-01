from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Bug, Comment
from .forms import BugCommentForm

# Create your views here.
def bugs_list(request):
	"""
	This view will list all bugs 
	"""
	bugs = Bug.objects.order_by('-created_on').all()
	paginate_by = 3
	return render(request, 'bugs/bugs.html', {'bugs': bugs})

def bug_detail(request, pk):
	bug = get_object_or_404(Bug, pk=pk)
	bug.views += 1
	bug.save()
	comments = bug.comments.filter(active=True)
	new_comment = None

	if request.method == 'POST':
		comment_form = BugCommentForm(data=request.POST)
		if comment_form.is_valid:
			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = BugCommentForm
	return render(request, 'bugs/bug_detail.html', {'bug': bug, 
											'comments': comments,
											'new_comment': new_comment,
											'comment_form': comment_form})