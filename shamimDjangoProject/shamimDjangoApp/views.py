from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'message': "Hello, I'm Sk Shamim Iqbal."
    }
    template_path = 'index.html'
    print(f'Trying to render template: {template_path}') #debugging
    return render(request, template_path, context)
    #return render(request, 'shamimDjangoApp/index.html', context)
