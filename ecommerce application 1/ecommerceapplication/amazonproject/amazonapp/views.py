from django.shortcuts import render
from amazonapp.models import Amazon
# Create your views here.
def access(request):
    amazon=Amazon.objects.all()
    return render(request,'amazonapp/mini.html',{'amazon':amazon})