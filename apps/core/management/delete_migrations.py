from django.conf import settings
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Deletes all migration files within all apps\' migrations directories.'

    def handle(self, *args, **kwargs):
        app_root = os.path.join(settings.BASE_DIR, 'apps')  # Adjust if your structure is different
        for root, dirs, files in os.walk(app_root):
            if 'migrations' in dirs:
                migrations_dir = os.path.join(root, 'migrations')
                for filename in os.listdir(migrations_dir):
                    if filename != '__init__.py':
                        file_path = os.path.join(migrations_dir, filename)
                        os.remove(file_path)
                        self.stdout.write(self.style.SUCCESS(f'Deleted {file_path}'))
        print("Deleted all migrations.")
