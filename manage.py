import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Hardcode the port number (e.g., 8001)
    if len(sys.argv) == 1 or sys.argv[1] == "runserver":
        sys.argv = [sys.argv[0], "runserver", "127.0.0.1:8002"]

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
