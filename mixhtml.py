# The main HTML for the whole page.
PAGE_HTML = """
<p>Welcome, {{user_name}}!</p>
<p>Products:</p>
<ul>
{% for product in product_list %}
    <li>{{ product.name }}:
        {{ product.price|format_price }}</li>
{% endfor %}
</ul>
"""

# The HTML for each product displayed.
PRODUCT_HTML = "<li>{prodname}: {price}</li>\n"

def make_page(username, products):
    product_html = ""
    for prodname, price in products.items():
        product_html += PRODUCT_HTML.format(prodname=prodname, price=price) #format在这里作用是什么？
    html = PAGE_HTML.format(name=username, products=product_html)
    return html

dic_products = {'egg':'$1.00','meat':'$15.00'}
print(make_page('yang',dic_products))
