from zillowdatamanager import DataManager
from listingdata import ListingData
from formmanager import FormFiller

dt = DataManager()
listing_data_list = []

for i in range(len(dt.price_list)):
    listing_data_list.append(ListingData(price=dt.price_list[i], url=dt.url_list[i], address=dt.address_list[i]))

ff = FormFiller(listing_data=listing_data_list)
