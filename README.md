# RE-Aided-VA
Enhancing Reverse Engineering: Automated Vulnerability Detection via Code Embeddings and LLMs

**Overview**

The main goal is to establish a reproducible baseline for vulnerability detection and explore prompt engineering and few-shot learning for improved performance.

**Dataset**

Source: Juliet Test Suite v1.3

Languages: C

**Target Vulnerabilities (CWEs):**

CWE-121: Buffer Overflow

CWE-190: Integer Overflow

CWE-416: Use-After-Free

CWE-476: Null Pointer Dereference

CWE-134: Format String

Samples Selected: 40 vulnerable + 40 safe per CWE → 400 total

Format: JSONL with fields {cwe, code, label}

**Methodology**

Data Preparation: Filtered code samples from the Juliet Test Suite based on CWE patterns. Constructed a balanced dataset for fair evaluation.

Embedding Extraction: Used CodeBERT to generate vector representations of code snippets, using mean-pooled embeddings of token outputs.

Classifier: Trained a Logistic Regression model on embeddings for binary classification (vulnerable/safe).

**Evaluation:**

Accuracy and classification report over a 70/30 train-test split.

Observed improved performance over baseline with embedding-based features.

Prompting (Optional): Explored zero-shot and few-shot LLM prompting for direct vulnerability detection (baseline ~50%, embedding-based ~82%).

**Results**
Model / Approach	Accuracy	Notes
LLM Zero-Shot Prompt	~50%	Baseline; naive yes/no prompting
Embedding + Logistic	~82%	Mean-pooled CodeBERT embeddings + classifier

**Insights:**

LLMs alone struggle with code-level vulnerability classification without task-specific training.

Embedding-based classifiers on pre-trained code models provide more stable, high-accuracy results.

Dataset balance is crucial for fair evaluation across CWEs.


**Future Work**

Implement ensemble learning for multiple models or prompts.

Compare different LLM responses with varied prompt engineering.

Explore integration with reverse engineering workflows, e.g., automated vulnerability triage for decompiled binaries.

**References**

Samuel, NIST, Juliet Test Suite v1.3: https://samate.nist.gov/SRD/testsuite.php

Feng et al., CodeBERT: A Pre-Trained Model for Programming and Natural Languages

Original Research Paper: “Enhancing Reverse Engineering: Investigating and Benchmarking Large Language Models for Vulnerability Analysis in Decompiled Binaries”
