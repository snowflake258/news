from management.models import Category


class CategoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.categories = Category.objects.all()
        response = self.get_response(request)
        return response
