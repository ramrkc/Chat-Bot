from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named shower
chatbot = ChatBot('Ram')

trainer = ListTrainer(chatbot)

trainer.train(['Hi','Hello','How are you?','I am fine and You?','Great','What are you Doing?','nothing just roaming around.'])

while True:
	input_data = input("You  ")
	response = chatbot.get_response(input_data)
	print("Ram- ",response)
