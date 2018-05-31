import iptc

from . import netconf


class IPTables(netconf.NetConf):

    def redirect(self):
        ports = ['80', '443']
        proxy_port = '8080'

        # Create Chain
        nat_table = iptc.Table(iptc.Table.NAT)
        chomper_chain = nat_table.create_chain('chomper')

        # Add Redirect Rules to Chain
        for p in ports:
            rule = iptc.Rule(chain=chomper_chain)
            rule.protocol = 'tcp'

            match = iptc.Match(rule, 'tcp')
            match.dport = p
            rule.add_match(match)

            target = iptc.Target(rule, 'REDIRECT')
            target.to_ports = [proxy_port]
            rule.target = target

            chomper_chain.append_rule(rule)

        # Add Jump Return to OUTPUT
        rule = iptc.Rule(chain=chomper_chain)
        t = rule.create_target('RETURN')
        rule.target = t
        chomper_chain.append_rule(rule)

        # Add Jump Rule to chomper Chain in OUTPUT
        output_chain = iptc.Chain(nat_table, 'OUTPUT')
        rule = iptc.Rule(chain=output_chain)
        match = iptc.Match(rule, 'owner')
        match.uid_owner = '!root'
        rule.add_match(match)
        t = rule.create_target('chomper')
        rule.target = t
        output_chain.append_rule(rule)

    def reset(self):
        # Delete Matching Rule (jump to chomper chain)
        output_chain = iptc.Chain(nat_table, 'OUTPUT')
        rule = iptc.Rule(chain=output_chain)
        match = iptc.Match(rule, 'owner')
        match.uid_owner = '!root'
        rule.add_match(match)
        t = rule.create_target('chomper')
        rule.target = t
        output_chain.delete_rule(rule)

        # Flush Chomper Chain Rules
        chomper_chain = iptc.Chain(iptc.Table.NAT, 'chomper')
        chomper_chain.flush()

        # Delete chomper Chain
        chomper_chain.delete()


netconf.NetConf.register(IPTables)
