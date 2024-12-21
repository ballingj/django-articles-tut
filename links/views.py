from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import LinkForm

# Create your views here.
def links_list(request):
  links = Link.objects.all()
  context = {
    'links': links
  }
  return render(request, 'links/links_list.html', context)

def root_link(request, link_slug):
  link = get_object_or_404(Link, slug=link_slug)
  link.click()  # this will increment the clicked field
  
  return redirect(link.url)

# Link Create View
def link_create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links_list')
    else:
        form = LinkForm()
    return render(request, 'links/link_create.html', {'form': form})
