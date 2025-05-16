import csv

# Expanded data to represent web traffic with more attack types
data = [
    ["/home", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/about", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/login?username=admin&password=' OR 1=1--", "POST", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "SQLi", "malicious"],
    ["/search?query=<script>alert('XSS')</script>", "GET", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "XSS", "malicious"],
    ["/profile?username=<img src=\"x\" onerror=\"alert(1)\">", "GET", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "XSS", "malicious"],
    ["/products?id=../../../../etc/passwd", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "Path Traversal", "malicious"],
    ["/login?username=admin&password=1234", "POST", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "None", "normal"],
    ["/update_profile?id=../../../../etc/passwd", "POST", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "Path Traversal", "malicious"],
    ["/purchase?amount=1000&item=xyz&csrf_token=xyz", "GET", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "CSRF", "malicious"],
    ["/admin/dashboard", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/profile?id=../../../etc/passwd", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "RFI", "malicious"],
    ["/contact", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/admin/delete_user?id=1234", "POST", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None",
     "normal"],
    ["/search?query=' UNION SELECT * FROM users--", "GET", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "SQLi", "malicious"],
    ["/upload_file?file=../../../../../etc/passwd", "POST", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "RFI", "malicious"],
    ["/checkout?csrf_token=xyz123&order=abc", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "CSRF", "malicious"],
    ["/dashboard?user=<script>evil()</script>", "GET", "Mozilla/5.0 (Windows)", "https://example.com/",
     "sessionid=12345", "XSS", "malicious"],
    ["/reset_password?token=12345", "POST", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None",
     "normal"],
    ["/admin/settings?cmd=ls", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "RFI",
     "malicious"],
    ["/home?search=1%20OR%20'1'='1", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "SQLi",
     "malicious"],
    ["/images?img=../../../etc/passwd", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "Path Traversal", "malicious"],
    ["/products?id=12345", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/cart", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None", "normal"],
    ["/profile?id=../../../../../etc/passwd", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "Path Traversal", "malicious"],
    ["/admin/reset?user=admin", "POST", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345", "None",
     "normal"],
    ["/search?term='; DROP TABLE users--", "GET", "Mozilla/5.0 (Windows)", "https://example.com/", "sessionid=12345",
     "SQLi", "malicious"],
    ["/user/info?username=admin&password=<script>alert('XSS')</script>", "GET", "Mozilla/5.0 (Windows)",
     "https://example.com/", "sessionid=12345", "XSS", "malicious"]
]

# Write the expanded data to a CSV file
with open('expanded_waf_traffic_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow(["request_url", "request_method", "user_agent", "referrer", "cookie", "attack_type", "label"])

    # Write data
    for row in data:
        writer.writerow(row)

print("Expanded CSV dataset has been generated.")