from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from social.forms import SignUpForm
import os
from django.utils.html import escape
import tmdbsimple as tmdb

tmdb.API_KEY = os.getenv('MOVIEDB_API_KEY_V3')

# Create your views here.
def index(request):
    movies = tmdb.Movies().popular()
    tvshows = tmdb.TV().popular()

    return render(request, "social/index.html",
                    {
                        "movies": movies['results'][:12],
                        "tvshows": tvshows['results'][:12]
                    }
                 )


def login_view(request):
    """Try to authenticate a user or show them an error message"""
    if  request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    errors = []
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            errors.append("Invalid credentials.")

    return render(request, "social/login.html",
        {
            "errors": errors,
            "type": "Login",
            "post_url": reverse('login'),
            "backlink": {
             "link": reverse('register'),
             "text": "Register"
             }
        })

def register(request):
    """Try and register a user using the extended UserCreationForm"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    message = []
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            for error in form.errors:
                message.append(form.errors[error])
    else:
        form = SignUpForm()

    return render(request, "social/login.html",
        {
            "errors": message,
            "type": "Register",
            "register" : True,
            "post_url": reverse('register'),
            'form': form,
            "backlink": {
                 "link": reverse('login'),
                 "text": "Login"
             }
        })

def details(request, type, id):
    print(f"{type} - {id}")
    types = {
        'movie': tmdb.Movies,
        'tv' : tmdb.TV
    }
    data = types[type](id)

    recommendations_data = data.recommendations()
    recommendations = recommendations_data['results'][:6]
    videos = data.videos()
    # print(data.info())
    return render(request, "social/details.html",
                {
                    "data": data.info(),
                    "recommendations": recommendations,
                    "videos" : videos,
                    "type": type
                })


def search(request):
    if request.method == 'POST':
        query = request.POST['search-term']
        print(escape(query))
        data = tmdb.Search().multi(query=escape(query))

    return render(request, "social/search.html", { "results": data['results'], "search": escape(query)} )

def logout_view(request):
    """
        Sign the user out
    """
    logout(request)
    return render(request, "social/login.html",
        {
            "errors": ["Logged out."],
            "type": "Login",
            "post_url": reverse('login'),
            "backlink": {
                "link": reverse('register'),
                "text": "Register"
            }
        })


def account_index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "social/account_index.html", {})
