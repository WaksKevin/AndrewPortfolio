from .models import SiteInfo, Author


def base(request):
    return {
        "site": SiteInfo.objects.first(),
        "author": Author.objects.first(),
    }
