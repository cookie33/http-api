# -*- coding: utf-8 -*-

"""
Run unittests inside the RAPyDo framework
"""

# from utilities import htmlcodes as hcodes
from restapi.tests import BaseTests  # , API_URI, AUTH_URI
from utilities.logs import get_logger

log = get_logger(__name__)


class TestIngestion(BaseTests):

    _main_endpoint = '/ingestion'

    def test_01_GET_giveityourname(self, client):

        assert True

        # endpoint = API_URI + self._main_endpoint
        # log.info('*** Testing GET call on %s' % endpoint)

        # r = client.get(endpoint)  # If NO authorization required
        # # headers, _ = self.do_login(client, None, None)
        # # r = client.get(
        # #     endpoint,
        # #     headers=headers  # If authorization required
        # # )

        # # Assert what is right or wrong
        # self.assertEqual(r.status_code, hcodes.HTTP_OK_BASIC)
        # output = self.get_content(r)

        # # pretty print data obtained from API to check the content
        # # log.pp(output)
        # assert output == 'Hello world!'
