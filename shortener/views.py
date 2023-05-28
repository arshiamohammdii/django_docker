from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Url
from .serializers import UrlSerializer
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
    try:
        url = Url(original_url=request.data["url"])
        url.save()
        url_serializer = UrlSerializer(url, many=False)

        return Response(data={'success': True, 'data': url_serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(data={'success': False, 'message': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)




@api_view()
def redirect_to_orginal(request, hash):
    """
    #query the url
    #check for expiration
        #if expired: return url not available and delete the column
    #else 
        #redirect to the right url
    """
    try:
        # url_query = Url.objects.filter(hash=hash).filter(expiration_date__gt=datetime.now())
        # if url_query:
        #     okay_url = url_query.values_list("short_url", flat=True).first()
        #     return HttpResponseRedirect(okay_url)
        # else:
        #     url_query = Url.objects.filter(hash=hash).filter(expirations_date_lt=datetime.now())
        #     if url_query:
        #         url_query.delete()
        #         return Response({"error": "url was not found"})
        url = Url.objects.filter(hash=hash).first()
        return HttpResponseRedirect(url.original_url)
    except Exception as e:
        return Response(data={'error': e})
        