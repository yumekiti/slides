
# Refarence Commands

Generate Slides

```bash
DIR=./example/JA/
docker run --rm -v $PWD:/home/marp/app/ -e LANG=$LANG -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli $DIR/README.md --theme ./style.css -o $DIR/index.html
```

node

```bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app node:22-alpine /bin/sh
```

python

```bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app python:3.12-slim /bin/sh
```

Setup Python environment

```bash
pip3 install pillow
```

Convert white background to transparent

```bash
IMG=02
python3 white_to_transparent.py \
  --input ./umbrella/assets/${IMG}.png \
  --output ./umbrella/assets/${IMG}.png \
  --threshold 245
```
