def save(block, block_state_file):
    """Save a given block object's session state"""
    # json dump to state file (overwrite)
    block_state = { 'start': str(block.start),
            'stop': str(block.stop),
            'rules': block.rules }

    block_state_file.write(json.dumps(block_state))

    # TODO raise error if write fails


def load(block_state_file):
    """Load block session state and return a block object"""

    block_state = json.loads(block_state_file.read())
    # TODO handle error if read() fails

    if is_valid(block_state):
        return Block(block_state['start'],
                block_state['stop'],
                block_state['rules'])

    # TODO raise error
    return None

def is_valid(block_state):
    """Verifies given block state dictionary is valid to become a block object"""
    # TODO validate block_state values
    return True
