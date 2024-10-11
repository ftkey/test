import json

def parse_conf(conf_file):
    rules = {
        "domain": [],
        "domain_suffix": [],
        "ip_cidr": []
    }
    with open(conf_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('DOMAIN-SUFFIX,'):
                domain = line.split(',')[1].strip()
                rules['domain_suffix'].extend(domain)
            elif line.startswith('IP-CIDR,'):
                ip_cidr = line.split(',')[1].strip()
                rules['ip_cidr'].extend(ip_cidr)
    return rules

def merge_rules(base_rules, new_rules):
    for key in new_rules:
        if key in base_rules:
            base_rules[key].extend(new_rules[key])
        else:
            base_rules[key] = new_rules[key]

def convert_conf_to_json(conf_file, json_file):
    base_rules = json.load(open(json_file, 'r'))
    new_rules = parse_conf(conf_file)
    merge_rules(base_rules, new_rules)
    output = {"version": 1, "rules": merge_rules}

    with open(json_file, 'w') as f:
        json.dump(base_rules, f, indent=4)

def convert_conf_to_json(conf_file, json_file):
    rules = parse_conf(conf_file)
    output = {"version": 1, "rules": [rules]}
    with open(json_file, 'w') as f:
        json.dump(output, f, indent=4)

convert_conf_to_json('sr_top500_banlist.conf', 'sbrule.json')
