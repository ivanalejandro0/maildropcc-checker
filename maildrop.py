#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests

BASE_URL = "https://maildrop.cc/api/inbox"


# Note comment about API here:
# https://github.com/m242/maildrop/issues/18#issuecomment-158133564
class Maildrop:
    def __init__(self, inbox_name):
        self._inbox_name = inbox_name

    def inbox(self):
        url = "/".join([BASE_URL, self._inbox_name])
        response = requests.get(url)
        inbox = response.json()
        return inbox

    def message(self, email_id):
        url = "/".join([BASE_URL, self._inbox_name, email_id])
        response = requests.get(url)
        message = response.json()
        return message

    def delete(self, email_id):
        url = "/".join([BASE_URL, self._inbox_name, email_id])
        response = requests.delete(url)
        deleted = response.json()

        # this will return something like
        # {'deleted': 'email_id'}
        return deleted


if __name__ == "__main__":
    from pprint import pprint

    # email address: inbox + "@maildrop.cc"
    inbox = "test"

    maildrop = Maildrop(inbox)
    emails = maildrop.inbox()

    if not emails:
        print("No emails on this inbox")
        sys.exit(0)

    for email in emails:
        pprint(email)
        print("-" * 20)

    print("-" * 40)
    email_id = emails[0]['id']
    email = maildrop.message(email_id)

    pprint(email)

    # deleted = maildrop.delete(email_id)
    # pprint(deleted)
