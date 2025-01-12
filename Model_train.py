import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments
)
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
from trl import SFTTrainer

def prepare_dataset():
    dataset = load_dataset("code_search_net", "python")
    
    def format_example(example):
        return {
            "text": f"Documentation: {example['func_documentation_string']}\nCode:\n{example['func_code_string']}"
        }
    
    formatted_dataset = dataset["train"].map(format_example)
    
    formatted_dataset = formatted_dataset.select(range(10000))
    
    return formatted_dataset

def get_model_config():
    return BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

def get_lora_config():
    return LoraConfig(
        r=8,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )

def get_training_args():
    return TrainingArguments(
        output_dir="./finetuned-codellama",
        num_train_epochs=3,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=10,
        save_strategy="epoch",
        fp16=True
    )

def main():
    if torch.cuda.is_available():
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
        print(f"Available GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    else:
        print("No GPU available. Please enable GPU runtime in Colab.")
        return
    
    print("Loading dataset...")
    train_dataset = prepare_dataset()
    print(f"Dataset size: {len(train_dataset)} examples")
    
    print("Loading model and tokenizer...")
    model_name = "codellama/CodeLlama-7b-hf"
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=get_model_config(),
        device_map="auto"
    )
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    print("Preparing model for training...")
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, get_lora_config())
    
    print("Trainable parameters:")
    model.print_trainable_parameters()
    
    print("Initializing trainer...")
    trainer = SFTTrainer(
        model=model,
        train_dataset=train_dataset,
        args=get_training_args(),
        tokenizer=tokenizer
    )
    
    print("Starting training...")
    trainer.train()
    
    print("Saving model...")
    trainer.save_model("./finetuned-codellama")
    
    print("Training complete!")

if __name__ == "__main__":
    main()