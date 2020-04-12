from django.http import HttpResponse
def index(request):
    output = "welCome to Our SiTE"
    return HttpResponse(output)
def detail(request, question):
    return HttpResponse("We got your query :: %s." % question)
def answer(request):
    question_id = 1456
    return HttpResponse("You're looking at answer for Q No %s." % question_id)
