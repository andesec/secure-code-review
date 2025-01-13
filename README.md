# SCRPY01
A small flask based app that contains a security vulnerability. Have a look at the `app.py` code and spot the vulnerability. 

<details>
<summary>Solution</summary>
The vulnerability presented in this challenge is Hardcoded Credentials.

```python
# Line number 8, the database password is hardcoded.
app.config['DB_PASSWORD'] = 'db-password'
```

For more information vist:
https://cwe.mitre.org/data/definitions/798.html
https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password
</details>

