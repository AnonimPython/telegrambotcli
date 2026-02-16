# --- Base Bot Template ---
START_PY_CONTENT = """import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers.main import router

# Load environment variables from .env file
load_dotenv()

async def main():
    # Logging setup
    logging.basicConfig(level=logging.INFO)
    
    # Get token from .env
    token = os.getenv("BOT_TOKEN")
    if not token:
        exit("Error: BOT_TOKEN not found in .env file")

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    
    print("🚀 System Online: Telegram Bot is now polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 System Offline")
"""

# --- Handlers Template ---
HANDLERS_MAIN_CONTENT = """from aiogram import Router, types
from aiogram.filters import Command
from app.handlers.keyboards.builders import get_main_kb, get_inline_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! I am your AI-powered bot. Use /keyboard or /inlinekeyboard to see what I can do.")

@router.message(Command("keyboard"))
async def cmd_keyboard(message: types.Message):
    await message.answer("This is a standard reply keyboard:", reply_markup=get_main_kb())

@router.message(Command("inlinekeyboard"))
async def cmd_inline(message: types.Message):
    await message.answer("This is an inline keyboard (under the text):", reply_markup=get_inline_kb())
"""

# --- Keyboards Template ---
KEYBOARDS_CONTENT = """from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

def get_main_kb():
    \"\"\"Standard Reply Keyboard (buttons at the bottom)\"\"\"
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="Support 🆘"), KeyboardButton(text="Settings ⚙️"))
    return builder.as_markup(resize_keyboard=True)

def get_inline_kb():
    \"\"\"Inline Keyboard (buttons under the message)\"\"\"
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Our GitHub", url="https://github.com"))
    builder.add(InlineKeyboardButton(text="Join Channel", url="https://t.me"))
    return builder.as_markup()
"""

# --- Handlers Template ---
HANDLERS_MAIN_CONTENT = """from aiogram import Router, types
from aiogram.filters import Command
from app.handlers.keyboards.builders import get_main_kb, get_inline_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! I am your AI-powered bot. Use /keyboard or /inlinekeyboard to see what I can do.")

@router.message(Command("keyboard"))
async def cmd_keyboard(message: types.Message):
    await message.answer("This is a standard reply keyboard:", reply_markup=get_main_kb())

@router.message(Command("inlinekeyboard"))
async def cmd_inline(message: types.Message):
    await message.answer("This is an inline keyboard (under the text):", reply_markup=get_inline_kb())
"""



# --- Database Template (SQLModel) ---
DATABASE_CONTENT = """from sqlmodel import Field, SQLModel, create_engine, Session

# Example Model
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int = Field(index=True, unique=True)
    username: str | None = None

# --- DATABASE CONNECTION ---
# SQLite (Local Development)
sqlite_url = "sqlite:///./database.db"

# PostgreSQL (Production Example)
# To use Postgres, install 'psycopg2' and change URL:
# postgres_url = "postgresql://user:password@localhost:5432/dbname"

engine = create_engine(sqlite_url, echo=False)

def init_db():
    \"\"\"Creates all tables defined in models\"\"\"
    SQLModel.metadata.create_all(engine)

def get_session():
    \"\"\"Dependency for getting DB sessions\"\"\"
    with Session(engine) as session:
        yield session
"""

# --- GITIGNORE Template ---
GITIGNORE_CONTENT = """# Python
__pycache__/
*.py[cod]

# VSCode Settings
.vscode
logs/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

__pypackages__/
# PyBuilder
.pybuilder/
target/
*.pot

# Database
*.db
"""

# --- .env Template  ---
ENV_CONTENT = """TELEGRAM_TOKEN="YOUR_BOT_TOKEN_HERE"
# DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
#ADMIN_ID="YOUR_TELEGRAM_ID"
"""
