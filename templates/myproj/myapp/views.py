
from django.shortcuts import render
from django.template  import loader
from django.shortcuts import render
# Create your views here.




def prismarea(request):
    context={}
    context['area'] = "0"
    context['s'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        s = request.POST.get('side','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Side=',s)
        print('Height=',h)
        area = 2*int(s)*int(s) + 4*int(h)*int(s)
        context['area'] = area
        context['s'] = s
        context['h'] = h
        print('Area=',area)
    return render(request,'myapp/math.html',context)

