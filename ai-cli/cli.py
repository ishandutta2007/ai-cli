import click
from rich.console import Console
from .models import get_model, registered_models
from .keys import set_key, get_key
from .plugins import load_plugins

console = Console()

@click.group()
@click.version_option()
def cli():
    """ai-cli — Unified CLI for ALL AI models (LLM, image/video/audio/gen...)"""
    load_plugins()

@cli.command()
def models():
    """List all available models from installed plugins"""
    if not registered_models:
        console.print("[yellow]No models registered. Install some plugins![/]")
        return
    for name in sorted(registered_models):
        console.print(f"• {name}")

@cli.command()
@click.argument("prompt", required=False, nargs=-1)
@click.option("-m", "--model", default=None, help="Model to use")
@click.option("-a", "--attachment", multiple=True, help="Path/URL to image/audio/video")
@click.option("--json", is_flag=True, help="Output JSON")
def run(prompt, model, attachment, json):
    """Run a prompt / generation (text, image, etc)"""
    prompt = " ".join(prompt) if prompt else None
    if not prompt and not attachment:
        raise click.UsageError("Provide prompt or attachments")

    if not model:
        raise click.UsageError("Use --model <model-name> (run 'ai-cli models' to list)")

    instance = get_model(model)
    result = instance.run(prompt or "", attachments=attachment)

    if json:
        import json as j
        console.print_json(data=result)
    else:
        if "text" in result:
            console.print(result["text"])
        if "image_url" in result:
            console.print(f"[green]Image:[/] {result['image_url']}")
        # etc.

@cli.group()
def keys():
    """Manage API keys for providers"""

@keys.command(name="set")
@click.argument("provider")
@click.argument("key", required=False)
def keys_set(provider, key):
    set_key(provider, key)
    console.print(f"Key for [bold]{provider}[/] set.")

# Add more groups: chat, generate (subcommands: image, video, speech, music), embed, etc.

@cli.group(name="generate")
def generate():
    """Generate media (image/video/audio/music) — plugin dependent"""
    pass

@generate.command(name="image")
@click.argument("prompt", nargs=-1)
@click.option("-m", "--model", required=True)
def gen_image(prompt, model):
    """Generate image from text prompt"""
    run.callback(" ".join(prompt), model=model, attachment=(), json=False)
    # In real plugins -> route to image gen path