from django.urls import path

from forms_lab.info_display.views import display_form

urlpatterns = [
    path('', display_form, name='show form'),
]