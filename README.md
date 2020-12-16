


<b>Third Party Authorization Service: Auth0:</b>

Account: arquitecto_usi03@minedu.gob.pe

password: *******

<b>Create Application:</b>


![Create app](resources/images/image01.png "Create app")

<b>Create Permissions:</b>

![Create permissions](resources/images/image02.png "Create permissions")

<b>Create Roles:</b> 

<i>Minedu Architect</i>
![Create architect](resources/images/image03.png "Create architect")


<i>Minedu QA</i>
![Create architect](resources/images/image04.png "Create architect")

<i>Minedu Technical Lead</i>
![Create technical lead](resources/images/image06.png "Create technical lead")


<i>Authorization code flow</i>
![Authorization code flow](resources/images/image07.png "Authorization code flow")

<b>Request and obtain Token: JWT</b>

GET https://dev-x5z4g2uf.us.auth0.com/authorize?
  audience=minedu&
  response_type=token&
  client_id=63NQ77tcwqfLJJej3hk7BZGEbADG18SR&
  redirect_uri=https://127.0.0.1:8080/login-results


<i>Registering arquitecto_usi03@minedu.gob.pe</i>
![Register](resources/images/image09.png "Register")


![Register](resources/images/image10.png "Register")

<b>JWT obtained:</b>

https://127.0.0.1:8080/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNQN25vam9zYWlDUlBROGQxbmhMMyJ9.eyJpc3MiOiJodHRwczovL2Rldi14NXo0ZzJ1Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkOTlmZjMzZjI3YzkwMDc1ZmRhYjlhIiwiYXVkIjoibWluZWR1IiwiaWF0IjoxNjA4MDk4MTE2LCJleHAiOjE2MDgxMDUzMTYsImF6cCI6IjYzTlE3N3Rjd3FmTEpKZWozaGs3QlpHRWJBREcxOFNSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6c3R1ZGVudHMiLCJkZWxldGU6dGVhY2hlcnMiLCJnZXQ6c3R1ZGVudHMiLCJnZXQ6dGVhY2hlcnMiLCJwYXRjaDpzdHVkZW50cyIsInBhdGNoOnRlYWNoZXJzIiwicG9zdDpzdHVkZW50cyIsInBvc3Q6dGVhY2hlcnMiXX0.qx0oDsOFY9kZ4NylSCfOCqupWcnbu2upNcJMXXrFpmHTQjzRysLjlR_ZPjgtlze2rco4qaamYR8uwrR_5YBM-4aDd09LoN1zZJXMAXpZKLU8BWRWx1uvannJcCRb5lN6wS8FLntSzuIb1XN-XgzuGorHX3EWd5NKl0qOWYVfqBw1xbF1x8K6U_HyNcajpIVbPxCo1RgbIS__02aK56EJ90z5QeGPWZAQ5bieDkwAV48WpP_aIRfJ6P4u_EQiJ7ZPMk0R4E283lpP3gDSWZvwX5rp3YtVv3mdw6zhrgx7De0vDd5CmRp48wLOMOMr3kJTLai-KoVsx591FEB4sGEYkw&expires_in=7200&token_type=Bearer


<b>Token:</b> <i>JWT</i>
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNQN25vam9zYWlDUlBROGQxbmhMMyJ9.eyJpc3MiOiJodHRwczovL2Rldi14NXo0ZzJ1Zi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZkOTlmZjMzZjI3YzkwMDc1ZmRhYjlhIiwiYXVkIjoibWluZWR1IiwiaWF0IjoxNjA4MDk4MTE2LCJleHAiOjE2MDgxMDUzMTYsImF6cCI6IjYzTlE3N3Rjd3FmTEpKZWozaGs3QlpHRWJBREcxOFNSIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6c3R1ZGVudHMiLCJkZWxldGU6dGVhY2hlcnMiLCJnZXQ6c3R1ZGVudHMiLCJnZXQ6dGVhY2hlcnMiLCJwYXRjaDpzdHVkZW50cyIsInBhdGNoOnRlYWNoZXJzIiwicG9zdDpzdHVkZW50cyIsInBvc3Q6dGVhY2hlcnMiXX0.qx0oDsOFY9kZ4NylSCfOCqupWcnbu2upNcJMXXrFpmHTQjzRysLjlR_ZPjgtlze2rco4qaamYR8uwrR_5YBM-4aDd09LoN1zZJXMAXpZKLU8BWRWx1uvannJcCRb5lN6wS8FLntSzuIb1XN-XgzuGorHX3EWd5NKl0qOWYVfqBw1xbF1x8K6U_HyNcajpIVbPxCo1RgbIS__02aK56EJ90z5QeGPWZAQ5bieDkwAV48WpP_aIRfJ6P4u_EQiJ7ZPMk0R4E283lpP3gDSWZvwX5rp3YtVv3mdw6zhrgx7De0vDd5CmRp48wLOMOMr3kJTLai-KoVsx591FEB4sGEYkw


<b>Steps to see permissions:</b>
<ol>
    <li>Enter to: https://jwt.io/</li>
    <li>paste Token displayed above</li>
</ol>

![Permission](resources/images/image11.png "Permission")






























