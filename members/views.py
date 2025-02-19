from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Member
from .forms import MemberForm

# Create your views here.

@login_required
def member_list(request):
    members = Member.objects.all().order_by('last_name_kana', 'first_name_kana')
    paginator = Paginator(members, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'members/list.html', context)

@login_required
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    context = {
        'member': member,
    }
    return render(request, 'members/detail.html', context)

@login_required
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.success(request, '会員を登録しました。')
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm()
    
    context = {
        'form': form,
        'is_create': True,
    }
    return render(request, 'members/form.html', context)

@login_required
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, '会員情報を更新しました。')
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)
    
    context = {
        'form': form,
        'member': member,
        'is_create': False,
    }
    return render(request, 'members/form.html', context)

@login_required
def profile(request):
    member = get_object_or_404(Member, user=request.user)
    return render(request, 'members/profile.html', {'member': member})
