from django.http import HttpResponse

from django.views.generic import TemplateView

from django.template import loader

from django.http import HttpRequest

from .models import AnimalFact, Breed, LineChartJSONView


def index(request) -> HttpResponse:
    animal_fact_list = AnimalFact.objects.all()
    template = loader.get_template('animalfacts/index.html')
    context = {
        'animal_fact_list': animal_fact_list,
    }
    return HttpResponse(template.render(context, request))


def detail(_, fact_id) -> HttpResponse:
    return HttpResponse('The fact %s' % fact_id)

def confirm(request, fact_id) -> HttpResponse:
    template = loader.get_template('animalfacts/confirm.html')
    context = {
        'fact_id': fact_id,
    }
    return HttpResponse(template.render(context, request))


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


def edit(request, fact_id) -> HttpResponse:
    template = loader.get_template('animalfacts/edit.html')
    fact = AnimalFact.objects.get(pk=fact_id)
    context = {
        'id': fact.id,
        'title': fact.title,
        'description': fact.description,
        'fact': fact.fact,
        'image': fact.image,
        'breeds': Breed.objects.all(),
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


def api_edit(request: HttpRequest) -> HttpResponse:
    post = request.POST
    fact = AnimalFact.objects.get(pk=post['id'])
    fact.title = post['title']
    fact.description = post['description']
    fact.fact = post['fact']
    fact.breed = Breed.objects.get(pk=post['breed'])
    if len(request.FILES) > 0:
        fact.image = request.FILES['image']
    fact.save()
    template = loader.get_template('animalfacts/saved.html')
    context = {}
    return HttpResponse(template.render(context, request))

popularity_chart = TemplateView.as_view(template_name='animalfacts/popularity.html')
popularity_chart_json = LineChartJSONView.as_view()