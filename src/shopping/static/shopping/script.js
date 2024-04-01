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

const send_cart_action_request = (url, token, product_id) => {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify({product_id}),
    });
};

const cart_action = async (product_id, url) => {
    const response = await send_cart_action_request(url, getCookie('csrftoken'), product_id);
    if (response.status === 200) {
        return response.json();
    }
    else {
        console.log(response.status);
    }
};

const add_to_cart = async (product_id, url, cur_page) => {
    data = await cart_action(product_id, url)
    console.log(data);
    if (cur_page === 'book') {
        if (data.cart_count === 1) {
            document.getElementById(`add_to_cart_btn${product_id}`).classList.remove('inline-block');
            document.getElementById(`add_to_cart_btn${product_id}`).classList.add('hidden');
            document.getElementById(`cart_btns${product_id}`).classList.remove('hidden');
        }
    }
    document.getElementById(`cart_count${product_id}`).innerHTML = data.cart_count;
};

const remove_from_cart = async (product_id, url, cur_page) => {
    data = await cart_action(product_id, url)
    console.log(data);
    console.log(data.cart_count);
    if (data.cart_count > 0) {
        console.log('here');
        document.getElementById(`cart_count${product_id}`).innerHTML = data.cart_count;
        return;
    }
    console.log(cur_page);
    if (cur_page === 'book') {
        delete_from_book_card(product_id);
    }
    else if (cur_page === 'cart') {
        delete_from_cart_list(product_id);
    }
};

const delete_from_cart = async (product_id, url) => {
    data = await cart_action(product_id, url)
    delete_from_cart_list(product_id);
}

const delete_from_book_card = (product_id) => {
    document.getElementById(`add_to_cart_btn${product_id}`).classList.add('inline-block');
    document.getElementById(`add_to_cart_btn${product_id}`).classList.remove('hidden');
    document.getElementById(`cart_btns${product_id}`).classList.add('hidden');
}

const delete_from_cart_list = (product_id) => {
    document.getElementById(`cart_count${product_id}`).parentElement.parentElement.remove();
}