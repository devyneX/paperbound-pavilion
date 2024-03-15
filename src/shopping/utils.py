from decimal import Decimal
from uuid import uuid4

from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ


def format_address(address):
    return {
        'address1': f'{address.house}, {address.street}',
        'city': address.city,
        'state': address.state if address.state else '',
        'country': address.country.name,
        'post_code': address.post_code
    }


def init_getway(request, amount, customer, address, books, urls):
    sslcz = SSLCOMMERZ(settings.SSL_SESSIONS_CONFIG)

    # address = format_address(address)

    post_body = {
        'total_amount': Decimal(amount),
        'currency': 'BDT',
        'tran_id': str(uuid4()),
        'success_url': request.build_absolute_uri(urls.get('success')),
        'fail_url': request.build_absolute_uri(urls.get('fail')),
        'cancel_url': request.build_absolute_uri(urls.get('cancel')),
        'ipn_url': request.build_absolute_uri(urls.get('ipn')),
        'emi_option': 0,
        'cus_name': customer.get_full_name(),
        'cus_email': customer.email,
        'cus_add1': address.get('address1'),
        'cus_city': address.get('city'),
        'cus_state': address.get('state'),
        'cus_postcode': address.get('post_code'),
        'cus_country': address.get('country'),
        'cus_phone': customer.phone,
        'shipping_method': 'NO',
        'num_of_item': len(books),
        'product_name': ','.join([book.title for book in books]),
        'product_category': 'Books',
        'product_profile': 'general'
    }

    response = sslcz.createSession(post_body)

    return response


def verify_payment(post_body):
    sslcz = SSLCOMMERZ(settings.SSL_SESSIONS_CONFIG)
    if sslcz.hash_validate_ipn(post_body):
        return sslcz.validationTransactionOrder(post_body['val_id'])
    else:
        return False
