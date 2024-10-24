# src/bert_finetuning.py

from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

def fine_tune_bert():
    """Fine-tune a BERT model on soft skill classification data."""
    dataset = load_dataset('csv', data_files={'train': 'data/labeled/train.csv', 'test': 'data/labeled/test.csv'})
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=5)

    def tokenize_data(examples):
        return tokenizer(examples['text'], padding='max_length', truncation=True)
    
    tokenized_data = dataset.map(tokenize_data, batched=True)
    
    training_args = TrainingArguments(output_dir='./models/bert_model', num_train_epochs=3, per_device_train_batch_size=8)
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_data['train'],
        eval_dataset=tokenized_data['test'],
    )
    
    trainer.train()
    model.save_pretrained('./models/bert_model')

if __name__ == "__main__":
    fine_tune_bert()
