set -euo pipefail

URL="http://localhost:8000/health"
MAX_RETRIES=12
SLEEP_SECONDS=2

echo "Checking health endpoint at ${URL} (up to ${MAX_RETRIES} retries)"

count=0
while [ $count -lt $MAX_RETRIES ]; do
	if curl -sSf "$URL" >/dev/null 2>&1; then
		echo "Health check OK (attempt $((count+1)))"
		exit 0
	else
		echo "Health check attempt $((count+1)) failed; retrying in ${SLEEP_SECONDS}s..."
		sleep ${SLEEP_SECONDS}
	fi
	count=$((count+1))
done

echo "ERROR: service did not become healthy after ${MAX_RETRIES} attempts"
exit 2