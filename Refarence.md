
# Refarence Commands

Generate Slides

```bash
DIR=./umbrella/KO/
docker run --rm -v $PWD:/home/marp/app/ -e LANG=$LANG -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli $DIR/README.md --theme ./style.css -o $DIR/index.html
```

node

```bash
docker run -it --rm -v $PWD:/usr/src/app -w /usr/src/app node:22-alpine /bin/sh
```

Setup Python environment

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
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
