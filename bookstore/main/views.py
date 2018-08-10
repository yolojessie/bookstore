from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse

# Create your views here.

def main(request):
    import datetime
    now = datetime.datetime.now()
    hour = datetime.datetime.now().hour
    context = {'now':now,'hour':hour}
    return render(request, 'main/main.html', context)


def contact(request):
    import datetime
    now = datetime.datetime.now()
    context = {'now':now}
    return render(request, 'main/contact.html', context)

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth


