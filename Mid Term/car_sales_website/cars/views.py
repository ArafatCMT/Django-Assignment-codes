from django.shortcuts import render, redirect
from django.views.generic import DetailView
from cars import models
from cars import forms
from orders.forms import OrderForm
from orders.models import Order
# Create your views here.

class CarDetailView(DetailView):
    model = models.CarModel
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object() # jei post e comment kora hobe oi post ta store korlam
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object() # jei post e comment kora hobe oi post ta store korlam
        comments = post.comments.all() #ei khan e post er moddhe joto gula comnt age sob store kore rakha hocca
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def PostUpdateView(request, id):
    post = models.CarModel.objects.get(pk=id)
    quentity = post.quentity - 1
    post.quentity = quentity
    post.save()

    #order model er object create kora hocca
    order = Order(carID=id, userID = request.user.id)
    order.save()

    return redirect('details', id)



