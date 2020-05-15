## Setup instructions

### Python related installations
1. Download Python for Windows (Mac has it pre-installed by default) 

   https://installpython3.com/windows/

2. Install `pip` 
   
   https://pip.pypa.io/en/stable/installing/

3. Install the following packages in your command line / terminal

   `pip install --upgrade google-api-python-client`
   
   `pip install --upgrade google-auth-oauthlib google-auth-httplib2`
   
   `pip install wordcloud`

## Usage guide

1. Go to https://developers.google.com/youtube/registering_an_application to register for an API key by following the instructions there

2. Copy and paste the key into the `api_key.txt` file, replacing the first line with your API key

3. Ensure that the file name `fetch` and `output` are **not changed** as the `generatecloud.py` is dependent on these two folders

4. First run `scraper.py` which is housed in the `fetch` folder

5. After the `.CSV`s have been generated, go up by one directory and run `generatecloud.py`. The word cloud generated should be named `cloud.png`

## Customization

To modify / add / delete regions which you want to search for trending videos, modify `country_codes.txt`. 

## License
There are two licenses, one that represents the code housed inside the `fetch` directory and one for `generatecloud.py`. 

The former project is licensed under the BSD 2-Clause License - see the `LICENSE` file in `fetch` directory for details.

The file `generatecloud.py` is licensed under the MIT License - see the `LICENSE_generatecloud` file in this current directory for details.
