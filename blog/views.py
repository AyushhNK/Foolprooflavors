from django.shortcuts import render
from django.views import generic
from .models import RecipePost
from .forms import SignUpForm
from django.contrib.auth import login

class RecipePostList(generic.ListView):
    queryset = RecipePost.objects.filter(status=1)
    template_name = "recipepost_list.html"

def RegisterUserView(request):
	if request.method=="POST":
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect("home")
	else:
		form=SignUpForm()
	return render(request,"registeruser.html",{"form":form})
