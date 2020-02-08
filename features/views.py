from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Feature, Comment
from .forms import FeatureCommentForm, FeaturePostForm



def features_list(request):
	"""
	This view will list all bugs starting with the most recent ones
	"""
	features = Feature.objects.order_by('-created_on').all()
	paginator = Paginator(features, 4)
	page = request.GET.get('page')
	features = paginator.get_page(page)
	return render(request, 'features/features.html', {'features': features})

def feature_detail(request, pk):
	"""
	This view allow users to see a specific bug report in a separate window
	and also to add comments to it
	"""
	# Retrive bug details
	feature = get_object_or_404(Feature, pk=pk)
	feature.views += 1
	feature.save()
	comments = feature.comments.filter(active=True)
	new_comment = None
	# Comments functionality *** credit for the code to https://djangocentral.com
	if request.method == 'POST':
		comment_form = FeatureCommentForm(data=request.POST)
		if comment_form.is_valid:
			new_comment = comment_form.save(commit=False)
			new_comment.feature = feature
			new_comment.save()
	else:
		comment_form = FeatureCommentForm
	return render(request, 'features/feature_detail.html', {'feature': feature, 
												'comments': comments,
												'new_comment': new_comment,
												'comment_form': comment_form})


@login_required
def feature_likes(request, pk):
	"""
	This view allow users to like bug reports
	"""
	feature = get_object_or_404(Feature, pk=pk)
	feature.likes += 1
	feature.save()

	return redirect('features:feature_detail', pk=feature.pk)


@login_required
def feature_add(request):
	"""
	This view allow users to submit their bug reports
	"""
	if request.method == 'POST':
		feature_form = FeaturePostForm(request.POST)
		if feature_form.is_valid:
			feature = feature_form.save(commit=False)
			feature.author = request.user
			feature.save()
			messages.success(request, 'Successfully created!')
			return redirect('features:feature_detail', pk=feature.pk)
	else:
		feature_form = FeaturePostForm()
	return render(request, 'features/feature_add.html', {'feature_form': feature_form})



@login_required
def feature_delete(request, pk):
	"""
	This view allow a user to delete a bug report, but only if is the author 
	"""
	feature = get_object_or_404(Feature, pk=pk)
	if request.user == feature.author:
		feature.delete()
		messages.success(request, 'Successfully deleted!')
	else:
		messages.error(request, 'You can\'t delete this!')
		return redirect('features:feature_detail', pk=feature.pk)

	return redirect('features:features_list')


@login_required
def feature_edit(request, pk):
	"""
	This view allow users to edit a previously submited bug report
	"""
	feature = get_object_or_404(Feature, pk=pk)
	if request.user == feature.author:
		if request.method == "POST":
			feature_form = FeaturePostForm(request.POST, instance=feature)
			if feature_form.is_valid:
				feature_form.save()
				return redirect('features:feature_detail', pk=feature.pk)
		else:
			feature_form = FeaturePostForm(instance=feature)
		return render(request, "features/feature_add.html", {"feature_form": feature_form})
	else:
		messages.error(request, 'You can\'t edit this!')
		feature_form = FeaturePostForm()
	return redirect('features:feature_detail', pk=feature.pk)


