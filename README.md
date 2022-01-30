# openeuler-wiki-bot
===============================================================================

## 功能介绍

定位为openEuler运营助手，用于帮助开发者查询openEuler相关信息，帮助运营者获取openEuler相关报告，目前想到的功能为：

- 查询openEuler整体相关信息
  - openEuler包含哪些SIG
  - openEuler上SIG运营情况
  - openEuler上有哪些分支
  - openEuler已发布哪些版本
  - openEuler后续版本计划
  - openEuler南北向兼容列表
  - openEuler上安全漏洞发布情况
  - 。。。
    
- 生成openEuler整体运营报告
  - openEuler上sig运营报告
  - openEuler上版本发布报告
  - openEuler上软件包发布计划
  - openEuler上issue和pr报告
  - openEuler上开发者活跃报告
  - openEuler上maintainer活跃报告
    
- 查询openEuler上sig相关信息
  - openEuler上sig的maintainer
  - openEuler上sig的代码仓
  - openEuler上sig的开发
  - openEuler上sig的issue
  - openEuler上sig的pr
  - openEuler上sig的maintainer参与情况
    
- 生成openEuler上sig相关报告
  - openEuler上sig的maintainer活跃报告
  - openEuler上sig的开发者活跃报告
  - openEuler上sig的issue和pr报告

- 查询openEuler上代码仓相关信息
  - openEuler上代码仓的issue
  - openEuler上代码仓的pr
    
- 生成openEuler上代码仓相关报告
  - openEuler上代码仓的maintainer活跃报告
  - openEuler上代码仓的开发者活跃报告
  - openEuler上代码仓的issue和pr报告

## 使用方法

### 帮助信息

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

### 查询openEuler整体相关信息
待开发

#### openEuler包含哪些SIG

```bash
python openeuler-wiki-bot.py -l
===== Start Init Sig Info... =====
===== Init Sig Info Done =====
===== Start Print Sig List =====
Total sig num:  95
A-Tune
Application
Base-service
Compiler
Computing
DB
Desktop
G11N
GNOME
...
sig-template
user-committee
xfce
===== Print Sig List Done =====
```

### 生成openEuler代码仓整体运营报告

待开发

### 查询openEuler代码仓上sig相关信息

#### 举例：获取sig-ai-bigdata的所有issue和pr

```bash
./openeuler-wiki-bot.py -r -s sig-ai-bigdata
===== Start Init Sig Info... =====
===== Init Sig Info Done =====
===== Start Process Sig Pull Request =====
===== Process Sig Pull Request Done =====
===== Start Process Sig Issue =====
===== Process Sig Issue Done =====
===== Start Generate Report =====
===== Generate Report Done =====
Report file:  sig_info.xlsx
```

### 生成openEuler代码仓上sig相关报告

待开发
