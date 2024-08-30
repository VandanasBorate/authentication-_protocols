import spf

def check_spf(ip, sender, helo):
    result = spf.check2(i=ip, s=sender, h=helo)
    return result

# Example usage
ip = '209.85.220.65'  # Example IP of a Gmail mail server
sender = 'vandanasborate2193@gmail.com'
helo = 'mail.google.com'


spf_result = check_spf(ip, sender, helo)

print(f"SPF result: {spf_result[0]}")  # 'pass', 'fail', 'softfail', etc.
print(f"Explanation: {spf_result[1]}")  # Explanation of the result
