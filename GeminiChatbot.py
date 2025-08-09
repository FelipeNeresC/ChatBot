import google.generativeai as genai
import os
#Configurar a API Key
genai.configure(api_key="AIzaSyBvLBiZm_sPkrzTpngpk7BHFZ-3P-wCg0Q")

#Escolher o modelo Gemini
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Iniciar uma sessão de chat
chat = model.start_chat(history=[])

print("Olá! Eu sou o seu chatbot Gemini. Digite 'sair' para encerrar a conversa.")

while True:
    user_message = input("Você: ")

    if user_message.lower() == 'sair':
        print("Chatbot: Até mais!")
        break

    try:
        #Enviar a mensagem do usuário para o modelo e obter a resposta
        response = chat.send_message(user_message)

        #Imprimir a resposta do chatbot
        print(f"Chatbot: {response.text}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        print("Tente novamente.")