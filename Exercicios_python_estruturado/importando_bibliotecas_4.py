# import dos pacotes necessários
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

# parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU EMAIL"
msg['To'] = "EMAIL PARA ENVIO"
msg['Subject'] = "ASSUNTO"

# criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

# criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login na conta para envio
server.login(msg['From'], senha)
# envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
# encerramento do servidor
server.quit()
print('Mensagem enviada com sucesso')
