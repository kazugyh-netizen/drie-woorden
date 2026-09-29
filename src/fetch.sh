cd "$(dirname "$0")"
curl -fL -o nl_50k.txt https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/nl/nl_50k.txt
curl -fL -o opentaal.txt https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/elements/basiswoorden-gekeurd.txt
curl -fL -o jmdict-all.json.tgz "$(gh api repos/scriptin/jmdict-simplified/releases/latest --jq '.assets[]|select(.name|test("jmdict-all-.*json.tgz"))|.browser_download_url')" && tar xzf jmdict-all.json.tgz
