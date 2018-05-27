
def proxy_conf():
    # probably to be a class that has the necessary configurations for the
    # proxy
    pass

def start_proxy():
    # subprocess.exec (proxy command w/ options/conf/arguments)
    pass

def _save_proxy_pid():
    # not sure which is best method for this to work
    # PID file
    # apart of block state ? (seems out of scope of the block state)
    pass

def get_proxy_pid():
    # read in PID from pid-file
    # if no pid-file (search for processes) use other stored pid
    # if not stored PID, search for proxy process (pgrep, etc.)

    # return PID
    pass

def stop_proxy():
    # get_proxy_pid
    # kill process for pid
    pass
