Chatbot for Business, Startups, Senior Project, and Investment Data
This is the back end part of a chatbot that answers questions related to business, startups, senior project, and investment data. The chatbot was built using the following libraries:
based on Flask Library to make a local host for the front end part

flask
numpy
json
random
nltk
pytorch
torch.nn
torch

The chatbot was trained on a dataset of business, startups, senior project, and investment data using pytorch. The training data was preprocessed and tokenized using nltk. The neural network model was built using torch.nn, and the optimization and backpropagation were handled using the pytorch framework.

Installation
To use the chatbot, you will need to have the following libraries installed:

numpy
json
random
nltk
pytorch
You can install these libraries using pip, the Python package manager. Here's an example command to install the required libraries:
pip install numpy json random nltk pytorch


Usage
To use the chatbot, you can run the chatbot.py file. The chatbot will prompt you to ask a question, and then it will provide an answer based on the training data.
$ python chatbot.py
Ask me a question: What is a startup?
A startup is a company or project in its early stages of development, typically characterized by a new and innovative product or service.

If you want to run the flask server and connect the API with front end part 
=> onn the terminal 
  python app.py 

Data
The training data used for the chatbot was sourced from business, startups, senior project, and investment data. The data was preprocessed and tokenized using nltk, and then it was used to train a neural network model using pytorch.
