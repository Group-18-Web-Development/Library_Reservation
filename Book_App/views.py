from django.shortcuts import render
from django.http import HttpResponse


def book_seat(request):
    # 座位预约
    return render(request, 'main/book_seat.html')


def book_record(request):
    # 预约记录
    return render(request, 'main/book_record.html')


def book_cancel(request):
    # 取消预约
    return render(request, 'main/book_cancel.html')
