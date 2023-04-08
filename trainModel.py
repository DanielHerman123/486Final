from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('training_data.csv')

# Extract the text data and labels from the DataFrame
texts = df['text'].tolist()
labels = df['label'].tolist()

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

# Tokenize the original data
tokenized_data = tokenizer(dataset["sentence"], return_tensors="pt", padding=True)

# Tokenize the new data
encodings = tokenizer(texts, truncation=True, padding=True)

# Create a PyTorch Dataset from the encodings and labels
class MyDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Combine the original and new datasets
combined_dataset = torch.utils.data.ConcatDataset([dataset, MyDataset(encodings, labels)])

# Create a DataLoader to load the combined data in batches
dataloader = DataLoader(combined_dataset, batch_size=16, shuffle=True)

# Load the pre-trained model
model = AutoModelForSequenceClassification.from_pretrained("bucketresearch/politicalBiasBERT")

# Set the model to training mode
model.train()

# Set up the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

# Set up the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataloader,
)

# Train the model on the combined data
trainer.train()

# Set the model to evaluation mode
model.eval()

# Test the model on a sample input
text = "your text here"
inputs = tokenizer(text, return_tensors="pt", padding=True)
outputs = model(**inputs)
logits = outputs.logits

# [0] -> left 
# [1] -> center
# [2] -> right
print(logits)


# https://huggingface.co/bucketresearch/politicalBiasBERT
# https://huggingface.co/docs/transformers/training