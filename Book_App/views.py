from django.shortcuts import render
from django.http import HttpResponse


def book_seat(request):
    # 座位预约
    if request.method == 'GET':
        return render(request, 'main/book_seat.html')
    elif request.method == 'POST':
        # x1 = request.POST.get('tableQ')
        zone = request.POST.get('zone')
        floor_1 = request.POST.get('floor')
        data = {
            'hh': 'hahaha',
            'name': 'Emison',
            # 'x1': x1,
            'zone': zone,
            'floor': floor_1,
        }
        return render(request, 'main/book_seat.html', context=data)


def book_record(request):
    # 预约记录
    return render(request, 'main/book_record.html')


def book_cancel(request):
    # 取消预约
    return render(request, 'main/book_cancel.html')
