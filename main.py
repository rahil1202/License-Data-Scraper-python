# python imports
import argparse
import json
from pprint import pprint

# project level imports
from scraper.getDetails import GetDetails


def check_validity_dl(dl_no):
    return len(dl_no) == 16 and dl_no[2] == '-'


def check_validity_dob(dob):
    return len(dob) == 10 and dob[2] == dob[5] == '-'


def main():
    help_text = "Example Command: python main.py -dl \"DL-0420110149646\" -dob \"09-02-1976\""

    arg_parser = argparse.ArgumentParser(description=help_text)
    arg_parser.add_argument(
        '-dl', required=True, help='Your Driving License Number in the specified format')
    arg_parser.add_argument('-dob', required=True,
                            help='Your Date Of Birth (dd-mm-yyyy)')

    args = arg_parser.parse_args()

    dl_no = args.dl
    dob = args.dob

    if not check_validity_dl(dl_no):
        print("Please check the license number format and try again")
    elif not check_validity_dob(dob):
        print("Please check the date of birth format and try again")
    else:
        response = GetDetails(dl_no, dob).scrape()
        print("Data received ->\n")
        pprint(response)
        if response:
            with open('driver_data.json', 'w') as output:
                json.dump(response, output, indent=1)
                print("\nAll details successfully stored in driver_data.json\n")


if __name__ == "__main__":
    main()
