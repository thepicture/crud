from django.http import HttpResponse

from django.template import loader

from django.http import HttpRequest

from .models import AnimalFact, Breed


def index(request) -> HttpResponse:
    animal_fact_list = AnimalFact.objects.all()
    template = loader.get_template('animalfacts/index.html')
    context = {
        'animal_fact_list': animal_fact_list,
    }
    return HttpResponse(template.render(context, request))


def detail(_, fact_id) -> HttpResponse:
    return HttpResponse('The fact %s' % fact_id)


def delete(request, fact_id) -> HttpResponse:
    AnimalFact.objects.get(pk=fact_id).delete()
    template = loader.get_template('animalfacts/deleted.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create(request) -> HttpResponse:
    template = loader.get_template('animalfacts/create.html')
    context = {
        'breeds': Breed.objects.all()
    }
    return HttpResponse(template.render(context, request))


def api_create(request: HttpRequest) -> HttpResponse:
    post = request.POST
    fact = AnimalFact(title=post['title'],
                      description=post['description'],
                      fact=post['fact'],
                      breed=Breed.objects.get(pk=post['breed']),
                      image=request.FILES['image'])
    fact.save()
    template = loader.get_template('animalfacts/saved.html')
    context = {}
    return HttpResponse(template.render(context, request))
