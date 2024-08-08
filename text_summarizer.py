import click
import ollama

def summarize_text(text):
    response = ollama.chat(model='qwen2:0.5b', messages=[
        {"role": "user", "content": f"Summarize the following text:\n{text}"}
    ])
    #print("Response:", response)
    return response.get('message', {}).get('content', 'No summary found')

@click.command()
@click.option('-f', '--file', type=click.Path(exists=True), help='Path to the input file.')
@click.option('-t', '--text', type=str, help='Text to summarize directly.')
def summarize(file, text):
    if file:
        with open(file, 'r') as f:
            text = f.read()
    elif not text:
        click.echo("Error: Either a file path or text must be provided.")
        return

    summary = summarize_text(text)
    click.echo(f"Summary:\n{summary}")

if __name__ == '__main__':
    summarize()
