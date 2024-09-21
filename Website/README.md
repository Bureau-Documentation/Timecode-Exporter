## Usage
```
# Initialize
docker run --rm --name=npm -u 1000 -v /path/to/website:/app -w /app node:lts-slim npm init -y

# Install node modules
docker run --rm --name=npm -u 1000 -v /path/to/website:/app -w /app node:lts-slim npm install \
  npm \
  @11ty/eleventy \
  luxon \
  html-minifier \
  clean-css \
  markdown-it-attrs \
  markdown-it-bracketed-spans \
  markdown-it-anchor
```
```
# Generate website
docker run --rm --name=npm -u 1000 -v /Users/producer/Downloads/website:/app -w /app --network none node:lts-slim npx eleventy
```

# Test
docker run --rm --name my-website -p 8080:80 -v /Users/producer/Downloads/website/site:/usr/share/nginx/html -d nginx:alpine

```
# Update
docker run --rm --name=npm -u 1000 -v /path/to/website:/app -w /app node:lts-slim npm update
```
