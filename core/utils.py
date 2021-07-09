from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template #trae la informacion de django en pdf
from xhtml2pdf import pisa #convierte html en pdf

def imprimir_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='Clarita/pdf')
    return None
