from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def buy_now(request, id):
    car = models.Car.objects.get(pk=id)
    owner, create = models.Owner.objects.get_or_create(owner=request.user)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        if car not in owner.purchased_cars.all():
            owner.purchased_cars.add(car)
        messages.success(request, "You have bought the car successfully")
        return redirect("profile")
    else:
        messages.warning(request, "The car is out of the stock")
        return redirect("home")
