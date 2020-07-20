# lets-get-this-bread
Let's get this bread!

## Auth0 Setup
- Make an auth0 acct (Not needed anymore since we all authenticating from Jacky's Auth0)
- Go into .env and fill in your own account credentials (So far only the AUTH0_CALLBACK_URL needs to be changed)
- Call_back URL is your heroku_url.com/callback
- In constants set your own profile and secret key (I believe not needed anymore since we auth from Jacky's)
- In your auth0 account settings make sure to whitelist the callback url as well as the logout
- Once you have your heroku url up and running send it to Jacky so she can whitelist it 
- Anything that doesn't need to be tracked please add it to the gitignoredfile