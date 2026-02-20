import typer
import os
import platform
from . import templates

app = typer.Typer(help="Aiogram 3 Project Generator CLI")

def create_init_files(base_path: str):
    """Рекурсивно создает __init__.py во всех подпапках проекта"""
    for root, dirs, files in os.walk(base_path):
        for directory in dirs:
            init_file = os.path.join(root, directory, "__init__.py")
            if not os.path.exists(init_file):
                with open(init_file, "a"): pass

@app.callback(invoke_without_command=True)
def main():
    """Основная точка входа для telegrambotcli"""
    typer.secho("🤖 Welcome to Telegram Bot CLI!", fg=typer.colors.MAGENTA, bold=True)
    
    typer.echo("\nSelect your project template:")
    typer.echo("1 - [Standard] Basic (app/main.py, DB, Keyboards)")
    typer.echo("2 - [Advanced] Pro (Filters, Middlewares, Admin logic)")
    
    choice = typer.prompt("\nEnter your choice (1 or 2)", default="1")

    # 1. Формируем карту файлов
    files_map = {
        "bot.py": templates.START_PY_CONTENT,
        ".gitignore": templates.GITIGNORE_CONTENT,
        ".env": templates.ENV_CONTENT,
        "app/database/database.py": templates.DATABASE_CONTENT,
        "app/keyboards/builders.py": templates.KEYBOARDS_CONTENT,
    }

    # 2. Настраиваем логику в зависимости от выбора пользователя
    if choice == "2":
        typer.secho("🚀 Deploying Advanced structure...", fg=typer.colors.CYAN)
        files_map.update({
            "app/main.py": templates.HANDLERS_ADVANCED_CONTENT,
            "app/filters/admin.py": templates.ADMIN_FILTER_CONTENT,
            "app/middlewares/antiflood.py": templates.ANTIFLOOD_MW_CONTENT,
        })
    else:
        typer.secho("🚀 Deploying Standard structure...", fg=typer.colors.BLUE)
        files_map["app/main.py"] = templates.HANDLERS_LITE_CONTENT

    # 3. Создаем папки и записываем файлы
    for path, content in files_map.items():
        # Получаем путь к директории (например, для "bot.py" это будет "")
        directory = os.path.dirname(path)
        
        # Создаем папку только если путь не пустой (фикс ошибки WinError 3)
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        # Записываем контент в файл
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # 4. Инициализируем пакеты (создаем __init__.py)
    if os.path.exists("app"):
        # Создаем __init__ в корне папки app
        with open("app/__init__.py", "a"): pass
        # Проходимся по всем вложенным папкам
        create_init_files("app")

    # 5. Финальные инструкции для пользователя
    current_os = platform.system()
    python_cmd = "python" if current_os == "Windows" else "python3"
    
    typer.secho("\n✅ Project generated successfully!", fg=typer.colors.GREEN, bold=True)
    typer.echo("👉 Next steps:")
    typer.echo("   1. Open '.env' and set your BOT_TOKEN and ADMIN_ID")
    typer.secho(f"   2. Run your bot: '{python_cmd} bot.py'", fg=typer.colors.CYAN, bold=True)

if __name__ == "__main__":
    app()
