# template_package

A brief description of what template-cli does.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager

## Installation

Install template-cli:

```bash
make install
```

Expected output:

```
template-cli installed successfully
```

The CLI is installed to `~/.local/bin`. Make sure this directory is in your `$PATH`:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="$HOME/.local/bin:$PATH"
```

## Usage

See the [usage documentation](./USAGE.md) for all available commands and options.

### Quick Start

```bash
# See commands
template-cli --help

# Example command
template-cli hello --name World
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.