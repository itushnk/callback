# AliExpress Callback (Flask on Railway)

This is a tiny web service that exposes `/ae/callback` for the AliExpress App Console.

## Deploy steps (Railway)

1. Create a **new service** (type: Web) and upload this folder or connect a repo with these files.
2. Make sure Railway detects Python via `requirements.txt`. It will install Flask and gunicorn.
3. **Start Command** (if prompted):
   ```
   gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 60
   ```
   (or set in a `Procfile` which is included here).
4. After deploy you get a `*.up.railway.app` URL. Open it — `/` should return `OK`.
5. In your DNS (smarthings.co.il), add a **CNAME** record for a subdomain, e.g. `callback.smarthings.co.il`, pointing to the Railway domain (e.g. `your-service.up.railway.app`).
6. Wait for DNS propagation (a few minutes). Then test:
   - `https://callback.smarthings.co.il/`
   - `https://callback.smarthings.co.il/ae/callback`
7. Put the following **Callback URL** in the AliExpress App Console:
   `https://callback.smarthings.co.il/ae/callback`

## Notes
- This callback is only needed for seller OAuth scenarios; for basic Affiliates API you won't actually use it, but the App Console requires a URL.
- The service logs any `code`/`state` query params to stdout so you'll see them in Railway logs.
