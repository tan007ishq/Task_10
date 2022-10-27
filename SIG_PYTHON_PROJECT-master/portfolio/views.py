from django.shortcuts import render
from portfolio.models import portfolio
# Create your views here.
def portfolio_run(request):
    # temp = portfolio.objects.all()
    context={
        "var1" : portfolio.objects.all()
    }
    return render(request,'port.html',context)