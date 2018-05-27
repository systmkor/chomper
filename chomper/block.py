import json
import rules
import rfc3339

class Block():

    def __init__(self, start, stop, rules):
        self.block_id = None  # uuid
        self.start = start  # start timestamp (date-time)
        self.stop = stop  # stop timestamp (date-time)
        self.rules = rules  # dictionary of enabled rule objects

    def enforce():
        """The block is enforced"""
        # start mitmproxy
        # redirect traffic through mitmproxy
        pass

    def halt():
        """THe block is no longer enforced"""
        # remove traffic redirect through mitmproxy
        # stop mitmproxy
        pass

# TODO is there better way for nested objects to marshall/codec
class BlockJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Block):
            return json.JSONEncoder.default(self, obj)


        d = {}
        d['start'] = rfc3339.format(obj.start)
        d['stop'] = rfc3339.format(obj.stop)
        d['rules'] = {}
        for name, rule in obj.rules.items():
            d['rules'][name] = rules.RuleJSONEncoder().default(rule)
        return d


# TODO
# class BlockJSONDecoder(json.JSONDecoder):

