# pip install flask

from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize Flask app
app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained("fine_tuned_model")
tokenizer = GPT2Tokenizer.from_pretrained("fine_tuned_model")

@app.route('/')
def home():
    return "Generative AI Tool - Code Assistant"

@app.route('/generate', methods=['POST'])
def generate_code():
    # Get user input and configurable settings from the request
    user_input = request.json.get('query')
    tone = request.json.get('tone', 'default')
    max_length = request.json.get('max_length', 100)

    # Tokenize the input
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    
    # Generate code suggestions
    outputs = model.generate(inputs, max_length=max_length, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return the generated response
    return jsonify({'generated_code': response})

if __name__ == "__main__":
    app.run(debug=True)
