#!/bin/python3
# Author: Jon Laberge

from pyshorteners import Shortener as s
import argparse
import sys

parser=argparse.ArgumentParser(
        description='''A script to shorten URLs''',
        epilog='''Enjoy.''')

# Default shortener is tinyurl as it does not require any additional configuration such as API keys etc.
parser.add_argument('--shortener', type=str, default='Tinyurl', help="Shortener: Tinyurl")
parser.add_argument('--url', type=str, default='https://google.ca', help="Your URL")
args=parser.parse_args()

def shortUrl(shortener, url):
    # Return shortened URL using the shortener provided
    return s(shortener).short(url)

print(shortUrl(args.shortener, args.url))

