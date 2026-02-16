# 🚀 TelegramBotCLI

A lightweight command-line utility for quickly generating professional project structures for **Aiogram 3** bots. Stop wasting time on boilerplate and start coding your logic instantly.

## ✨ Features

- **Instant Structure:** Creates folders for handlers, database (SQLModel), and keyboards in one command.
- **Smart OS Detection:** Automatically suggests the correct run command (`python` vs `python3`) based on your system.
- **Ready-to-Go Templates:** Includes pre-configured `.env`, `.gitignore`, and basic bot logic with commands.
- **Built-in Keyboards:** Comes with examples for both standard and inline keyboards.

## 📦 Installation

Install the tool directly from PyPI:

```bash
pip install telegrambotcli
```

```
## 📂 Generated Project Structure

When you run the tool, it creates a clean, modular architecture:

```text
your_project/
├── app/
│   ├── handlers/
│   │   ├── database/
│   │   │   ├── database.py   # SQLModel engine & session setup
│   │   │   └── __init__.py
│   │   ├── keyboards/
│   │   │   ├── builders.py   # Reply & Inline keyboard templates
│   │   │   └── __init__.py
│   │   ├── main.py           # Command handlers (/start, /keyboard, etc.)
│   │   └── __init__.py
│   └── __init__.py
├── bot.py                    # Main entry point (Dispatcher & Polling)
├── .env                      # Environment variables (Tokens, DB URLs)
└── .gitignore                # Pre-configured for Python & VSCode
```

## **🧑‍💻**GitHub repository

[Sourse code](https://github.com/AnonimPython/telegrambotcli)
