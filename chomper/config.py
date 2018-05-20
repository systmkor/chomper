import yaml


def load(conf_file):
    """Load a chomper configuration file, (validates configuration) if valid
    returns conf object, otherwise returns None & throws error """

    conf = yaml.load(conf_file.read())

    if is_valid(conf):
        return conf

    return None


def is_valid(conf):
    """Validate a chomper configuration file, returns True if no errors, false
    otherwise"""

    # Do validation checks: if any issues/errors return False

    return True
