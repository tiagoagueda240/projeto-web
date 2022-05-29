from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

from .models import *
from .forms import PostForm

def home_page_view(request):
	return render(request, 'portfolio/home.html')


def sobre_mim_view(request):
	return render(request, 'portfolio/sobre-mim.html', {'cadeiras': Cadeira.objects.all(), 'educacao': Formacao.objects.all(),
     'competencias': Competencia.objects.all(),
      'linguas': Lingua.objects.all(),
      'interesses': Interesse.objects.all()})

def projetos_view(request):
	return render(request, 'portfolio/projetos.html', {'projetos': Projeto.objects.all()})

def web_view(request):
	return render(request, 'portfolio/web.html', {'tecnologias': Tecnologia.objects.all(), 'laboratorios': Laboratorio.objects.all(), 'noticias' : Noticia.objects.all()})

def blog_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/blog.html', context)

def contactos_view(request):
	return render(request, 'portfolio/contactos.html')

def login_view(request):
	return render(request, 'portfolio/login.html')


def nova_tarefa_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/criar.html', context)


def edita_tarefa_view(request, tarefa_id):
    tarefa = Post.objects.get(id=tarefa_id)
    form = PostForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'portfolio/editar.html', context)


def apaga_tarefa_view(request, tarefa_id):
    Post.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def resultados_quizz(request):
    pontuacao = 0
    nome = request.POST['nome']
    apelido = request.POST['apelido']
    resposta1 = request.POST['resposta1']
    resposta2 = request.POST['resposta2']
    resposta3 = request.POST['resposta3']
    resposta4 = request.POST['resposta4']

    if resposta1 == "1" :
        pontuacao += 25

    if resposta2 == "2" or resposta2 == "2" :
        pontuacao += 25

    if resposta3 == "3" or resposta3 == "3" :
        pontuacao += 25 
    
    if resposta4 == "4" or  resposta4 == "4" :
        pontuacao += 25

    return pontuacao

def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao, reverse=True)     
    nomes = []     
    pontuacoes = []     
    for pt in participantes:         
        nomes.append(pt.nome +" "+pt.apelido)         
        pontuacoes.append(pt.pontuacao)     
        plt.barh(nomes, pontuacoes)     
        plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')


def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        a = request.POST['apelido']
        p = resultados_quizz(request)
        r = PontuacaoQuizz(nome=n, apelido=a, pontuacao=p)
        r.save()
    context = {
        'pontuacao': p,
        'tecnologias': Tecnologia.objects.all(), 
        'laboratorios': Laboratorio.objects.all(), 
        'noticias' : Noticia.objects.all()
    }
    desenha_grafico_resultados()
    return render(request,'portfolio/web.html',context)