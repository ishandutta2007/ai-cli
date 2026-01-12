# ai-cli — Access **every** AI model from your terminal

![Project Status](https://img.shields.io/badge/status-active-success) <!-- Placeholder for a badge -->
![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue) <!-- Placeholder for a badge -->

Unified CLI for LLMs, image gen (DALL·E, Flux, SD3, ...), video (Runway, Luma, Kling, ...), TTS/STT, music (Udio/Suno), etc.

This powerful command-line interface (CLI) provides a seamless way to interact with a vast array of Artificial Intelligence models, ranging from large language models (LLMs) to cutting-edge image, video, audio generation, and speech-to-text/text-to-speech services. Designed for developers, researchers, and AI enthusiasts, `ai-cli` simplifies the process of integrating and experimenting with the latest AI technologies directly from your terminal.

## ✨ Features

*   **Universal Access**: Connect to diverse AI models including LLMs, image generation (e.g., DALL·E, Stable Diffusion, Flux), video synthesis (e.g., Runway, Luma, Kling), audio production (e.g., Udio, Suno), and speech processing (TTS/STT).
*   **Unified Interface**: A consistent and intuitive command-line interface streamlines interaction across different AI providers and model types.
*   **API Key Management**: Securely manage your API keys for various services, ensuring easy access without compromising security.
*   **Extensible Plugin System**: Easily extend `ai-cli`'s functionality by developing and integrating custom plugins for new models or providers.
*   **Local & Cloud Integration**: Support for both cloud-based AI APIs and potentially local models (if applicable, needs clarification from user).
*   **Developer-Friendly**: Built with a clean architecture, making it easy to contribute, understand, and adapt.

## 🚀 Installation

`ai-cli` is designed for easy installation via pip.

### Prerequisites

*   Python 3.8+
*   `git` (for cloning the repository directly)

### From PyPI

The easiest way to install `ai-cli` is using `pip`:

```bash
pip install ai-cli
```

### From Source

If you prefer to install the latest development version or contribute to the project, you can install it from source:

```bash
git clone https://github.com/your-org/ai-cli.git # Replace with your actual repository URL
cd ai-cli
pip install -e .
```

## 📚 Usage

`ai-cli` uses a modular command structure, allowing you to interact with different AI domains and models.

### General Command Structure

```bash
ai <domain> <command> [options]
```

*   `<domain>`: Refers to the type of AI task (e.g., `llm`, `image`, `video`, `audio`).
*   `<command>`: The specific action within that domain (e.g., `chat`, `generate`, `transcribe`).
*   `[options]`: Parameters specific to the command and model.

### 🔑 API Key Configuration

Before using most AI models, you'll need to configure your API keys. `ai-cli` provides a secure way to manage these.

```bash
ai keys set <provider> <key_value>
ai keys list
# Example:
# ai keys set openai sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
*Note: Replace `<provider>` with the service name (e.g., `openai`, `gemini`, `stability`) and `<key_value>` with your actual API key.*

### 💬 LLM Interaction (Example)

Engage with large language models for chat, code generation, summarization, and more.

```bash
# Chat with a default LLM
ai llm chat "What is the capital of France?"

# Specify a different model (if configured)
ai llm chat -m gemini-pro "Explain quantum entanglement in simple terms."

# Generate code
ai llm generate-code -p "Python function to reverse a string"
```

### 🖼️ Image Generation (Example)

Generate images from text prompts using various models.

```bash
# Generate an image using a default image model
ai image generate "A futuristic city at sunset, cyberpunk style"

# Specify resolution and model
ai image generate -m dall-e-3 --size 1024x1024 "A serene landscape with cherry blossoms and a flowing river"
```

### 🎬 Video Generation (Example)

Create short videos from text or image prompts.

```bash
# Generate a short video clip
ai video generate "A cat playing piano in a dimly lit jazz club, 8k"
```

### 🎧 Audio Processing (Example)

Perform speech-to-text, text-to-speech, or music generation.

```bash
# Transcribe an audio file
ai audio transcribe --file "path/to/my_audio.mp3"

# Generate speech from text
ai audio tts "Hello, this is ai-cli speaking." --voice "nova" --output "hello.mp3"
```

*Note: The exact commands and available options may vary based on configured plugins and providers. Use `ai <domain> --help` and `ai <domain> <command> --help` for detailed information.*

## ⚙️ Configuration

`ai-cli` stores its configuration (including API keys) in a secure location. You can usually find configuration details in `~/.config/ai-cli/config.yaml` (Linux/macOS) or `C:\Users\<YourUser>\AppData\Roaming\ai-cli\config.yaml` (Windows).

## 🤝 Contributing

We welcome contributions! If you're interested in improving `ai-cli`, whether by adding new features, fixing bugs, or extending support for more AI models, please see our [Contribution Guidelines](CONTRIBUTING.md) (placeholder - will need to be created if not present).

### Development Setup

1.  Fork the repository.
2.  Clone your forked repository: `git clone https://github.com/your-username/ai-cli.git`
3.  Navigate to the project directory: `cd ai-cli`
4.  Install in editable mode: `pip install -e .`
5.  Install development dependencies: `pip install -r requirements-dev.txt` (placeholder - need to confirm if this file exists)

## 📄 License

This project is licensed under the MIT OR Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions, issues, or suggestions, please open an issue on our [GitHub repository](https://github.com/your-org/ai-cli).

---

**`ai-cli` is an open-source project designed to make AI accessible to everyone. Your contributions and feedback are highly appreciated!**

