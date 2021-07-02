from django.shortcuts import render

from forms_lab.info_display.forms import DisplayInfo


def display_form(request):
    if request.method == 'POST':
        form = DisplayInfo(request.POST)

        if form.is_valid():
            fields = ['name', 'age', 'email', 'password', 'text']
            # name = form.cleaned_data['name']
            # age = form.cleaned_data['age']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # text = form.cleaned_data['text']
            [print(field, form.cleaned_data[field]) for field in fields]
        else:
            print(form.errors)
    else:
        context = {
            'form': DisplayInfo()
        }
        return render(request, 'info_display/forms.html', context=context)
