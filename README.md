Get started by customizing your environment (defined in the .idx/dev.nix file) with the tools and IDE extensions you'll need for your project!

Learn more at https://firebase.google.com/docs/studio/customize-workspace

## Using JWT for API Access

This API uses JSON Web Tokens (JWT) for authentication and authorization. To access protected endpoints, you need to include a valid JWT in the `Authorization` header of your HTTP requests.

**Steps:**

1. **Obtain a JWT:**  You'll typically get a JWT by authenticating with the API (e.g., through a login endpoint). The details of how to obtain the token will depend on the specific authentication mechanism implemented by the API.  Refer to the API's documentation for instructions on user registration and login.
2. **Include the JWT in the request:**  For each request to a protected endpoint, set the `Authorization` header as follows:

   
