from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, redirect
from blog.models import Post, PostForm
from django.core.context_processors import csrf
from django.template import RequestContext

def home(request):
	try:
		p = Post.objects.all()
	except Post.DoesNotExist:
		raise Http404
	return render_to_response('index.html',
		{'post':p})

def post(request, uID):
	try:
		p = Post.objects.get(pk=uID)
	except:
		raise Http404
	return render_to_response('post.html',
		{'post':p})

def delete(request, uID):
	try:
		p = Post.objects.get(pk=uID).delete()
	except:
		raise Http404
	return render_to_response('delete.html',
		{'post':p})

def new(request):
	form = PostForm()
	return render_to_response('new.html', {'form': form}, 
	 context_instance=RequestContext(request))

def added(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			t = form.cleaned_data['text']
			p = Post.objects.create(text=t)
			p.save()
			return redirect("/" + str(p.id),
			 context_instance=RequestContext(request))
		else:
			raise Http404
	else:
		raise Http404