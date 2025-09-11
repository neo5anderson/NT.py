#!/bin/bash

PYTHON_VERSION=3.13
PYTHON_PATH=20250902

MIRROR_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
MIRROR_HOST="pypi.tuna.tsinghua.edu.cn"

CONFIG_PATH="$HOME/.config/uv/"
CONFIG_FILE="$CONFIG_PATH/uv.toml"

mkdir -p "$CONFIG_PATH"

cat > "$CONFIG_FILE" <<EOF
[[index]]
url = "$MIRROR_URL"
default = true
EOF

cd /root
mkdir -p ${PYTHON_PATH}
mv cpython-${PYTHON_VERSION}* ${PYTHON_PATH}
mv et.py ${PYTHON_PATH}

mv uv uvx /usr/local/bin
echo 'Installing deps...'
UV_PYTHON_INSTALL_MIRROR="file:///root" uv python install ${PYTHON_VERSION}

cd ${PYTHON_PATH}
uv init .
uv add exif pyinstaller pillow
echo 'Building et...'
uv run pyinstaller -F et.py && mv dist/et /usr/local/bin # && cd /root && rm -rf /root/20250902

echo 'Cleanup...'
# uv python uninstall ${PYTHON_VERSION} && rm /usr/local/bin/uv*

echo 'Done'
ls -lh /usr/local/bin/et
et -v

