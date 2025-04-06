# Tinrux Database

[![PyPI - Version](https://img.shields.io/pypi/v/tinrux.svg)](https://pypi.org/project/tinrux)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinrux.svg)](https://pypi.org/project/tinrux)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

-----------------

A lightweight Redis-inspired database written in pure Python, designed for small-scale applications needing simple persistence.

## ✨ Features

- **Redis-like commands**: `SET`, `GET`, `DEL`, `EXPIRE`, etc.
- **Auto-persistence**: Saves data to JSON (`tdb.json`).
- **Server/Client mode**: Runs as a standalone service.
- **Zero dependencies**: Pure Python (≥ 3.6).

## 🚀 Installation

```bash
pip install tinrux
```

## 🛠️ Basic Usage

Make a new db:

```bash
tinrux server 
```

Start the server:

```bash
tinrux server localhost 6379
```

Interactive client:

```bash
tinrux client localhost 6379
```

Python example:

```python
>>> SET greeting "Hello Tinrux"
"+OK"
>>> GET greeting
"Hello Tinrux"
```

## 📚 Available Commands

| Command | Description              | Example       |
| ------- | ------------------------ | ------------- |
| SET     | Store a value            | SET key value |
| GET     | Retrieve a value         | GET key       |
| DEL     | Delete a key             | DEL key       |
| EXPIRE  | Set key expiration (sec) | EXPIRE key 10 |
| SAVE    | Manual data persistence  | SAVE          |

## 📦 Project Structure

```
tinrux/
├── src/
│   ├── tinruxClient.py  # Connection handler
│   ├── tinruxServer.py  # Core database engine
│   └── cli.py           # Command-line interface
```

## 📄 License

`tinrux` is distributed under the terms of the [GPLv3](https://spdx.org/licenses/GPL-3.0-or-later.html) license.

GNU General Public License v3.0 - See LICENSE.txt.

