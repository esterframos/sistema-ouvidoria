"""
Módulo responsável pelas regras de negócio do sistema de ouvidoria.
"""
from operacoesbd import *

def listarManifestacoes(conexao):
    consulta = 'select * from manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0:
        print('Nenhuma manifestação foi encontrada')
    else:
        print('\nLista de Manifestações\n')
        for item in manifestacoes:
            print(f'- Manifestação: {item[1]}. Código:{item[0]}.')

def criarManifestacao(conexao):
    descricaoManifestacao = input('Digite sua Manifestação: ').strip().capitalize()

    if not descricaoManifestacao:
        print('\nErro: A Manifestação não pode ser vazia!\n')
        return

    consulta = 'insert into manifestacoes (manifestacao) values(%s);'
    dados = [descricaoManifestacao]

    codigoNovaManifestacao = insertNoBancoDados(conexao, consulta, dados)

    if codigoNovaManifestacao:
        print(f'Manifestação registrada com Sucesso! O código da manifestação é: {codigoNovaManifestacao}.')
    else:
        print('\nErro ao registrar manifestação.\n')


def quantidadeManifestacoes(conexao):
    consulta = 'select count(*) from manifestacoes;'
    resultado = listarBancoDados(conexao, consulta)
    quantidade = resultado[0][0]

    if quantidade == 0:
        print('\nVocê ainda não criou nenhuma manifestação.\n')
    elif quantidade == 1:
        print('\nAté o momento, o sistema possui 1 manifestação.\n')
    else:
        print(f'\nAté o momento, o sistema possui {quantidade} manifestações.\n')


def pesquisarManifestacao(conexao):
    try:
        codigoManifestacao = int(input('Informe o código da manifestação para pesquisa: '))
    except ValueError:
        print('Por favor, digite um número válido.')
        return

    consulta = 'select * from manifestacoes where codigo = %s;'
    dados = [codigoManifestacao]

    resultado = listarBancoDados(conexao, consulta, dados)

    if len(resultado) > 0:
        print('\nManifestação Encontrada!\n')
        print(f'- Manifestação: {resultado[0][1]}.')
    else:
        print('\nManifestação não encontrada.\n')


def excluiManifestacao(conexao):
    try:
        codigoExcluir = int(input('Informe o código da manifestação que deseja excluir: '))
    except ValueError:
        print('\nPor favor, digite um número válido.\n')
        return

    consulta = 'delete from manifestacoes where codigo = %s;'
    dados = [codigoExcluir]

    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)

    if linhasAfetadas > 0:
        print('\nManifestação excluída com sucesso!\n')
    else:
        print('\nNenhuma manifestação encontrada com esse código.\n')

