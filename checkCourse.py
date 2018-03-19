#!/usr/bin/python3

import sys
import os
import json
import yaml
import requests
from lxml import html
from twilio.rest import Client


PAGE_URL = 'http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl'
API_URL = 'https://api.uwaterloo.ca/v2/terms/'
API_URL_2 = 'https://api.uwaterloo.ca/v2/courses/'

def check_api_terms(sess, subject, cournum):
    resp = requests.get(API_URL + sess + '/' + subject + '/enrollment.json?key=' + API_KEY)
    data = resp.json()['data']
    sections = [course for course in data if course['catalog_number'] == cournum and course['section'][:3] == 'LEC']
    isRoom = False

    for course in sections:
        print(str(course['enrollment_total']) + ' / ' + str(course['enrollment_capacity']))
        if (course['enrollment_total'] < course['enrollment_capacity']):
            isRoom = True

    return isRoom


def scrape_webpage(sess, subject, cournum):
    isRoom = False

    payload = {
        'level': 'under',
        'sess': sess,
        'subject': subject,
        'cournum': cournum
    }

    page = requests.post(PAGE_URL, data=payload)
    tree = html.fromstring(page.content)

    secType = tree.xpath('//table/tr[3]/td[2]/table/tr/td[2]/text()')
    cap = tree.xpath('//table/tr[3]/td[2]/table/tr/td[7]/text()')
    enrolled = tree.xpath('//table/tr[3]/td[2]/table/tr/td[8]/text()')

    print(secTypei)
    print(cap)
    print(enrolled)

    for i in range(len(secType)):
        if (secType[i][:3] == 'LEC'):
            if (int(cap[i]) - int(enrolled[i]) > 0):
                isRoom = True

    return isRoom


def check_api_courses(sess, subject, cournum):
    isRoom = False
    payload = {
        'term': sess,
        'key': API_KEY
    }
    resp = requests.get(API_URL_2 + subject + '/' + cournum + '/schedule.json', params=payload)
    data = resp.json()['data']
    sections = [section for section in data if section['section'][:3] == 'LEC']

    for section in sections:
        spaces = section['enrollment_capacity'] - section['enrollment_total']
        if (spaces <= 0):
            continue

        reserves = section['reserves']
        reservedSpaces = 0
        for group in reserves:
            groupSpaces = group['enrollment_capacity'] - group['enrollment_total']
            if (groupSpaces > 0):
                reservedSpaces += groupSpaces

        if (spaces > reservedSpaces):
            isRoom = True
            break

    if isRoom:
        send_sms(subject, cournum)

    return isRoom


def send_sms(subject, cournum):
    client = Client(creds['client']['accountSID'], creds['client']['authToken'])
    client.messages.create(
        to=creds['message']['recipient'],
        from_=creds['message']['sender'],
        body="Space available in " + subject + " " + cournum + "!"
    )


if __name__ == '__main__':
    try:
        with open(os.path.expanduser('~/.config/armadillo/credentials.yml')) as cf:
            creds = yaml.load(cf)
    except IOError:
        sys.exit("You must provide a config file")

    API_KEY = creds['api_key']

    sess = sys.argv[1]
    subject = sys.argv[2]
    cournum = sys.argv[3]
    check_api_courses(sess, subject, cournum)
