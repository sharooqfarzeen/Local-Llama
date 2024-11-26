# Local LLM - Llama 3.2

This repository contains the setup and code to run a local instance of the Llama 3.2 Large Language Model (LLM) or any open source model of your choice. Follow the steps below to set up and start the application.

---

## 🚀 Quick Start

### 1. Download Ollama
To run the Llama 3.2 model locally, you need **Ollama** installed.  
Click [here to download Ollama](https://ollama.com/download).

---

### 2. Download Model Files
The model files for Llama 3.2 can be downloaded from the following link:  
[Download model files](https://github.com/ollama/ollama/blob/main/README.md)

---

### 3. Update the Model Name
Open the file `get_response.py` in your text editor, and update the `MODEL_NAME` variable to match the model you want to run. For example:
```python
MODEL_NAME = "llama3.2:1b"


### 4. Run the Application in terminal
```streamlit run app.py```