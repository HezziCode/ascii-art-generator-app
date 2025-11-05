🚀 Python Project Management Guide

In our project, we use uv instead of pip for all Python-related work and project management.

🧩 Why uv?

⚡ Faster than pip and poetry

🧠 Handles virtual environments automatically

🪶 Lightweight and modern

🔒 Deterministic and reproducible builds


💻 Usage Rules

❌ Do not use: pip install <package>

✅ Always use: uv add <package>

Example:

```
uv add fastapi
```

To run your Python app:

```
uv run python app.py
```