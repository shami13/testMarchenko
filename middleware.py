from models import URL

class MiddlewareHttp():
    def process_request(self, request):
        url = URL()
        url.url = request.get_host() + request.get_full_path()
        url.save()
