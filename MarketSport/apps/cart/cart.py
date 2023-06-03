from django.conf import settings
from apps.store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        product_clean_ids = []

        for id in product_ids:
            product_clean_ids.append(id)
            self.cart[str(id)]['product'] = Product.objects.get(pk=id)
        
        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product, quantity, update_q=False):
        id = str(product.id)
        title = product.title
        price = product.price
        size = product.size
        color = product.color

        if id not in self.cart:
            self.cart[id] = {'title':title,'id': id,'quantity':0,\
                            'price':price, 'size': size, 'color': color}
        
        if update_q==False:
            self.cart[id]['quantity'] = 1
        
        
        self.save()

    def remove(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    

    def increment(self, id):
        if id in self.cart:
            self.cart[id]['quantity'] += 1
            print('inc')
            self.save()
    
    def decrement(self, id):
        if id in self.cart:
            print('dec')
            self.cart[id]['quantity'] -= 1
            self.save()
        
        
    
