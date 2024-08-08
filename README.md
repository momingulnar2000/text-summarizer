# Text Summarizer
A command-line tool written in Python for summarizing text using the Ollama API and the Qwen2 0.5B model.

## Overview
The Text Summarizer tool allows you to efficiently summarize large amounts of text. You can provide text directly via command-line arguments or read from a file. The tool utilizes the Qwen2 0.5B model provided by Ollama to generate concise summaries. The command-line interface is built using the `Click` library for ease of use.


## Features
- Summarize text provided directly via command-line arguments.
- Read text from a file and summarize it.
- Output summary directly to the command line.

## Technologies Used

- **Python**: The primary programming language used for the development of this tool.
- **Click**: A Python package used for creating beautiful command-line interfaces with as little code as necessary.
- **Ollama API**: An API that provides access to advanced language models for text summarization.

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

## Ouput Snippet

![image](https://github.com/user-attachments/assets/8c53c1bf-6afb-49c2-a466-16804882f32c)

