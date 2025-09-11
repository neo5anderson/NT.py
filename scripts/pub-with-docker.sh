#!/bin/bash

# prepare uv: https://github.com/astral-sh/uv/releases
# prepare python: https://github.com/astral-sh/python-build-standalone/releases

if [ -z "$1" ]; then
	echo "expect container name"
	exit 1
fi

for i in output/et/*; do
	docker cp "$i" $1:/root/
done

docker exec $1 /root/pub-with-docker.sh
docker cp $1:/usr/local/bin/et .

