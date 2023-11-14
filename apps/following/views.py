from django.shortcuts import render

# Create your views here.
@require_http_methods(["POST"])
def follow(request, username):
    u = User.objects.get(username__iexact=username)
    Relationship.objects.create(from_user=request.user, to_user=u, status=1)
    return redirect('/')


@require_http_methods(["POST"])
def unfollow(request, username):
    u = User.objects.get(username__iexact=username)
    Relationship.objects.get(from_user=request.user, to_user=u, status=1).delete()
    return redirect('/')
