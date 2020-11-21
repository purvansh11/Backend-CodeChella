from django.shortcuts import render, HttpResponse

def index(request):
   return HttpResponse("This iste")

# def reportTweet(request):
#    return render(request, "myapp/template/hello.html", {})
