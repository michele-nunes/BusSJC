#RODANDO EM PYTHON 2.7.12
import telegram
import ConfigParser
import requests
import json
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters


#Setando BOT apartir de INI
config = ConfigParser.ConfigParser()
config.read('config.ini')

#Pegando TOKEN BOT TELEGRAM
TKB = config.get('DEFAULT','token')

#UNINDO URL BOT + TOKEN
url = 'https://api.telegram.org/bot' + TKB


#CONECTANDO AO SERVIDO REDIS EASY PEASY
#BD = redis.StrictRedis(host = config.get('DB','host'),
#					   port = config.getint('DB', 'port'),
#					   db = config.getint('DB', 'db'))

#FUNCÇÃO QUE INICIA O BOT COM /START
def start(bot, update):
	update.message.reply_text("Qual onibus tu deseja pegar o horario?")

#FUNCAO DE COMANDO /AJUDA
def ajuda (bot, update):
	update.message.reply_text("Temos dois horarios disponiveis no momento!")

#FUNCAO DE COMANDO /AJUDA
def tesouro (bot, update):
	update.message.reply_text("De segunda-feira a sexta-feira 05:00,05:25, 05:40, 05:55, 07:25, 07:45, 08:05, 08:25, 08:45, 09:05, 09:25, 09:45, 10:05, 10:25, 10:45, 11:05, 11:25, 11:45, 11:55")
	update.message.reply_text("15:00")
def tesouroTarde (bot,update):
        update.message.reply_text("15:00")

#FACA A FUNCAO AQUI EM CIMA 	
#FUNCAO QUE RETORNA TEXTO PRO USUARIO
def escre(bot, update):
	update.message.reply_text(update.message_text)

getME = requests.get(url+'/getMe')
if(getME.status_code == 200 ):
	bot = json.loads(getME.content.decode('latin1'))
	print bot['result']['first_name']
	nome = bot['result']['first_name'].lower()


def main():
#CONECTANDO API TELGRAM
#UPDATE RECEBE MENSAGEM
#DISPATCHER RECEBE COMANDOS
	updater = Updater(token = TKB)
	dispatcher = updater.dispatcher

#CRIANDO OS HANDLERS DE CADA COMANDO DO USUARIO
	dispatcher.add_handler(CommandHandler("start",start))
	dispatcher.add_handler(CommandHandler("ajuda", ajuda))
	dispatcher.add_handler(CommandHandler("tesouro", tesouro))
	dispatcher.add_handler(CommandHandler("tesouroTarde", tesouroTarde))

#CASO O USUSARIO NAO DIGITE NENHUM DESSES COMANDOS ELE SOMENTE RETORNA O QUE ELE DISSE
	dispatcher.add_handler(MessageHandler([Filters.text], escre))
#COMANDO QUE FAZ O BOT FAZER UPDATE.
	updater.start_polling()
	updater.idle()
#GABIARRA DE POO PRA RODAR O MAIN !! xD
if __name__ == '__main__':
	main()
