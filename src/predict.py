import json
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import torch

MODEL_NAME = "microsoft/codebert-base"

def load_dataset(path: str):
    samples = []
    with open(path, "r") as f:
        for line in f:
            samples.append(json.loads(line))
    return samples

def get_embedding(code: str, tokenizer, model) -> np.ndarray:
    inputs = tokenizer(
        code, return_tensors="pt",
        truncation=True, max_length=512, padding=True
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def train_and_evaluate(dataset_path: str):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, revision="main")  # nosec B615
    model = AutoModel.from_pretrained(MODEL_NAME, revision="main")  # nosec B615

    data = load_dataset(dataset_path)
    embeddings = [get_embedding(s["code"], tokenizer, model) for s in data]
    labels = [s["label"] for s in data]

    X_train, X_test, y_train, y_test = train_test_split(
        embeddings, labels, test_size=0.3, random_state=42
    )

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, preds):.4f}")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    train_and_evaluate("data/dataset.jsonl")
