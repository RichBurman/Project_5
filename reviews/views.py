from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def create_review(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.package = package
            review.save()
            return redirect('package_detail', package_id=package_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form, 'package': package})
