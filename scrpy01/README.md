# SCRPY01
A small flask based app that contains a security vulnerability. 

To run and test the code, ensure that docker is installed and running. And then execute the following commands:

```bash
docker-compose build
docker-compose up
```


### Challenge:
Have a look at the `app.py` code and spot the vulnerability then check the solution to find out if you got it right. 

<details>
<summary>Solution</summary>
The vulnerability presented in this challenge is Hardcoded Credentials.

```python
# Line number 8, the database password is hardcoded.
app.config['DB_PASSWORD'] = 'db-password'
```

For more information vist:
- https://cwe.mitre.org/data/definitions/798.html
- https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password
</details>

<details>
<summary>How to Fix?</summary>
...
</details>


### Explanation of the vulnerability:
YouTube Link: 