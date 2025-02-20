from flask import Flask
from api.v1.chatbot.chatbotController import chatbotRoutes
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

app = Flask(__name__)

app.register_blueprint(chatbotRoutes)

if __name__ == '__main__':
    app.run(debug=True)
