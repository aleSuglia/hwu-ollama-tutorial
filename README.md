# Ollama Tutorial

This repository is designed to teach students how to use [Ollama](https://ollama.com/) via the
official [Python API](https://github.com/ollama/ollama-python).

## Installation

To get started, you need to install the required dependencies for your Python environment. 
Activate one using your favourite Python environment manager (e.g., [Anaconda](https://www.anaconda.com/)). 

Then, you can install all the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Running the Scripts

### Interacting with an LLM: `llm_client.py`

To run the script, use the following command:

```bash
python llm_client.py
```

This script demonstrates the basic usage of the Ollama API for text-only LLMs.

### Interacting with a VLM: `vlm_client.py`

To run the second script, use the following command:

```bash
python vlm_client.py
```

This script provides an example of how to run vision+language models that are available in Ollama.