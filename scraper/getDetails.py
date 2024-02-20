# Standard library imports
import sys
from pprint import pprint

# Third-party imports
import requests
from bs4 import BeautifulSoup

# Project-level imports
from .getTableData import GetTableData


get_url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'


class GetDetails:
    """
    This class scrapes driving license data from parivahan.gov.in
    """

    def __init__(self, dl_no, dob):
        self.dl_no = dl_no
        self.dob = dob

    def get_view_state(self, soup):
        view_state = soup.select('input[name="javax.faces.ViewState"]')[
            0]['value']
        return view_state

    def post_data(self, data, cookies):
        response = requests.post(url=post_url, data=data, cookies=cookies)
        response_data = BeautifulSoup(response.text, features='lxml')
        return response_data

    def validate_table(self, table):
        try:
            check_table = table[3]
        except IndexError:
            raise ValueError(
                "Invalid license number or DOB. Please check and try again")

    def scrape(self):
        data = {
            'javax.faces.partial.ajax': 'true',
            'javax.faces.source': 'form_rcdl:j_idt43',
            'javax.faces.partial.execute': '@all',
            'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
            'form_rcdl:j_idt43': 'form_rcdl:j_idt43',
            'form_rcdl': 'form_rcdl',
            "form_rcdl:tf_dlNO": self.dl_no,
            'form_rcdl:tf_dob_input': self.dob,
        }

        response = requests.get(url=get_url)
        cookies = response.cookies
        soup = BeautifulSoup(response.text, 'html.parser')

        # get the unique view state
        view_state = self.get_view_state(soup)
        data['javax.faces.ViewState'] = view_state

        response_data = self.post_data(data, cookies)

        table_list = response_data.find_all('table')

        self.validate_table(table_list)

        json_data = GetTableData(table_list).get_json()

        return json_data
