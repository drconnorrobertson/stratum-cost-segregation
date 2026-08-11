#!/bin/bash
API_KEY="69c31f304cca19db01f82e3f51f4091e"
HOST="www.stratumcostsegregation.com"
URL="$1"
if [ -z "$URL" ]; then echo "Usage: $0 <url>"; exit 1; fi
curl -s -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d "{\"host\":\"$HOST\",\"key\":\"$API_KEY\",\"keyLocation\":\"https://$HOST/$API_KEY.txt\",\"urlList\":[\"$URL\"]}"
echo "Submitted $URL to IndexNow"
