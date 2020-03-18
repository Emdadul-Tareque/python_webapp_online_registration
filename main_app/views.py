from django.http import HttpRequest
from django.shortcuts import render

from main_app.models import registration


def index(request: HttpRequest):
    error = {}
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if not len(phone_number) == 11:
            error['phone'] = "ফোন নাম্বারটি ভুল"
        if len(name) <= 2:
            error['name'] = "নাম অবশ্যই দুই অক্ষরের বেশি হতে হবে"
        if not email:
            error['email'] = "ইমেল ফিল্ডটি পূরণ করুন"

    success = request.method == "POST" and not error
    if success:
        count = len(registration.objects.all())
        count += 1
        student = registration(count,
                               count,
                               request.POST.get('name'),
                               request.POST.get('email'),
                               request.POST.get('phone'),)

        student.save()

    else:
        student = None

    return render(request, 'index.html', context={'error': error, 'ticket': student})
