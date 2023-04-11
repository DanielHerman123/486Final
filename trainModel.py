from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import os




# Load the CSV file into a pandas DataFrame
df = pd.read_csv('trainingData/training_data.csv')

# Extract the text data and labels from the DataFrame
texts = df['text'].tolist()
labels = df['label'].tolist()

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased", max_length=512)

# Tokenize the original data
tokenized_data = tokenizer(texts, truncation=True, max_length=512, return_tensors="pt", padding=True)

# Tokenize the new data
encodings = tokenizer(texts, truncation=True, padding=True, return_tensors='pt')

# Create a PyTorch Dataset from the encodings and labels
class MyDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(int(self.labels[idx]))
        return item

    def __len__(self):
        return len(self.labels)

# Combine the original and new datasets
combined_dataset = torch.utils.data.ConcatDataset([MyDataset(tokenized_data, labels), MyDataset(encodings, labels)])

# Create a DataLoader to load the combined data in batches
batch_size = 4
dataloader = DataLoader(combined_dataset, batch_size=batch_size, shuffle=True)

# Load the pre-trained model
model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

# Set the model to training mode
model.train()

# Set up the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    max_grad_norm=1.0, # set max_grad_norm to a smaller value
    gradient_accumulation_steps=4, # accumulate gradients over 4 batches
)

# Set up the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=combined_dataset,
)

# Train the model on the combined data
trainer.train()

# Set the model to evaluation mode
model.eval()


while True:
    user_input = input("Enter a Sentence to classify: ")
    # do something with user_input

    # Test the model on a sample input
    inputs = tokenizer(user_input, return_tensors="pt", padding=True)
    inputs = {k: v.to('cuda:0') for k, v in inputs.items()} # Move inputs to the same device as model
    outputs = model(**inputs)
    logits = outputs.logits

    # [0] -> left 
    # [1] -> center
    # [2] -> right
    count_left = 0
    count_center = 0
    count_right = 0

    prediction = logits.argmax().item()
    if prediction == 0:
        print("Liberal.")
        count_left += 1
    elif prediction == 1:
        print("Centrist.")
        count_center += 1
    else:
        print("Conservative.")
        count_right += 1

# TODO create an accuracy checker for the code

# https://huggingface.co/bucketresearch/politicalBiasBERT
# https://huggingface.co/docs/transformers/training
