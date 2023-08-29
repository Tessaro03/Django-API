from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    ''' Mostrando Lista de Alunos '''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
    ''' 
    ----- Utilizado para autenticação de Usuario -----
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] 
    '''

class CursosViewSet(viewsets.ModelViewSet):
    ''' Mostrando Lista de Cursos '''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

class MatriculaViewSet(viewsets.ModelViewSet):
    ''' Mostrando Lista de Matriculas '''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    


class ListaMatriculasAluno(generics.ListAPIView):
    ''' Mostrando a Lista de Matricula do Aluno especifico'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
   

class ListaAlunosMatriculados(generics.ListAPIView):
    ''' Mostrando a Lista de Matricula do Curso especifico'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
   