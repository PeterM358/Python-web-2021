from django.shortcuts import render, redirect

from notes_app.core.profile_utils import get_profile
from notes_app.notes.models import Note
from notes_app.profiles.forms import CreateProfileForm


def profile_info(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.count_notes = len(notes)
    context = {
        'profile': profile,
        'notes_count': profile.count_notes
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    if request.method == 'POST':
        profile.delete()
        notes.delete()
        return redirect('home page')
    return render(request, 'profile_delete.html')
