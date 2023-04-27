""" Cenário indicar se aluno aprovado ou reprovado de acordo com a nora """

nota = eval(input('Digite a nota do aluno: '))

if(nota >= 7.0):
    print(f'Aluno aprovado! Sua nota foi: {nota}')
elif(nota >= 5.0):
    print(f'Aluno de recuperação com nota: {nota}')
else:
    print(f'Aluno reprovado! Sua nota foi: {nota}')
