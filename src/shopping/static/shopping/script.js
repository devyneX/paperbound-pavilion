const getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

const add_remove_cart = (product_id, url, handler=(data) => {
    console.log(document.getElementById(`cart_count${product_id}`));
    document.getElementById(`cart_count${product_id}`).innerHTML = data.cart_count;
}) => {
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({product_id}),
    })
    .then(response => {
        if (response.status === 200) {
            return response.json();
        }
    })
    .then(data => handler(data));
};

const delete_from_cart = (product_id, url) => {
    add_remove_cart(product_id, url, (data) => {
        document.getElementById(`cart_count${product_id}`).parentElement.parentElement.remove();
    });
};