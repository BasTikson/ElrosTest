import io
import csv
from rest_framework import renderers
import openpyxl


class CSVStudentDataRenderer(renderers.BaseRenderer):
    media_type = "text/csv"
    format = "csv"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        csv_buffer = io.StringIO()
        headers = list(data[0].keys())
        csv_writer = csv.DictWriter(csv_buffer, fieldnames=headers, extrasaction="ignore")
        csv_writer.writeheader()

        for item in data:
            csv_writer.writerow(item)

        return csv_buffer.getvalue()


class ExcelStudentDataRenderer(renderers.BaseRenderer):

    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        headers = list(data[0].keys())
        worksheet.append(headers)
        for item in data:
            worksheet.append([str(value) for value in item.values()])
        workbook.save(buffer)

        return buffer.getvalue()


class CSVStudentDataRendererDetail(renderers.BaseRenderer):
    media_type = "text/csv"
    format = "csv"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        csv_buffer = io.StringIO()
        headers = list(data.keys())
        csv_writer = csv.DictWriter(csv_buffer, fieldnames=headers, extrasaction="ignore")
        csv_writer.writeheader()
        csv_writer.writerow(data)

        return csv_buffer.getvalue()


class ExcelStudentDataRendererDetail(renderers.BaseRenderer):

    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        headers = list(data.keys())
        worksheet.append(headers)
        worksheet.append([str(value) for value in data.values()])
        workbook.save(buffer)

        return buffer.getvalue()
