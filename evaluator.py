import sys
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Add root folder to sys.path so we can import sibling modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from evaluation.metrics import (
    evaluate_sentiment,
    evaluate_summaries,
    evaluate_generation
)

# Load your ground truth dataset (only once)
dataset_path = os.path.join(os.path.dirname(__file__), '../datasets/synthetic_nlp_dataset_broad.csv')
df = pd.read_csv(dataset_path)

def get_ground_truth(input_text):
    # Normalize input text for comparison
    row = df[df['input_text'].str.lower().str.strip() == input_text.lower().strip()]
    if not row.empty:
        return {
            'sentiment_label': row.iloc[0].get('sentiment_label', None),
            'summary': row.iloc[0].get('summary', None),
            'generated_reference': row.iloc[0].get('generated_reference', None)
        }
    print(f"[DEBUG] No ground truth found for: {input_text}")
    return None

def evaluate_output(task, user_input, model_output):
    # Normalize the task string
    task = task.lower().replace(" ", "_")
    print(f"[DEBUG] Evaluating Task: {task}")

    ground_truth = get_ground_truth(user_input)
    if not ground_truth:
        return f"No ground truth found for input: {user_input}", None

    if task == "sentiment_analysis":
        return evaluate_sentiment(ground_truth['sentiment_label'], model_output), ground_truth['sentiment_label']
    elif task == "summarization":
        return evaluate_summaries(ground_truth['summary'], model_output), ground_truth['summary']
    elif task == "text_generation":
        return evaluate_generation(ground_truth['generated_reference'], model_output), ground_truth['generated_reference']
    else:
        print(f"[DEBUG] Unsupported Task Passed: {task}")
        return "Unsupported Task", None
