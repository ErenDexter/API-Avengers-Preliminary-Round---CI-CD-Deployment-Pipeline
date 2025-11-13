set -e

echo "Checking health endpoint..."

echo

echo "\nHealth check $(curl -f http://localhost:8000/health)"