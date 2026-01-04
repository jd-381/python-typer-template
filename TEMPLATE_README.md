# my_package

A brief description of what my-cli does.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager

## Installation

Install my-cli:

```bash
make install
```

Expected output:

```
my-cli installed successfully
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
my-cli --help

# Example command
my-cli hello --name World
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.