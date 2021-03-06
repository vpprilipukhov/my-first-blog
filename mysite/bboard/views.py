from django.http import HttpResponse
from django.shortcuts import render #?
from django.template import loader
from django.views.generic.edit import CreateView

from django.urls import  reverse_lazy

from .models import Bd, Rubric
from .forms import Bbform




def index(request):
    #tamplate = loader.get_template("bboard/index.html")
    rubrics = Rubric.objects.all()
    bds = Bd.objects.all()
    contex = {'bds': bds,'rubrics': rubrics}
    return render(request, 'bboard/index.html', contex)


def by_rubric(request, rubric_id):
    bds = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bds': bds, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request,'bboard/by_rubric.html',context)

class BdCreatView(CreateView):
    template_name = 'bboard/create.html'
    form_class = Bbform
    success_url =  reverse_lazy('index')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context












# def index(request):
#     s = "Список объявлений\r\n\r\n\r\n"
#     for bb in Bd.objects.order_by('-published'):
#         s += bb.tile + '\r\n' + bb.connect + '\r\n\r\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')
#
