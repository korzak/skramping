# pip install python-whois  # run terminal

import whois
domainName = "sql.com"
# W_2 = whois.whois(domainName) # No work domain ru
# print(W_2)

def get_whois_info(domain_name):
    try:
        parsed_whois_info = whois.whois(domain_name)
    except whois.parser.PywhoisError as e:
        error_message = str(e)
        if error_message.startswith("No match for"):
            error_message = error_message.split(os.linesep)[0]
        return False, error_message
    return True, parsed_whois_info


print( get_whois_info(domainName))