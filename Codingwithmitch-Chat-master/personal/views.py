from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from account.models import Account
from django.contrib.auth.decorators import login_required

DEBUG = False


@login_required(login_url='/login/')
def home_screen_view(request):
	context = {}
	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	context['room_id'] = "1"
	accounts = Account.objects.all()[:40]
	context['accounts'] = accounts
	# account_id=11;
	# a=accounts.raw('SELECT * FROM friend_friendlist_friends WHERE account_id = %d', [account_id])
	# print(a)
	# print("fhgjdfhgj");


	return render(request, "personal/home.html", context)















