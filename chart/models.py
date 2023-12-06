import os
import logging
from datetime import datetime
import datetime as dt
import pandas as pd
import re

from django.utils import timezone
from django.db.models import F
from django.db.models.functions import ExtractWeek, ExtractYear
from django.utils.translation import gettext_lazy as _
from django.db import models
from wagtail.models import Page




class ChartLine(models.Model):
    start_time = models.DateTimeField()
    program_title = models.CharField(_("Название программы"), max_length=200)
    program_genre = models.CharField(_("Жанр программы"), max_length=100, blank=True, null=True)


def chart_context(request):
    context = {}
    now = timezone.now()
    start_of_week = now - dt.timedelta(days=now.weekday())
    end_of_week = start_of_week + dt.timedelta(days=6)
    # Extract the week number and year from the current date
    current_week_number = ExtractWeek(F('start_time'))
    current_year = ExtractYear(F('start_time'))
    # Filter ChartLines for the current week
    lines_in_current_week = ChartLine.objects.annotate(
        week_number=current_week_number,
        year=current_year
    ).filter(week_number=now.isocalendar()[1], year=now.year).order_by('start_time')# Organize ChartLines by date
    chart_lines_by_date = {}
    for line in lines_in_current_week:
        date_key = line.start_time.date()
        if date_key not in chart_lines_by_date:
            chart_lines_by_date[date_key] = []
        chart_lines_by_date[date_key].append(line)
    context['chart_lines_by_date'] = chart_lines_by_date
    context['start_of_week'] = start_of_week

    return context


class TVChart(models.Model):
    tv_chart_file = models.FileField(max_length=255)

    def get_today_week():
        return datetime.date(2010, 6, 16).isocalendar()[1]


class WeekChart(Page):
    template = 'chart' + os.sep + 'week_chart.html'
    parent_page_types = ['programs.ProgramsIndexPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context.update(chart_context(request))
        return context
