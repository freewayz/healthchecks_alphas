from hc.api.models import Check
from hc.test import BaseTestCase


class PauseTestCase(BaseTestCase):

    def test_it_works(self):
        check = Check(user=self.alice, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        ### Assert the expected status code and check's status

        self.assertEqual(r.status_code, 200)

    def test_it_validates_ownership(self):
        check = Check(user=self.bob, status="up")
        check.save()

        url = "/api/v1/checks/%s/pause" % check.code
        r = self.client.post(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r.status_code, 400)

        ### Test that it only allows post requests
        r1 = self.client.get(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r1.status_code, 405)

        r2 = self.client.put(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r2.status_code, 405)

        r3 = self.client.patch(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r3.status_code, 405)

        r4 = self.client.delete(url, "", content_type="application/json",
                             HTTP_X_API_KEY="abc")

        self.assertEqual(r4.status_code, 405)


        
        