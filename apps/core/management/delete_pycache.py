from django.conf import settings
from django.core.management.base import BaseCommand
import shutil
import os

class Command(BaseCommand):
    help = 'Deletes all __pycache__ directories within the project.'

    def handle(self, *args, **kwargs):
        for root, dirs, files in os.walk(settings.BASE_DIR):
            if '__pycache__' in dirs:
                pycache_dir = os.path.join(root, '__pycache__')
                shutil.rmtree(pycache_dir)
                self.stdout.write(self.style.SUCCESS(f'Deleted {pycache_dir}'))
        print("Removed all pycache (.pyc) files.")
