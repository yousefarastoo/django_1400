from . import jalali
from django.utils import timezone

def convert_number(number):
    persian_Number = ["۰","۱","۲","۳","۴","۵","۶","۷","۸","۹"]
    output =""
    for i in str(number):
        output += persian_Number[int(i)]
    return output

def jalali_convertor(time):
    time = timezone.localtime(time)
    jmonth = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    time_to_str = "{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = "{} {} {} | ساعت {}:{}".format(
        convert_number(time_to_tuple[2]), jmonth[time_to_tuple[1]-1], convert_number(time_to_tuple[0]), convert_number(time.hour), convert_number(time.minute))
    return output
