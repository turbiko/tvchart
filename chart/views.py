from datetime import datetime
import datetime as dt
import pandas as pd
import re

from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import TVChartUploadForm

from .models import chart_context, ChartLine


def chart_page(request):
    print(f"chart_page started")

    return render(request, 'chart/week_chart.html', chart_context(request))


def upload_chart(request):
    print(f"upload_chart")
    previous_date = None
    if request.method == 'POST':
        form = TVChartUploadForm(request.POST, request.FILES)
        if form.is_valid():
            tv_chart_file = form.cleaned_data['tv_chart_file']

            _match = re.match(
                r'.*?(\d+)[ _]неделя[ _]\((\d{2}\.\d{2}\.\d{4})[ _]-[ _](\d{2}\.\d{2}\.\d{4})\)\.xlsx',
                tv_chart_file.name
            )

            print(f"Uploading {tv_chart_file.name=}")
            if _match:
                chart_week, chart_start_date, chart_end_date = _match.groups()
            try:
                df = pd.read_excel(tv_chart_file, header=0, sheet_name='Рус')

                with transaction.atomic():
                    for _, row in df.iterrows():
                        cell_datetime_match = re.match(r"([А-Яа-я]+),\s*(\d{2}\.\d{2}\.\d{4})", str(row['Время и дата']))

                        if cell_datetime_match:
                            current_weekday, current_date_str = cell_datetime_match.groups()
                            current_date = datetime.strptime(current_date_str, '%d.%m.%Y')
                        else:
                            chart_line_date = datetime.combine(current_date, df.iloc[_, 0])
                            program_title = df.iloc[_, 1]
                            program_genre = df.iloc[_, 2]
                            if previous_date is None:
                                previous_date = chart_line_date
                            else:
                                if previous_date.time() >= chart_line_date.time():
                                    chart_line_date += dt.timedelta(days=1)
                                    previous_date = chart_line_date  # change only when next day arrives
                                    current_date = chart_line_date.date()  # after 24-00 current date changed

                            chart_line, created = ChartLine.objects.get_or_create(
                                start_time=chart_line_date,
                                defaults={'program_title': program_title, 'program_genre': program_genre}
                            )

# final result reading
                messages.success(request, 'TV Chart data uploaded successfully.')
                return redirect('upload_chart')
            except Exception as e:
                messages.error(request, f'Error processing the file: {e}')
    # enf POST
    else:
        form = TVChartUploadForm()

    return render(request, 'chart/upload_chart.html', {'form': form})
