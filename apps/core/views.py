from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def entry(request):
    return Response('ok')
