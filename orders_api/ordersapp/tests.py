import logging
import json
import string
import random
import requests
from random import choice
from django.test import TestCase


class APITests(TestCase):

    def test_create_order(self) -> int:
        """ This method creates an order using POST request,
            :return res_id: the id or created order
        """
        order = {"description": APITests.random_data(),
                 "price": random.randint(10, 100)}
        req = requests.post('http://127.0.0.1:8000/ordersapp/orders/',
                            data=json.dumps(order),
                            headers={'content-type': 'application/json'})
        res_id = req.json()['id']
        assert req.status_code == 201

        return res_id

    def test_update_order(self):
        """ This method creates the order and updates it using PUT request,
            :return None
        """
        order = {"description": APITests.random_data(),
                 "price": random.randint(10, 100)}
        order_id = self.test_create_order()
        req = requests.put(
            'http://127.0.0.1:8000/ordersapp/orders/{}/'.format(order_id),
            data=json.dumps(order),
            headers={'content-type': 'application/json'})
        assert req.status_code == 200

    def test_delete_order(self):
        """ This method creates the order and deletes it using DELETE request,
            :return None
        """
        # order = {"description": "eraser", "price": "18"}
        order_id = self.test_create_order()
        req = requests.delete(
            'http://127.0.0.1:8000/ordersapp/orders/{}/'.format(order_id),
            headers={'content-type': 'application/json'})
        assert req.status_code == 204

    @staticmethod
    def test_view_all_orders():
        """ This method views all orders using GET request,
            :return None
        """
        req = requests.get('http://127.0.0.1:8000/ordersapp/orders',
                           headers={'content-type': 'application/json'})
        assert req.status_code == 200

    def test_view_order(self):
        """ This method views all orders using GET request,
            :return None
        """
        order_id = self.test_create_order()
        req = requests.get(
            'http://127.0.0.1:8000/ordersapp/orders/{}/'.format(order_id),
            headers={'content-type': 'application/json'})
        assert req.status_code == 200

        logging.info("Status of view the order: %s", req.status_code)
        logging.info("Response after viewing the order: %s", req)

    @staticmethod
    def random_data():
        """ Generate random data string """
        return ''.join(choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits)
                       for _ in range(10))
