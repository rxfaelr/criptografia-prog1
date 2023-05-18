print('Seja bem-vindo, escolha uma opção:')
print('1. Cifra Reversa')
print('2. Cifra de César')
print('3. Encerrar programa')
escolha = int(input())

if (escolha == 1):
    print('A Cifra Reversa trata-se de um método bem simples para encriptar determinadas mensagens, essa técnica se consiste em receber uma certa mensagem do usuário e inverte-la por completa, assim distorcendo a mensagem. Porém a Cifra Reversa não é usada por um motivo bem óbvio: Ela não protege em nada a mensagem que foi digita, se essa mensagem for interceptada por um Cracker ele rapidamente irá descobrir a mensagem')
    print('Digite a mensagem a ser encriptada')
    mensagem = input()
    invertido = ""
    i = len(mensagem) - 1
    while(i >= 0):
     invertido = invertido + mensagem[i]
     i = i - 1
    print("Mensagem original invertida: " + invertido)
    print('A mensagem original é: ' + mensagem)
    
elif (escolha == 2):
    print('A Cifra de César é uma técnica de criptografia bastante simples e provavelmente a mais conhecida de todas, trata-se de um tipo de cifra de substituição, na qual cada letra de um texto a ser criptografado é substituída por outra letra, presente no alfabeto, porém deslocada um certo número de posições à esquerda ou à direita de acordo com uma chave definida previamente. A cifra de César recebe esse nome pois, segundo o escritor Suetônio, foi utilizada por Júlio César para se comunicar com seus generais, protegendo mensagens militares. Essa cifra é uma cifra de substituição monoalfabética, o que significa que cada letra do texto plano é substituída por uma outra letra do alfabeto, por conta disso, ela acaba sendo extremamente simples de ser decifrada e nunca é utilizada na prática, pois não possui absolutamente nenhuma segurança')
    message = input('Insira a mensagem a ser encriptada: ')
    key = int(input('Insira a chave para a encriptação: '))
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    message = message.upper()
    for symbol in message:
     if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num + key
         if num >= len(LETTERS):
             num = num - len(LETTERS)
         elif num < 0:
             num = num + len(LETTERS)
         translated = translated + LETTERS[num]
     else:
         translated = translated + symbol
    print(translated)
    print('A mensagem original é: ' + message)
elif (escolha == 3):
    print('Programa encerrado.')
else:
    print('Selecione uma opção válida.')
