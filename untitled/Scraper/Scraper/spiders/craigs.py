# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from scrapy.spider import BaseSpider


# from scrapy.selector import HtmlXPathSelector
# from scrapy.selector import Selector


class CraigsSpider(BaseSpider):
    name = "craigs"
    allowed_domains = ["myspace.com", 'facebook.com', 'plentyoffish.com',
                       'gotinder.com', 'tagged.com', 'zoosk.com', 'match.com',
                       'elitesingles.com', 'adultfriendfinder.com',
                       'wooplus.com', 'sapio.com', 'hitwe.com', 'speeddatemate.com',
                       'okcupid.com', 'grindr.com', 'downapp.com', 'twitter.com']

    start_urls = ['https://www.plentyoffish.com',
                  'https://www.facebook.com', 'https://www.tagged.com',
                  'https://www.gotinder.com', 'https://www.myspace.com',
                  'https://www.zoosk.com', 'https://www.match.com',
                  'https://www.elitesingles.com', 'https://www.adultfriendfinder.com',
                  'https://www.wooplus.com', 'https://www.sapio.com', 'https://www.hitwe.com',
                  'http://www.speeddatemate.com/', 'https://www.okcupid.com/', 'http://www.grindr.com/',
                  'https://www.downapp.com/', 'https://www.twitter.com'
                  ]

    facebook_profile = '//*[@id="content"]/div'
    facebook_info = dict(name='//*[@id="fbCoverImageContainer"]', picture='//*[@id="u_jsonp_6_8"]/img',
                         location='//*[@id="js_1oe"]',
                         relationship_snapshot='//*[@id="u_jsonp_14_1i"]/div/div/div/div',
                         relationship='//*[@id="u_jsonp_9_7"]/div/ul/li[5]/a/span[1]',
                         spouse_information='//*[@id="js_4jl"]')
    myspace_profile = ''
    myspace_info = dict(name='', pic='', location='', relationship='')

    twitter_profile = ''
    twitter_information = dict(name='', picture='', location='', )

    plenty_of_fish_picture = '//*[@id="container"]'
    plenty_of_fish = dict(name='//*[@id="container"]/div[3]', location='//*[@id="user-details-wrapper"]/div[2]',
                          links='//*[@id="image-bar"]/div[1]/a/img', intent='//*[@id="user-details-wrapper"]/div[5]',
                          lastActive='', profilePicture='//*[@id="mp"]')

    # tinder_picture = '' to do, tinder doesnt have a website yet.
    # tinder_profile = { '' }

    tagged_Profile = ''
    tagged_info = dict(name='', location='', picture='', last_login='')

    zoosk_profile = ''
    zoosk_info = dict(name='', location='', picture='', last_active='')

    match_profile = ''
    match_info = dict(name='', location='', picture='', last_active='')

    leet_singles_profile = ''
    leet_singles_info = dict(name='', location='', picture='', last_active='')

    aff_profile = ''
    aff_info = dict(name='', location='', picture='', last_login='')

    woo_profile = ''
    woo_info = dict(name='', location='', picture='', last_login='')

    sapio_profile = ''
    sapio_info = dict(name='', location='', picture='', last_login='')

    hitwe_profile = ''
    hitwe_info = dict(name='', location='', picture='', last_login='')

    speeddateme_profile = ''
    speeddate_info = dict(name='', location='', picture='', last_login='')

    okcupid_profile = ''
    okcupid_info = dict(name='', location='', picture='', last_login='')

    # grinder_picture = ''   to do right here, gotta check the grinder API
    # grinder_profile = { '' }

    downapp_profile = ''
    downapp_info = dict(name='', location='', picture='', last_login='')

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        for link in soup.find_all('a'):
            print(link.get('href'))

        pass
