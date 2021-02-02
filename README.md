openeuler-wiki-bot
==============
## 使用方法
```bash
usage: openeuler-wiki-bot.py [-h] [-l] [-r] [-s SIG] [-a]

openEuler wiki bot.

optional arguments:
  -h, --help         show this help message and exit
  -l, --list         List all sig info.
  -r, --report       Generate information report.
  -s SIG, --sig SIG  Specify sig group.
  -a, --all          Report information for all sig.
```

#### 举例：获取sig列表
```bash
./openeuler-wiki-bot.py -l
```

#### 举例：获取sig-ai-bigdata的所有issue和pr
```bash
./openeuler-wiki-bot.py -r -s sig-ai-bigdata
```
