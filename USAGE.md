# `my-cli`

**Usage**:

```console
$ my-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `greet`: No command example
* `mail`: Multiple command example

## `my-cli greet`

No command example

**Usage**:

```console
$ my-cli greet [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-n, --names TEXT`: Comma-separated list of names  [required]
* `-g, --greeting TEXT`: Greeting  [default: Hello]
* `--debug`: Print debug messages
* `--help`: Show this message and exit.

## `my-cli mail`

Multiple command example

**Usage**:

```console
$ my-cli mail [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `delete`: Delete mail
* `fetch`: Fetch mail
* `error`: Show example error

### `my-cli mail delete`

Delete mail

**Usage**:

```console
$ my-cli mail delete [OPTIONS]
```

**Options**:

* `-c, --count INTEGER`: Number of messages to delete  [default: 1]
* `--debug`: Print debug messages
* `--help`: Show this message and exit.

### `my-cli mail fetch`

Fetch mail

**Usage**:

```console
$ my-cli mail fetch [OPTIONS]
```

**Options**:

* `--debug`: Print debug messages
* `--help`: Show this message and exit.

### `my-cli mail error`

Show example error

**Usage**:

```console
$ my-cli mail error [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
