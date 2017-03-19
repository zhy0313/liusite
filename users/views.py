from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#from django.contrib.auth.
# Create your views here.
@login_required
def index(request):
    return render(request, 'users/index.html')

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainpage:index'))

