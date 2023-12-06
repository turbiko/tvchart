#!/usr/bin/env python
import os
import sys
import logging

from core.settings.base import PROJECT_DIR, BASE_DIR
from core.settings.dev import DEBUG

if __name__ == "__main__":
    print(f"{PROJECT_DIR=}")
    print(f"{BASE_DIR=}")
    print(f"{DEBUG=}")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
