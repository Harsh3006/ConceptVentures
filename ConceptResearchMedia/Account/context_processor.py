from ConceptResearchMedia.Account.models import BasicDetails

def get_profile_picture(request):
    if request.user.is_authenticated:
        try:
            current_user = BasicDetails.objects.get(user=request.user)
            if (current_user.profile_picture):
                profile_picture = current_user.profile_picture.url
            else:
                profile_picture = None
        except BasicDetails.DoesNotExist:
            profile_picture = None
    else:
        profile_picture = None
    return {
        'profile_picture': profile_picture
    }