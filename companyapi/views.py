from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested")
    friends = ['Noman', 'Ali', 'Waqar']
    #return HttpResponse("This is home page")
    return JsonResponse(friends, safe=False)