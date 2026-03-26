# Arya Venture

Premium digital agency website.
Live at: https://aryaventure.com

## Stack
- Vanilla HTML5 / CSS3 / JS
- Three.js r162 (3D logo)
- GSAP 3 + ScrollTrigger (animations)
- Vercel (deployment)
- GitHub (version control)

## Local Development
Open index.html directly in browser for basic preview. For GLB loading, run a local server:

```
python3 -m http.server 8090
```

Then open http://localhost:8090

## Deployment
Push to main branch on GitHub.
Vercel auto-deploys on every push.

## Making Changes
1. Edit files locally in Cursor
2. git add .
3. git commit -m "describe change"
4. git push origin main
5. Vercel deploys automatically in ~30 seconds

## Files
- index.html — main site
- privacy-policy.html — legal
- cookie-policy.html — legal
- robots.txt — crawler instructions
- sitemap.xml — search engine sitemap
- llms.txt — AI search optimization
- vercel.json — deployment config
- *.glb — 3D logo model
- *.mp4 — video assets

## Environment
No environment variables required.
Replace GA4 placeholder G-XXXXXXXXXX with actual measurement ID before first deploy.
