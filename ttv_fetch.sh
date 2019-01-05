#!/bin/bash
cd "$(dirname "$0")"

FNAME="ttv.json"
URL="http://hmxuku36whbypzxi.onion/trash/ttv-list/ttv.json"

GNAME="${FNAME}.gz"
curl --fail -R -z "${GNAME}" -o "${GNAME}" -H "Accept-Encoding: gzip" "${URL}" && \
 python gen_m3u.py ${GNAME} 1> ttv.m3u && \
 tail -n+2 radio.m3u >> ttv.m3u && \
 sed 's/127.0.0.1/odroid.lan/' ttv.m3u > out_ttv.m3u
# gunzip -c "${GNAME}" >"${FNAME}"
