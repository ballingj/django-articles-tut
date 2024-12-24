from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# needed for class based Forms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Models
from .models import Profile, LinkPlant


# Classbased view
class LinkPlantListView(ListView):
  # in function based view, we have to....
  # links = query for all the link_plant
  # context={'link' : links}
  # return render(request, 'link_list.html', context)
  
  model = LinkPlant
  # by default this will look for model_list.html -> so linkplant_list.html
  

class LinkPlantCreateView(CreateView):
  # in function based view, we have to....
  # creating forms.py file and form
  # check if post or get request
  # return an empty form or save the form data
  
  # by default django will look for a template called a <model-name>_form -> linkplant_form.html
  # but we can customize the template name
  # template_name = "link_plant/linkplant_form.html"
  model = LinkPlant
  fields = "__all__"
  success_url = reverse_lazy('link_plant_list')


class LinkPlantUpdateView(UpdateView):
  # in function based view, we have to....
  # create a form
  # check if GET or a POST request
  # either render or update and save in db
  
  # template name is default
  # template_name = "link_plant/link_plant_form.html"
  model = LinkPlant
  fields = ['text', 'url']
  success_url = reverse_lazy("link_plant_list")
  # context_object_name = "link_plant"


class LinkPlantDeleteView(DeleteView):
  # in function based view, we have to....
  # take id of an object
  # query db for that object
  # check if exists -> delete the object
  
  # expect a template name model_confirm_delete.html
  # template_name = "link_plant/linkplant_confirm_delete.html"
  model = LinkPlant
  success_url = reverse_lazy("link_plant_list")
  # context_object_name = "link_plant"


## external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)