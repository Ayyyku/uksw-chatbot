from flask import Flask, render_template
from api.v1.chatbot.chatbotController import chatbotRoutes
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.register_blueprint(chatbotRoutes)

if __name__ == '__main__':
    app.run(debug=True)
