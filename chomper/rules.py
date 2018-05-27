import enum
import json
import yaml

class RuleType(enum.Enum):
    WHITE_LIST = enum.auto()
    BLACK_LIST = enum.auto()

class Rules(dict):
    def __init__(self):
        super(dict, self).__init__()

# Rule, RuleList, RuleSet ??
class Rule():
    def __init__(self, name, rule_type, addresses):
        self.name = name #string
        self.rule_type = rule_type
        self.addresses = addresses # TODO should be a set not list


# TODO Should it be called a Rule Type or Block Type (Both?)?

# TODO cleanup code below, a bit messy
def load(rules_file):
    """Function takes in given rules file and returns a dictionary of rule
       objects"""
    yaml_import = yaml.load(rules_file.read())
    rules = {}
    for key, value in yaml_import.items():
        rule_name = key # TODO sanitize name
        rule_type = None
        if (value[0]['block_type'][0] == "whitelist"):
            rule_type = RuleType.WHITE_LIST
        elif (value[0]['block_type'][0] == "blacklist"):
            rule_type = RuleType.BLACK_LIST
        else:
            # TODO print/log/throw error
            pass

        rule_addresses = value[1]['addresses']

        rules[rule_name] = Rule(rule_name, rule_type, rule_addresses)

    return rules

def is_valid(rules):
    """Takes in parsed rules file (yaml) and ensures is valid"""
    pass


class RuleJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Rule):
            return json.JSONEncoder.default(self, obj)

        d = {}
        d['name'] = obj.name
        if obj.rule_type == RuleType.WHITE_LIST:
            d['type'] = 'whitelist'
        if obj.rule_type == RuleType.BLACK_LIST:
            d['type'] = 'blacklist'
        d['addresses'] = obj.addresses

        return d

