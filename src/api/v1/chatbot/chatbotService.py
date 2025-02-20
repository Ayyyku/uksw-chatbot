import torch
import torch.nn as nn
import torch
import random
import json
from utils.utils import tokenize, stem, bag_of_words

FILE = 'model/trained_model_indo.pth'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

INTENTS_PATH = 'data/intents_indo.json'
with open(INTENTS_PATH, 'r') as f:
    intents = json.load(f)

PROBABILITY_THRESHOLD = 0.55

class ChatbotService:

    def __init__(self):
        data = torch.load(FILE)
        self.input_size = data['input_size']
        self.hidden_size = data['hidden_size']
        self.output_size = data['output_size']
        self.all_words = data['all_words']
        self.tags = data['tags']
        model_state = data['model_state']

        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(device)
        self.model.load_state_dict(model_state)
        self.model.eval()

    def chat(self, sentence: str) -> str:
        try:
            response = ''
            sentence = tokenize(sentence)
            X = bag_of_words(sentence, self.all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X)

            output = self.model(X)
            _, predicted = torch.max(output, dim = 1)
            tag = self.tags[predicted.item()]

            probs = torch.softmax(output, dim = 1)
            prob = probs[0][predicted.item()]
        
            if prob.item() > PROBABILITY_THRESHOLD:
                for intent in intents[ 'intents']:
                    if tag == intent['tag']:
                        response = random.choice(intent['responses'])
            else:
                response = "Maaf Saya tidak mengerti"

            return response, 200
        except Exception as e:
            return str(e), 500

class NeuralNet(nn.Module):
    '''
    Model untuk melakukan prediksi dengan menggunakan 3 layer neural network
    '''
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out