#!/usr/bin/env python

from functions import *
from game import *


def main():
    # show_title_screen()
    wardrobe = read_json('wardrobe')
    places = read_json('places')
    location_id = 0
    locations = places['locations']
    nearby = render_location(0, locations)

    print("Nearby:", nearby)


if __name__ == "__main__":
    main()
