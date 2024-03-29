# Python imports
import re


class GetTableData:
    """
    Get the relevant data from the table and return a JSON object with 3 different keys ->
        -Driver Details
        -Validity
        -Class Of Vehicle
    """

    def __init__(self, table):
        self.table = table

    def get_driver_details(self, list1):
        details = dict()

        for i in range(0, len(list1), 2):
            # Trim any leading/trailing whitespaces
            key = list1[i].text[:-1].strip()
            # Trim any leading/trailing whitespaces
            value = re.sub(' +', ' ', list1[i + 1].text.strip())
            details[key] = value

        return details

    def get_class(self, header, data):
        '''
        Handles different classes of vehicles
        '''
        final_details = list()

        for i in range(0, len(data), 3):
            details = dict()
            details[header[0].text] = data[i].text
            details[header[1].text] = data[i + 1].text
            details[header[2].text] = data[i + 2].text
            final_details.append(details)

        return final_details

    def get_validity(self, list1, list2):
        details = dict()

        for i in range(0, len(list1), 3):
            from_date = list1[i + 1].text[5:]
            to_date = list1[i + 2].text[3:]
            details[list1[i].text] = {"from": from_date, "to": to_date}

        for i in range(0, len(list2), 2):
            details[list2[i].text[:-1].strip()] = list2[i + 1].text.strip()

        return details

    def get_json(self):
        json_data = dict()

        self.table1 = self.table[0].find_all('td')
        self.table2 = self.table[1].find_all('td')
        self.table3 = self.table[2].find_all('td')
        self.table4 = self.table[3].find_all('th')
        self.table5 = self.table[3].find_all('td')

        json_data['Driver Details'] = self.get_driver_details(self.table1)
        json_data['Validity'] = self.get_validity(self.table2, self.table3)
        json_data['Class Of Vehicle'] = self.get_class(
            self.table4, self.table5)

        return json_data
