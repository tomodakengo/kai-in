from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Association, AssociationMember
from .forms import AssociationForm, AssociationMemberForm

# Create your views here.

@login_required
def association_list(request):
    associations = Association.objects.all().order_by('name')
    paginator = Paginator(associations, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'associations': page_obj,
    }
    return render(request, 'associations/list.html', context)

@login_required
def association_detail(request, pk):
    association = get_object_or_404(Association, pk=pk)
    context = {
        'association': association,
    }
    return render(request, 'associations/detail.html', context)

@login_required
def association_create(request):
    if request.method == 'POST':
        form = AssociationForm(request.POST)
        if form.is_valid():
            association = form.save()
            messages.success(request, '協会を登録しました。')
            return redirect('associations:detail', pk=association.pk)
    else:
        form = AssociationForm()
    
    context = {
        'form': form,
        'is_create': True,
    }
    return render(request, 'associations/form.html', context)

@login_required
def association_update(request, pk):
    association = get_object_or_404(Association, pk=pk)
    if request.method == 'POST':
        form = AssociationForm(request.POST, instance=association)
        if form.is_valid():
            form.save()
            messages.success(request, '協会情報を更新しました。')
            return redirect('associations:detail', pk=association.pk)
    else:
        form = AssociationForm(instance=association)
    
    context = {
        'form': form,
        'association': association,
        'is_create': False,
    }
    return render(request, 'associations/form.html', context)

@login_required
def member_add(request, pk):
    association = get_object_or_404(Association, pk=pk)
    if request.method == 'POST':
        form = AssociationMemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.association = association
            member.save()
            messages.success(request, '会員を追加しました。')
            return redirect('associations:detail', pk=association.pk)
    else:
        form = AssociationMemberForm()
    
    context = {
        'form': form,
        'association': association,
    }
    return render(request, 'associations/member_form.html', context)

@login_required
def member_remove(request, pk, member_pk):
    association = get_object_or_404(Association, pk=pk)
    member = get_object_or_404(AssociationMember, association=association, member_id=member_pk)
    if request.method == 'POST':
        member.delete()
        messages.success(request, '会員を削除しました。')
    return redirect('associations:detail', pk=association.pk)
