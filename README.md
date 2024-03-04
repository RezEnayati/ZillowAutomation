**Zillow Data Manager**

This script `zillowdatamanager.py` is designed to scrape data from a Zillow Clone website and prepare it for use in the Zillow Automation project. It utilizes BeautifulSoup for web scraping and extracts URL, price, and address data from the Zillow Clone website.

### How to Use:

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```
     pip install requests
     pip install beautifulsoup4
     ```

2. **Usage:**
   - Import the `DataManager` class from `zillowdatamanager.py`.
   - Initialize an instance of the `DataManager` class.
   - The instance will automatically scrape data from the Zillow Clone website.

3. **Integration:**
   - After scraping data, integrate the extracted data with other components of the Zillow Automation project.

### Components:

1. **`zillowdatamanager.py`**:
   - `DataManager`: Scrapes data from the Zillow Clone website, including URLs, prices, and addresses.

2. **`listingdata.py`**:
   - `ListingData`: Represents a listing with price, address, and URL attributes.

3. **`formmanager.py`**:
   - `FormFiller`: Fills a Google Form with listing data.

### Example Usage:

```python
from zillowdatamanager import DataManager
from listingdata import ListingData

# Initialize DataManager
dt = DataManager()

# Extract listing data
listing_data_list = [ListingData(price=dt.price_list[i], url=dt.url_list[i], address=dt.address_list[i]) for i in range(len(dt.price_list))]

# Example of integrating with FormFiller
from formmanager import FormFiller
ff = FormFiller(listing_data=listing_data_list)
```

### Dependencies:

- `requests`: For making HTTP requests to the Zillow Clone website.
- `beautifulsoup4`: For parsing HTML content and extracting data.

### Note:

- Ensure that the Zillow Clone website structure remains consistent for accurate data extraction.
- Adjust XPath values in `FormFiller` class if the structure of the Google Form changes.
