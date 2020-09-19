import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Relation, Activity, Photo
from .forms import CommunicationForm

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'first-bgq'

class RelationCreate(CreateView):
  model = Relation
  fields = ['name', 'relation_type', 'description', 'age']

class RelationUpdate(UpdateView):
  model = Relation
  fields = ['relation_type', 'description', 'age']

class RelationDelete(DeleteView):
  model = Relation
  success_url = '/relations/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def relations_index(request):
  relations = Relation.objects.all()
  return render(request, 'relations/index.html', { 'relations': relations })

def relations_detail(request, relation_id):
  relation = Relation.objects.get(id=relation_id)
  activitys_relation_doesnt_have = Activity.objects.exclude(id__in = relation.activitys.all().values_list('id'))
  communication_form = CommunicationForm()
  return render(request, 'relations/detail.html', {
    'relation': relation, 'communication_form': communication_form,
    'activitys': activitys_relation_doesnt_have
  })

def add_communication(request, relation_id):
  form = CommunicationForm(request.POST)
  if form.is_valid():
    new_communication = form.save(commit=False)
    new_communication.relation_id = relation_id
    new_communication.save()
  return redirect('detail', relation_id=relation_id)

def assoc_activity(request, relation_id, activity_id):
  Relation.objects.get(id=relation_id).activitys.add(activity_id)
  return redirect('detail', relation_id=relation_id)

def unassoc_activity(request, relation_id, activity_id):
  Relation.objects.get(id=relation_id).activitys.remove(activity_id)
  return redirect('detail', relation_id=relation_id)

class ActivityList(ListView):
  model = Activity

class ActivityDetail(DetailView):
  model = Activity

class ActivityCreate(CreateView):
  model = Activity
  fields = '__all__'

class ActivityUpdate(UpdateView):
  model = Activity
  fields = ['name', 'color']

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activitys/'

def add_photo(request, relation_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      Photo.objects.create(url=url, relation_id=relation_id)
    except:
      print('An error occured uploading file to S3')
  return redirect('detail', relation_id=relation_id)
