
START_PY_CONTENT = """import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.main import router

load_dotenv()

async def main():
    logging.basicConfig(level=logging.INFO)
    
    token = os.getenv("BOT_TOKEN")
    if not token:
        exit("Error: BOT_TOKEN not found in .env")

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    

    print("🚀 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Stopped")
"""
HANDLERS_LITE_CONTENT = """from aiogram import Router, types, F
from aiogram.filters import Command
from app.keyboards.builders import get_main_kb, get_inline_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! I am your bot. Use /keyboard or /inline to see buttons.")

@router.message(Command("keyboard"))
async def cmd_keyboard(message: types.Message):
    await message.answer("This is a standard keyboard:", reply_markup=get_main_kb())

@router.message(Command("inline"))
async def cmd_inline(message: types.Message):
    await message.answer("This is an inline keyboard:", reply_markup=get_inline_kb())
    
@router.message(F.text == "Help 🆘")
async def help_handler(message: types.Message):
    await message.answer("You use Help button")

@router.message(F.text == "Settings ⚙️")
async def settings_handler(message: types.Message):
    await message.answer("You use Settings button")    

"""
# --- Handlers (Advanced version with Admin check) ---
HANDLERS_ADVANCED_CONTENT = """from aiogram import Router, types, F
from aiogram.filters import Command
from app.keyboards.builders import get_main_kb, get_inline_kb
from app.filters.admin import AdminFilter

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! Advanced bot is ready. Commands: /keyboard, /inline, /admin")

@router.message(Command("keyboard"))
async def cmd_keyboard(message: types.Message):
    await message.answer("Standard keyboard:", reply_markup=get_main_kb())

@router.message(Command("inline"))
async def cmd_inline(message: types.Message):
    await message.answer("Inline keyboard:", reply_markup=get_inline_kb())
    
@router.message(F.text == "Help 🆘")
async def help_handler(message: types.Message):
    await message.answer("You use Help button")

@router.message(F.text == "Settings ⚙️")
async def settings_handler(message: types.Message):
    await message.answer("You use Settings button")

@router.message(Command("admin"), AdminFilter())
async def cmd_admin_success(message: types.Message):
    await message.answer(f"👑 Access granted, Admin {message.from_user.id}!")

@router.message(Command("admin"))
async def cmd_admin_fail(message: types.Message):
    await message.answer("🚫 Access denied: You are not an admin.")
"""


# --- Keyboards ---
KEYBOARDS_CONTENT = """from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

def get_main_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="Help 🆘"), KeyboardButton(text="Settings ⚙️"))
    return builder.as_markup(resize_keyboard=True)

def get_inline_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="GitHub", url="https://github.com/AnonimPython/"))
    builder.add(InlineKeyboardButton(text="PyPl",url="https://pypi.org/project/telegrambotcli/", callback_data="support"))
    return builder.as_markup()
"""

# --- Database ---
DATABASE_CONTENT = """from sqlmodel import Field, SQLModel, create_engine, Session
import os

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int = Field(index=True, unique=True)

# --- DB CONNECTION CONFIG ---
# Local SQLite
db_url = "sqlite:///./database.db"

# PostgreSQL Example
# To use: uncomment the line in .env and add your PostgreSQL credentials
# db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

def init_db():
    SQLModel.metadata.create_all(engine)
"""
# --- Advanced Components ---
ADMIN_FILTER_CONTENT = """from aiogram.filters import Filter
from aiogram.types import Message
import os

class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        admin_id = os.getenv("ADMIN_ID")
        return str(message.from_user.id) == str(admin_id)
"""

ANTIFLOOD_MW_CONTENT = """import asyncio
from aiogram import BaseMiddleware

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 2):
        self.limit = {}
        self.limit_time = limit
        super().__init__()

    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        if user_id in self.limit:
            return
        self.limit[user_id] = True
        await asyncio.sleep(self.limit_time)
        del self.limit[user_id]
        return await handler(event, data)
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
ENV_CONTENT = """BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
ADMIN_ID="123456789"

# DB_URL="postgresql://USER:PASSOWRD@localhost:5432/DATABASE_NAME"
"""
