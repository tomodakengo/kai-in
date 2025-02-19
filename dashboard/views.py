from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from members.models import Member
from associations.models import Association
from clubs.models import Club
from payments.models import Payment
from .models import Notification

# Create your views here.

@login_required
def home(request):
    context = {
        'total_members': Member.objects.count(),
        'total_associations': Association.objects.count(),
        'total_clubs': Club.objects.count(),
        'recent_payments': Payment.objects.order_by('-created_at')[:5],
        'notifications': Notification.objects.filter(user=request.user, is_read=False)[:5],
    }
    return render(request, 'dashboard/home.html', context)
