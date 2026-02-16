import typer
import os
import platform
from . import templates

app = typer.Typer()

@app.callback(invoke_without_command=True)
def main():
    """Generates a professional Aiogram 3 project structure"""
    
    
    current_os = platform.system()
    python_cmd = "python" if current_os == "Windows" else "python3"
    
    folders = [
        "app",
        "app/handlers",
        "app/handlers/database",
        "app/handlers/keyboards"
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "__init__.py"), "a"): pass

    files_map = {
        "bot.py": templates.START_PY_CONTENT,
        ".gitignore": templates.GITIGNORE_CONTENT,
        ".env": templates.ENV_CONTENT,
        "app/handlers/main.py": templates.HANDLERS_MAIN_CONTENT,
        "app/handlers/database/database.py": templates.DATABASE_CONTENT,
        "app/handlers/keyboards/builders.py": templates.KEYBOARDS_CONTENT
    }

    for path, content in files_map.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
    typer.secho("🚀 Project structure created successfully!", fg=typer.colors.CYAN, bold=True)
    typer.secho("👉 Next steps:", fg=typer.colors.YELLOW)
    typer.echo("1. Fill your BOT_TOKEN in .env")
    
    typer.secho(f"2. Run '{python_cmd} bot.py'", fg=typer.colors.GREEN, bold=True)

if __name__ == "__main__":
    app()
