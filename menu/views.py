# from django.shortcuts import render
# from django.views import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


# data = {}
#
# # Opens up page as PDF
# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('app/menu_template.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
#
#
# # Automaticly downloads to PDF file
# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('app/menu_template.html', data)
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "recipe.pdf"
#         content = "attachment; filename='%s'" % filename
#         response['Content-Disposition'] = content
#         return response
#
#
# def index(request):
#     context = {}
#     return render(request, 'app/index.html', context)
