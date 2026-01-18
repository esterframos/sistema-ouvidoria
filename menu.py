'''
Análise e Desenvolvimento de Sistemas
Programação Estruturada com Python - Prof. Daniel Abella

Ana Carolina Vasconcelos Barreto
Ester de Farias Ramos
Jadeilson Teixeira Faustino Junior
Mirelly dos Santos Silva
Pedro Henrique Araújo Ferreira
Warlley Kaio dos Santos Firmino

PROJETO OUVIDORIA
'''
from ouvidoria import *
from operacoesbd import *

conexao = criarConexao('localhost', 'root', 'ester013', 'ouvidoria')


print('========= Setor de Ouvidoria ==========')

while True:
    print('\n1. Listagem das manifestações.')
    print('2. Criar uma nova manifestação.')
    print('3. Exibir quantidade de manifestações.')
    print('4. Pesquisar uma manifestação por código.')
    print('5. Excluir uma manifestação por código.')
    print('6. Sair do Sistema.')

    opcao = input('\nDigite a opção desejada (apenas números):').strip()

    if opcao == '1':
        listarManifestacoes(conexao)

    elif opcao == '2':
        criarManifestacao(conexao)

    elif opcao == '3':
        quantidadeManifestacoes(conexao)

    elif opcao == '4':
        pesquisarManifestacao(conexao)

    elif opcao == '5':
        excluiManifestacao(conexao)

    elif opcao == '6':
        break

    else:
        print('Opção Inválida')

print('\nVocê escolheu sair do sistema')
print('Obrigada por usar o sistema de ouvidoria! Volte sempre.')

encerrarConexao(conexao)

