import os

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle

from src.shopping.models import Order, OrderStatusChoices


def generate_invoice(order, user):
    doc = SimpleDocTemplate(
        settings.EMAIL_ATTACHMENT_PATH + f'/invoice-{order.id}.pdf',
        pagesize=letter
    )
    elements = []

    # Company details
    company_data = [[
        'Company Name: Paperbound Pavilion'
    ], ['Description: An online bookstore offering a wide variety of books.'],
                    ['Address: 123 Main St, Anytown, USA'],
                    ['Contact: info@paperboundpavilion.com'], ['', '', '', '']]

    company_table = Table(company_data)
    elements.append(company_table)
    elements.append(Spacer(1, 0.25 * inch))

    state = order.address.state + ', ' if order.address.state else ' '
    address = f'{order.address.house}, \
    {order.address.street}, \
    {order.address.city}, \
    {state}{order.address.get_country_display()}, \
    Postal Code: {order.address.post_code}'

    # Invoice details
    data = [['Invoice'], ['Order ID:', order.id], ['User:', user.username],
            ['Address:', address],
            ['Order Date:',
             order.created_at.strftime('%m/%d/%Y')], ['', '', '', '']]

    order_details_table = Table(data)
    elements.append(order_details_table)
    elements.append(Spacer(1, 0.25 * inch))

    data = [['Item', 'Quantity', 'Price', 'Total']]

    for item in order.orderbooks.all():
        if item.out_of_stock:
            continue
        data.append([
            item.book.title, item.quantity, item.price,
            item.quantity * item.price
        ])

    data.append(['', '', 'Grand Total', order.total_price()])

    table = Table(data)

    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-2, -2), colors.beige),
                        ('GRID', (0, 1), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    elements.append(table)
    doc.build(elements)


@shared_task
def send_confirmation_email(order_id):
    order = Order.objects.get(pk=order_id)
    recipient_list = [order.user.email]
    generate_invoice(order, order.user)
    attachment = settings.EMAIL_ATTACHMENT_PATH + f'/invoice-{order.id}.pdf'
    message = 'Your order has been confirmed. Here is your invoice. \
        Thank you for shopping with us.',
    email_message = EmailMessage(
        'Order Confirmation', message, settings.EMAIL_HOST_USER, recipient_list
    )
    email_message.attach_file(attachment)
    email_message.send(fail_silently=False)

    order.status = OrderStatusChoices.CONFIRMED
    order.save()

    os.remove(attachment)
