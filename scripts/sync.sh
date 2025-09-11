#!env bash
src=bsf
dst=bs

docker cp $src:$1 ./$2
docker cp $2 $dst:$1
