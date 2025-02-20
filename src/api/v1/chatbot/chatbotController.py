from flask import Blueprint, jsonify, request
from .chatbotService import ChatbotService

chatbotRoutes = Blueprint('chatbotRoutes', __name__, url_prefix='/v1/chatbot')

@chatbotRoutes.route('/chat', methods=['POST'])
def chat():
    data, status = ChatbotService().chat(request.json['message'])
    return jsonify(data), status