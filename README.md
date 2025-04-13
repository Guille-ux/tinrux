# Tinrux Database

[![PyPI - Version](https://img.shields.io/pypi/v/tinrux.svg)](https://pypi.org/project/tinrux)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinrux.svg)](https://pypi.org/project/tinrux)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

-----------------

A lightweight Redis-inspired database written in pure Python, designed for small-scale applications needing simple persistence.

## ✨ Features

- **Redis-like commands**: `SET`, `GET`, `DEL`, `EXPIRE`, etc.
- **Auto-persistence**: Saves data to JSON for more read (`tdb.json`).
- **Server/Client mode**: Runs as a standalone service.
- **Zero dependencies**: Pure Python (≥ 3.6).
- **Autosaving system**: Saves automatically the database (by default every 15 minutes).
- **Cookie's management system**: Has a cookie's management system for logins and more!

## 🚀 Installation

```bash
pip install tinrux
```

## 🛠️ Basic Usage

Make a new db:

```bash
tinrux server localhost 5000 new
```

Start a saved server:

```bash
tinrux server localhost 5000
```

Interactive client:

```bash
tinrux client localhost 5000
```

Python example:

```python
(localhost:5000)>>> SET greeting "Hello Tinrux"
OK
(localhost:5000)>>> GET greeting
Hello Tinrux
```

## 📝 Why JSON?

Tinrux uses JSON for persistance due to several key advantages:
- **Human-readable format**: JSON files are easy to inspect and modify manually, making debugging and testing more straightforward.
- **Language interoperability**: JSON is widely supported across programming languages, allowing easy data export or import into other systems.
- **Lightweight and structured**: Perfect for small-scale applications where full databse engines are overkill, but a clear and structured format is still needed.
- **Built-in support in Python**: Using Python's standard `json` module eliminates the need for external dependencies and ensures compatibility.

This choice aligns with Tinrux's philosophy of simplicity, transparency and minimalism.

## 📚 Available Commands

| Command | Description              | Example       |
| ------- | ------------------------ | ------------- |
| SET     | Store a value            | SET key value |
| GET     | Retrieve a value         | GET key       |
| DEL     | Delete a key             | DEL key       |
| EXPIRE  | Set key expiration (sec) | EXPIRE key 10 |
| SAVE    | Manual data persistence  | SAVE          |
| HELP    | Help command             | HELP          |

## 📦 Project Structure

```
tinrux/
├── src/
│    └── tinrux/
│         ├── tinruxClient.py  # Connection handler
│         ├── tinruxServer.py  # Core database engine
│         ├── __about__.py # version
│         ├── __init__.py # packet
│         └── cli.py           # Command-line interface
```

## 📄 License

`tinrux` is distributed under the terms of the [GPLv3](https://spdx.org/licenses/GPL-3.0-or-later.html) license.

GNU General Public License v3.0 - See LICENSE.txt.

## Contributors
Make pull request to be here!


## Contributing

[Contributing](CONTRIBUTING.md)
