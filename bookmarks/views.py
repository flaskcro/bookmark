# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from bookmarks.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.context_processors import csrf

def home(request):
    print request.user
    c = {}
    c.update(csrf(request))
    return render_to_response('main.html',{'user':request.user})
    #return render_to_response('main.html',c)
    '''
    template = get_template('main.html')
    variables = Context({'user': request.user})
    output = template.render(variables)
    return HttpResponse(output)
    '''

def user_page(requset, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('사용자를 찾을수 없습니다')

    bookmarks = user.bookmark_set.all()

    template = get_template('user_page.html')
    variables = Context({
        'username':username,
        'bookmarks':bookmarks
    })
    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


