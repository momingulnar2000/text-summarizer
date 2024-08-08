import click
import ollama

def summarize_text(text):
    prompt = f"Please provide a brief and concise summary of the following text: {text}"
    response = ollama.chat(model='qwen2:0.5b', messages=[
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

@click.command()
@click.argument('text', type=str, required=False)
@click.option('--file', '-f', type=click.Path(exists=True), help='Path to the text file to summarize.')
def summarize(text, file):
    if file:
        with open(file, 'r') as f:
            text = f.read()
    
    if not text:
        click.echo('Error: No text provided or file is empty.')
        return

    summary = summarize_text(text)
    click.echo(f"Summary: {summary}")

if __name__ == "__main__":
    summarize()
