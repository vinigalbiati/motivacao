import google.generativeai as genai
import tweepy

# Chaves de API e tokens do Twitter
consumer_key="CONSUMER KEY DO USUARIO"
consumer_secret="CONSUMER SECRET KEY DO USUARIO"
access_token="ACCESS TOKEN DO USUARIO"
access_token_secret="ACCESS TOKEN SECRET DO USUARIO"

apiv2 = tweepy.Client(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token=access_token,
                      access_token_secret=access_token_secret)

# Chave da API do Gemini
genai.configure(api_key='CHAVE DA API DO GEMINI')

# Função para gerar uma frase motivacional
def gerar_frase_motivacional():
    model = genai.GenerativeModel('models/gemini-pro')
    response = model.generate_content('gere uma frase motivacional curta e insira emojis condizentes')
    frase_motivacional = response.text
    return frase_motivacional


# Função para postar uma frase motivacional
def postar_frase_motivacional():

    # Gera a frase motivacional
    frase = gerar_frase_motivacional()

    # Publica a mensagem no Twitter
    try:
        apiv2.create_tweet(text=frase)
        print("Frase motivacional postada com sucesso:\n ", frase)
    except:
        print("Erro ao postar frase motivacional")

if __name__ == "__main__":
    postar_frase_motivacional()
    quit();
