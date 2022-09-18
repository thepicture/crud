from django.http import HttpResponse

from django.template import loader

from .models import AnimalFact


def index(request) -> HttpResponse:
    animal_fact_list = AnimalFact.objects.all()
    template = loader.get_template('animalfacts/index.html')
    context = {
        'animal_fact_list': animal_fact_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, fact_id) -> HttpResponse:
    return HttpResponse('The fact %s' % fact_id)
