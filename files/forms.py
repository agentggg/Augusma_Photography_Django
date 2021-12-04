from django import forms
from .models import identity


class identity(forms.ModelForm):
#Classes are used to construct the form that you want to build, and assign it to the correct attribute
  class Meta:
#Not sure what this does, but it is important
    model = identity
#Uses the model Owner
    fields = ("first_name", "last_name", "gender", "age",)
#Fields entry


#Goes in views

from .forms import identity
#   Import your form name

class identity(CreateView):
    #Create a class for this form
    #The class is usually named after the form and the view that it is using
    model = identity
    #Assign the model that we want to use
    template_name = "web_app_1/contact.html"
    #The template name that the form will be populated in
    form_class = identity
    #The name of the class that we created in the forms.py file


#goes into urls
path('contactme', views.identity.as_view(), name="identity"),


#goes into contact
{% block body %}
  <div class="row">
    <div class="col-4 text-center mx-auto fs-1">
  <form method="POST">
    <!-- Form creation with post. No method "post" needed -->
    {% csrf_token %}
    <!-- Insert token -->
    {{ form | crispy }}
    <!-- form variable -->
    <input type="submit">
    <!--  Form input submission -->
  </form>
</div>
</div>
{% endblock %}
