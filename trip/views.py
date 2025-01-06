from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

# redirects if user is not loggedin
from django.contrib.auth.decorators import login_required # for FBV
from django.contrib.auth.mixins import LoginRequiredMixin # for CBV


from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
  template_name = 'trip/trip_home.html'


# function based view
@login_required
def trips_list(request):
  trips = Trip.objects.filter(owner=request.user)
  context = {
    'trips': trips
  }
  return render(request, 'trip/trip_list.html', context)


class TripCreateView(LoginRequiredMixin, CreateView):
  # template_name = 'trip/trip_form.html'
  model = Trip
  success_url = reverse_lazy('trip_list')
  fields = ['city', 'country', 'start_date', 'end_date']
  
  def form_valid(self, form):
    # owner field = logged in user
    form.instance.owner = self.request.user
    return super().form_valid(form)


class TripDetailView(LoginRequiredMixin, DetailView):
  model = Trip

  # data stored on trip - also have the notes data
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    trip = context['object']
    notes = trip.notes.all()
    context['notes'] = notes
    return context


class NoteDetailView(LoginRequiredMixin, DetailView):
  model = Note

 
class NoteListView(LoginRequiredMixin, ListView):
  model = Note
  
  def get_queryset(self):
    queryset = Note.objects.filter(trip__owner=self.request.user)
    return queryset


class NoteCreateView(CreateView):
  model = Note
  success_url = reverse_lazy('note_list')
  fields = '__all__'

  # since we need to restrict notes for current user only, we have to
  # overwrite the get_form object
  def get_form(self):
    form = super(NoteCreateView, self).get_form()
    trips = Trip.objects.filter(owner=self.request.user)
    form.fields['trip'].queryset = trips
    return form


class NoteUpdateView(UpdateView):
  model = Note
  success_url = reverse_lazy('note_list')
  fields = '__all__'

  # since we need to restrict notes for current user only, we have to
  # overwrite the get_form object
  def get_form(self):
    form = super(NoteUpdateView, self).get_form()
    trips = Trip.objects.filter(owner=self.request.user)
    form.fields['trip'].queryset = trips
    return form


class NoteDeleteView(DeleteView):
  model = Note
  success_url = reverse_lazy('note_list')
  
  # expect a template name model_confirm_delete.html
  # template_name = "trip/note_confirm_delete.html"
  # or you can delete without confirmation/or template - send a post request to this url


class TripUpdateView(UpdateView):
  model = Trip
  success_url = reverse_lazy('trip_list')
  fields = ['city', 'country', 'start_date', 'end_date' ]

  # No need to restrict for current user like we did with notes


class TripDeleteView(DeleteView):
  model = Trip
  success_url = reverse_lazy('trip_list')
  
  # expect a template name model_confirm_delete.html
  # template_name = "trip/trip_confirm_delete.html"
  # or you can delete without confirmation/or template - send a post request to this url