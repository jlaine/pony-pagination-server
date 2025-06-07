from django.test import TestCase


class PonyListTest(TestCase):
    fixtures = ["ponies.json"]

    def test_list_all(self):
        response = self.client.get("/v1/ponies")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "count": 21,
                "next": "http://testserver/v1/ponies?limit=5&offset=5",
                "previous": None,
                "results": [
                    {"id": 1, "is_available": True, "name": "Adorable Alfy"},
                    {"id": 2, "is_available": False, "name": "Brave Barbara"},
                    {"id": 3, "is_available": False, "name": "Cuddly Charlie"},
                    {"id": 4, "is_available": True, "name": "Devious Deborah"},
                    {"id": 5, "is_available": True, "name": "Extreme Ernest"},
                ],
            },
        )

    def test_list_available(self):
        response = self.client.get("/v1/ponies?is_available=true")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "count": 13,
                "next": "http://testserver/v1/ponies?is_available=true&limit=5&offset=5",
                "previous": None,
                "results": [
                    {"id": 1, "is_available": True, "name": "Adorable Alfy"},
                    {"id": 4, "is_available": True, "name": "Devious Deborah"},
                    {"id": 5, "is_available": True, "name": "Extreme Ernest"},
                    {"id": 6, "is_available": True, "name": "Furious Fanny"},
                    {"id": 8, "is_available": True, "name": "Holy Holly"},
                ],
            },
        )

    def test_list_search(self):
        response = self.client.get("/v1/ponies?search=alf")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {"id": 1, "is_available": True, "name": "Adorable Alfy"},
                ],
            },
        )
