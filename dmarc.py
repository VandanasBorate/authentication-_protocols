import dns.resolver

def get_dmarc_record(domain):
    try:
        # Query DMARC record
        query = f"_dmarc.{domain}"
        answers = dns.resolver.resolve(query, 'TXT')
        for rdata in answers:
            for txt_record in rdata.strings:
                if txt_record.startswith(b'v=DMARC1'):
                    return txt_record.decode('utf-8')
    except dns.resolver.NoAnswer:
        print(f"No DMARC record found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain name does not exist: {domain}")
    except Exception as e:
        print(f"Error: {e}")
    return None

# Domain to check
domain = "google.com"  # Main domain for DMARC check
dmarc_record = get_dmarc_record(domain)
if dmarc_record:
    print(f"DMARC Record for {domain}: {dmarc_record}")
else:
    print(f"No DMARC record found for {domain}")
