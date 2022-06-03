from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    funcao = [
        ('aluno', 'aluno'),
        ('professor', 'professor'),
    ]
    nome = models.CharField(max_length=64)
    apelido = models.CharField(max_length=64)
    funcao = models.CharField(max_length = 20, choices= funcao,  blank=True)
    linkLusofona = models.URLField(max_length = 200, blank=True)
    linkLinkedin = models.URLField(max_length = 200, blank=True)

    def __str__(self):
        return f"{self.nome} {self.apelido}"


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Pessoa, on_delete = models.CASCADE, related_name = "autor")
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, blank=True)
    imagem = models.ImageField()

    def __str__(self):
        return self.titulo[:50]

class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)
    acronimo = models.CharField(max_length=20,  blank=True)
    ano = models.DateField()
    criador = models.CharField(max_length=20)
    logo = models.ImageField()
    link = models.URLField(max_length = 200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome[:50]

    
class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao =  models.TextField(max_length=5000)
    imagem = models.ImageField(upload_to="projetos")
    ano = models.DateField()
    participantes = models.ManyToManyField(Pessoa)
    linkGithub = models.CharField(max_length=1000,  blank=True)
    linkYoutube = models.CharField(max_length=1000,  blank=True)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo[:50]



class Cadeira(models.Model):
    ano = [
        ('ano1', '1'),
        ('ano2', '2'),
        ('ano3', '3'),
    ]

    semestre = [
        ('sem1', '1'),
        ('sem2', '2'),
    ]

    rank = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
    ]

    nome = models.CharField(max_length=40)
    anoLectivo = models.CharField(max_length=4,choices= ano, default='1')
    semestre = models.CharField(max_length=4,choices= semestre)
    ano = models.IntegerField(default=2021)
    ects = models.IntegerField()
    topicosAbordados = models.TextField(max_length=1000, blank=True)
    linguagens = models.ManyToManyField(Tecnologia, blank=True)
    ranking = models.CharField(max_length=2,choices= rank)
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='caderias')
    link = models.URLField(max_length = 200)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome[:50]

class Competencia(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    projetos = models.ManyToManyField(Projeto)
    disciplinas = models.ManyToManyField(Cadeira)
    
    def __str__(self):
        return self.titulo[:50]



class Interesse(models.Model): #quem sou 3
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField()
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.titulo[:50]


class Laboratorio(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.titulo[:50]


class Formacao(models.Model): #quem sou 2
    curso = models.CharField(max_length=50)
    local = models.CharField(max_length=50)
    inicio = models.CharField(max_length=50)
    fim = models.CharField(max_length=50)
    imagem = models.ImageField()

    def __str__(self):
        return self.curso[:50]


class Lingua(models.Model):
    niveis = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]
    nome = models.CharField(max_length=50)
    nivel = models.CharField(max_length=5, choices= niveis)

    def __str__(self):
        return self.nome[:50]


class PontuacaoQuizz(models.Model):     
   nome = models.CharField(max_length=30)    
   apelido = models.CharField(max_length=30)     
   pontuacao = models.IntegerField()

   def __str__(self):
      return self.nome[:50]


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    imagem = models.ImageField()

    def __str__(self):
        return self.titulo[:50]


class Tfc(models.Model):
    autor = models.ManyToManyField(Pessoa, on_delete = models.CASCADE, related_name = "autor")
    orientadores = models.ManyToManyField(Pessoa, related_name='orientadores')
    ano = models.IntegerField(default=2021)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=1000)
    imagem = models.ImageField()
    relatorio = models.CharField(max_length=1000)
    linkGithub = models.CharField(max_length=1000)
    video = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo[:50]