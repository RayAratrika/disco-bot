# Ensure default configs exist to prevent unnecessary bail outs and API calls
if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample_config to a seperate config.py file, don't just rename and change "
          "values here.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    BOT_TOKEN = "YOUR TOKEN HERE"
    API_KEY = "YOUR KEY HERE"
    USER_AGENT = "YOUR NAME HERE"

    # OPTIONAL
    BOT_COLOR = 0xFFA000


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
