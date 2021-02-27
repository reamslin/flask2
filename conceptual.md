### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?

RESTful routing is when you follow the REST principles for sending requests/responses through HTTP. The Representational State Transfer protocol provides a mapping between HTTP verbs and CRUD operations to a database. In order to be RESTful, routes must follow the mapping and requests must contain all information needed to send the response.

- What is a resource?

A resource is some type of data, either html, json, or some other format that can be requested through HTTP.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?

Since it is a JSON API, the data will be sent via JSON and no form will need to be filled out by the user.

- What does idempotent mean? Which HTTP verbs are idempotent?

if an operation is idempotent, that means that the result of performing the operation is the same no matter how many times the operation is called. PUT, DELETE, and GET are idempotent.

- What is the difference between PUT and PATCH?

PUT allows you to replace a resource with a new version, while PATCH allows you to update parts of a resource.

- What is one way encryption?

One way encryption is a function in which there is no inverse. You can not decrypt a one way encrypted resource.


- What is the purpose of a `salt` when hashing a password?

A 'salt' provides an additional argument to a hashing function. It's purpose is to prevent hasing results from being predictable. 

- What is the purpose of the Bcrypt module?

It provides us with string hashing functions.

- What is the difference between authorization and authentication?

Authorization is a process to determine if a user has permission to access a resource, while authentication is a process to determine if a user is who they say they are.