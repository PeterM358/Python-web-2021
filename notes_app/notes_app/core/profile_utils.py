from notes_app.notes.models import Note
from notes_app.profiles.models import Profile


def get_profile():
    profile = Profile.objects.first()
    return profile
