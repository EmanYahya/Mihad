from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product, Review
from products.forms import ReviewForm

@login_required
def create_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            comment = form.cleaned_data.get('comment')
            review = Review.objects.create(
                user=request.user,
                product=product,
                rating=rating,
                comment=comment,
            )
            messages.success(request, 'Your review has been added.')
            return redirect('product_detail', product.slug)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'reviews/create_review.html', context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        messages.error(request, 'You do not have permission to edit this review.')
        return redirect('product_detail', review.product.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect('product_detail', review.product.slug)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'product': review.product,
        'review': review,
    }

    return render(request, 'reviews/edit_review.html', context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        messages.error(request, 'You do not have permission to delete this review.')
        return redirect('product_detail', review.product.slug)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        return redirect('product_detail', review.product.slug)

    context = {
        'product': review.product,
        'review': review,
    }

    return render(request, 'reviews/delete_review.html', context)

