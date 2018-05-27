import clicker

# arguments
#
# commands
# rules 
#   enable <rule>...
#   disable <rule>...
# list enabled rules
# list all rules
# enforce block
#   --at (enforce --at 16:00)
#   --in (enforce --in HH:MM:SS)
#   --for (enforce --for HH:MM:SS)
# halt block
#   --at (halt --at 17:00)
#   --in (halt --at HH:MM:SS)
#   --for (halt --for HH:MM:SS)

@click.command()
#@click.option('--all', help='List All Known Rules')
#@click.option('--all-enabled', help='List all enabled rules')
def list():
    """List"""
    # List the current rules
    # if list_all == true
    #  list all rules (basically rule file)

    # default is list enabled rules (i.e. rules enabled apart of block)
    pass


@click.group()
def rules():
    """Rules"""
    pass

#@click.command() #? @click.subcommand()? or @click.command(parent=rules)
#@click.argument('rule') #list of input rules <rule>...
@click.argument('rule', nargs=-1)
def rules_enable():
    """Rules to enable"""
    # if this command is called when a block DNE then you are adding which
    # rulesets to be activated when the halt is enforced
    # if this command is called during an active block (it will only successfully work)
    # during a (wratcheting) block were you are increase the restrictiveness
    # if this is a black-list block then you can add more rules to black-list
    # if this is a white-list block then you can only remove rules from the white-list


    # TODO below is far too many nested conditionals
    # get block state
    # if enforcing
    #   if block_mode.allows_modify
    #      if block_mode.type == whitelist
    #         error
    #      if block_mode.type = blacklist
    #         error
    #
    # else
    #  remove rules
    pass

@click.command()
#@click.argument('rule') #list of input rules <rule>...
def rules_disable():
    """Rules to disable"""
    # if this command is called when a block DNE then you are removing which
    # rulesets to be activated when the halt is enforced
    # if this command is called during an active block (it will only successfully work)
    # during a (wratcheting) block were you are increase the restrictiveness
    # if this is a black-list block then you can add more rules to black-list
    # if this is a white-list block then you can only remove rules from the white-list

    # TODO below is far too many nested conditionals
    # get block state
    # if enforcing
    #   if block_mode.allows_modify
    #      if block_mode.type == whitelist
    #         remove rules
    #      if block_mode.type = blacklist
    #         error
    #
    # else
    #  remove rules
    pass

@click.command()
#@click.option('--at', help='Enforace block at HH:MM:SS')
#@click.option('--in', help='Enforace block in HH:MM:SS')
#@click.option('--for', help='Enforace block for duration HH:MM:SS')
def enforce():
    """Enforce block"""
    # Begin a Block on the specified rules

    # load block state

    # if already enforcing block
    #   return error

    # handle arguments
    # update block

    # if no rules are defined
    #   return error

    # enforce block
    pass

@click.command()
#@click.option('--at', help='Enforace block at HH:MM:SS')
#@click.option('--in', help='Enforace block in HH:MM:SS')
#@click.option('--for', help='Enforace block for duration HH:MM:SS')
def halt():
    """Halt block"""
    # Halt the current Block State

    # load block state

    # if not already enforcing block
    #   return error

    # handle arguments
    # update block

    # halt block
    pass
