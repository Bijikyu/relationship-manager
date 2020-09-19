from django.db import models
from django.urls import reverse
from datetime import date

COMMUNICATIONS = (
    ('T', 'Text'),
    ('C', 'Call'),
    ('E', 'Email')
)

class Activity(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('activitys_detail', kwargs={'pk': self.id})

class Relation(models.Model):
  name = models.CharField(max_length=100)
  relation_type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  activitys = models.ManyToManyField(Activity)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'relation_id': self.id})

  def contacted_for_today(self):
    return self.communication_set.filter(date=date.today()).count() >= len(COMMUNICATIONS)

class Communication(models.Model):
  date = models.DateField('communication date')
  contact_method = models.CharField(
    max_length=1,
    choices=COMMUNICATIONS,
    default=COMMUNICATIONS[0][0]
  )
  relation = models.ForeignKey(Relation, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_contact_method_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  relation = models.ForeignKey(Relation, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for relation_id: {self.relation_id} @{self.url}"

