import torch
import torch.nn as nn
import torch.optim as optim

# 1. Prepare Training Data
# Vocabulary map (assigning a number to each unique word)
vocab = {
    "i": 0, "love": 1, "coding": 2, "this": 3, "is": 4, "amazing": 5, "great": 6, "work": 7,
    "hate": 8, "bugs": 9, "terrible": 10, "broken": 11, "code": 12, "slow": 13, "bad": 14
}
vocab_size = len(vocab)

# Helper function to convert a sentence into a Bag-of-Words vector
def sentence_to_vector(sentence, vocab_dict):
    vector = torch.zeros(len(vocab_dict))
    words = sentence.lower().replace(".", "").split()
    for word in words:
        if word in vocab_dict:
            vector[vocab_dict[word]] += 1.0
    return vector

# Sentences and their true labels (1 = Positive, 0 = Negative)
raw_sentences = [
    "i love coding", "this is amazing", "great work",
    "i hate bugs", "this is terrible", "broken code"
]
labels = torch.tensor([1.0, 1.0, 1.0, 0.0, 0.0, 0.0]).unsqueeze(1)

# Convert all text into numerical vectors
inputs = torch.stack([sentence_to_vector(s, vocab) for s in raw_sentences])

# 2. Define the Neural Network Architecture
class TinySentimentModel(nn.Module):
    def __init__(self, input_size):
        super(TinySentimentModel, self).__init__()
        # A single layer mapping inputs directly to a single output score
        self.layer = nn.Linear(input_size, 1)
        # Squeezes the output score into a probability between 0 and 1
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        return self.sigmoid(self.layer(x))

# Create an instance of our model
model = TinySentimentModel(vocab_size)

# 3. Setup the Training Configurations
criterion = nn.BCELoss() # Binary Cross Entropy Loss (standard for 0 vs 1 problems)
optimizer = optim.SGD(model.parameters(), lr=0.1) # Stochastic Gradient Descent optimizer

# 4. The Training Loop (Optimization over 500 rounds)
print("Training the neural network...")
for epoch in range(500):
    # Forward Pass: Predict outputs based on current weights
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    
    # Backward Pass: Calculate errors and tweak the weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print(f"  Epoch [{epoch+1}/500], Loss: {loss.item():.4f}")

print("\nModel training complete!\n")

# 5. Test the AI on a brand new sentence it has never seen
test_sentence = "i love code"
test_vector = sentence_to_vector(test_sentence, vocab)

# Tell PyTorch we are just testing, not training anymore
with torch.no_grad():
    prediction = model(test_vector)
    probability = prediction.item()

print(f"Testing new text: '{test_sentence}'")
print(f"AI Positive Probability: {probability:.4f}")
if probability > 0.5:
    print("Prediction: Positive Sentiment")
else:
    print("Prediction: Negative Sentiment")