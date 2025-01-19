# Ollama Tutorial

This repository is designed to teach students how to use [Ollama](https://ollama.com/) via the
official [Python API](https://github.com/ollama/ollama-python).

## Installation

To get started, first make sure you have Ollama installed from [their website](https://ollama.com/).

Then, you need to install the required dependencies for your Python environment. 
Activate one using your favourite Python environment manager (e.g., [Anaconda](https://www.anaconda.com/)). 

Then, you can install all the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Running the Scripts

### Interacting with an LLM: `llm_client.py`

To run the script, first make sure you have the Ollama server running (by opening the Ollama app on your computer).

Then, you need to pull the model you want to use. For this tutorial, we will use the `llama3.2` model, therefore you need to run the following command:

```bash
ollama pull llama3.2
```

> 💡 **Note:** you can check out other available models on [Ollama model library](https://ollama.com/library).


Finally, use the following command to run the script:

```bash
python llm_client.py
```

or just run it in favourite Python IDE.

> ⚠️ **Warning:** if you got an error (`command not found` or something similar), you need to close and reopen your IDE. 

This script demonstrates the basic usage of the Ollama API for text-only LLMs.

### Interacting with a VLM: `vlm_client.py`

To run the second script, use the following command:

```bash
python vlm_client.py
```

This script provides an example of how to run vision+language models that are available in Ollama.

To save space on your local machine, you can delete the model you pulled earlier by running:

```bash
ollama rm MODEL_NAME
```