# Armadillo
Be notified by text message the instant a University of Waterloo course you're interested in has an open spot



## Install
#### Dependencies

- [lxml](https://github.com/lxml/lxml)
- [requests](https://github.com/requests/requests)
- [Twilio helper library](https://pypi.python.org/pypi/twilio) (version >= 6.0.0)

You can install these from their source pages.
You can also use [pip](https://github.com/pypa/pip) with or without [virtualenv](https://virtualenv.pypa.io/en/latest/):
```
sudo pip install lxml requests twilio
```

#### Install Armadillo
```
git clone git@github.com:Samwisemr/armadillo.git
cd armadillo
sudo make
```

#### Acquire UW API key
You'll need to acquire a University of Waterloo API key, which you can do [here](https://uwaterloo.ca/api/)

#### Setup SMS
Now you'll need to [sign up for a free Twilio trial](https://www.twilio.com/try-twilio) if you don't already have a Twilio account. After signing up, Twilio will prompt you to generate a phone number to send sms texts from, which you should do.

---

You can now set up your `credentials.yml` file as instructed in the file itself. Once you have filled in each field, run `sudo make` and you're done!


## Usage





# TODO
 - document additional scraper functions
 - automate running
 - finish readme with usage instructions
