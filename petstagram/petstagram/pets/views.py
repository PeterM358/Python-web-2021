from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, 'pets/pet_list.html', context=context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    is_owner = pet.user == request.user
    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()

    context = {
        'pet': pet,
        'form': CommentForm(),
        'comments': pet.comment_set.all(),  # thus we get all comments
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,  # we give these to context so we check in html whom to show view
    }
    return render(request, 'pets/pet_detail.html', context)


@login_required
def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()

        # cmment = Comment(
        #     comment=form.cleaned_data['comment'],
        #     pet=pet,
        # )
        # comment.user = request.user
        # comment.save()  # TODO this does not work
    return redirect('pet details', pet.id)  # to return to correct pet with id


@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object_by_user = pet.like_set.filter(user_id=request.user.id).first()

    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()
    return redirect('pet details', pet.id)


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
    else:
        form = PetForm()
        context = {
            'form': form
        }
        return render(request, 'pets/pet_create.html', context)


@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = EditPetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet
        }
        return render(request, 'pets/pet_delete.html', context)
