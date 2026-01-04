# My Package

A brief description of what your CLI does.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package manager

## Installation

Install this CLI tool globally:

```bash
make install
```

Expected output:
```
my-cli installed successfully
```

The CLI will be installed to `~/.local/bin`. Make sure this directory is in your `$PATH`:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export PATH="$HOME/.local/bin:$PATH"
```

## Usage

See the [usage documentation](./USAGE.md) for all available commands and options.

### Quick Start

```bash
# Example command
my-cli greet --names Alice,Bob

# Get help
my-cli --help
```

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.