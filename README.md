# Text Summarizer
A command-line tool for summarizing text using the Ollama API and the Qwen2 0.5B model.

## Overview
The Text Summarizer application allows you to summarize large amounts of text efficiently. You can provide text directly or read from a file. The application uses the Qwen2 0.5B model provided by Ollama to generate concise summaries.

## Features
- Summarize text provided directly via command-line arguments.
- Read text from a file and summarize it.
- Output summary directly to the command line.

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
   
2. **Create a Virtual Environment**
   ```bash
   python -m venv myenv

4. **Activate the Virtual Environment**
   ```bash
   myenv\Scripts\activate

6. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
7. **Command for Ouput**
   
**Summarize Text Directly**
   ```bash
   python text_summarizer.py -t "Your text here."
```
**Summarize Text from a File**
 ```bash
  python text_summarizer.py -f input.txt
```


