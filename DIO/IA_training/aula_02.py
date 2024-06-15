import speech_recognition as sr
import os

# Inicializa o reconhecedor de fala (seja o que Deus quiser)
recognizer = sr.Recognizer()

# Função para reconhecer a palavra-chave informada pelo usuário :D
def recognize_keyword():
    with sr.Microphone() as source:
        print("Aguardando a palavra-chave...")
        audio = recognizer.listen(source)
        try:
            # Reconhece o áudio usando o Google Web Speech API (API é vida)
            text = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao acessar o serviço de reconhecimento de fala; {e}")
            return None

# Looping principal da brincadeira
while True:
    keyword = recognize_keyword()
    if keyword and "navegador" in keyword.lower():
        print("Palavra-chave reconhecida! Executando comando...")
        os.system('start chrome')
    
    elif keyword and "bloco de notas" in keyword.lower():
        print("Palavra-chave reconhecida! Executando comando...")
        os.system('start notepad.exe')
    
    elif keyword and "desligar o computador" in keyword.lower():
        print("Palavra-chave reconhecida! Executando comando...")
        os.system('shutdown /s /t 0')
    break
