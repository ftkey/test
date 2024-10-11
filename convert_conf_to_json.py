import json

def parse_conf(conf_file):
    rules = []
    with open(conf_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('DOMAIN-SUFFIX,'):
                rule = {"domain_suffix": line.split(',')[1].strip()}
                rules.append(rule)
            elif line.startswith('IP-CIDR,'):
                rule = {"ip_cidr": line.split(',')[1].strip()}
                rules.append(rule)
            elif line.startswith('DOMAIN-KEYWORD,'):
                rule = {"domain_keyword": line.split(',')[1].strip()}
                rules.append(rule)
            elif line.startswith('DOMAIN,'):
                rule = {"domain": line.split(',')[1].strip()}
                rules.append(rule)
            elif line.startswith('DOMAIN-SUFFIX,'):
                rule = {"domain_suffix": line.split(',')[1].strip()}
                rules.append(rule)
    return rules

def convert_conf_to_json(conf_file, json_file):
    rules = parse_conf(conf_file)
    output = {"version": 1, "rules": rules}
    with open(json_file, 'w') as f:
        json.dump(output, f, indent=4)

convert_conf_to_json('sr_top500_banlist.conf', 'sbrule.json')
