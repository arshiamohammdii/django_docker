from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Url

# Create your views here.
def index(request):
    return HttpResponse("this page is testing")


@api_view(['POST'])
def url_shortener(request):
    """
    #input is going to be a url 
    #get the hash outcome of the original url
    #save it to the database
    #return Succes and the shorturl in s/<int:hash>
    """
    domain = request.META['HTTP_HOST']
    if request.url:
        url = Url(original_url=request.url)





    return Response({'message': 'helooooooo url', 'data': request.META['HTTP_HOST']})



@api_view()
def redirect_to_orginal(request, hash):
    """
    #query the url
    #check for expiration
        #if expired: return url not available and delete the column
    #else 
        #redirect to the right url
    """
    return Response({'message': 'helooooooo url', 'data': hash})