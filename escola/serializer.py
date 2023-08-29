from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from .validators import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno 
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Somente Letras'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "Já Cadastrado"})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF Invalido'})
        return data 

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Aluno
        fields = ['aluno_nome']
    