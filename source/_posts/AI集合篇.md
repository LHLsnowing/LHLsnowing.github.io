---
title: AI集合篇
date: 2023-06-02 23:53:52
tags: [chatgpt,ai工具,插件,git push失败原因及解决]
categories: AI
---

# AI
![](./AI%E9%9B%86%E5%90%88%E7%AF%87/ad.jpg)
把我知道的一些国内镜像站做个集合,自己想搭GitHub也有开源,会用ai会有不少便利和乐趣
1. [npm 镜像——freegpt](https://www.npmmirror.com/package/freegpt)
2. [AI工具集合，这个工具很多](https://ai-bot.cn/)
3. [需要梯子，有gpt4和3.5](https://chat.forefront.ai/)
4. [花钱，gpt4，可试用](https://poe.com/GPT-4)
5. [还可以，积分制](https://ai.usesless.com/)
6. [coplit平体](https://codeium.com/playground)

## 好用的vs插件
1. Error Lens ， 在后面事实显示错误

## 浏览器内搜索
ctrl+f

##  git push失败原因
开启梯子（VPN）是为了解决网络访问被封锁或限制的问题，但是对于git push失败可能有以下几个常见原因：

1. 梯子连接不稳定：有些梯子连接质量并不稳定，导致在推送操作时出现意外中断或延迟。
2. 仓库地址错误：如果使用了错误的仓库地址，那么即使使用梯子也无法推送成功。
3. SSH配置错误：如果使用SSH协议进行push操作，在梯子环境下需要将SSH协议的代理设置正确。可以通过在本地`.ssh/config`文件中增加如下内容进行设置：
```
Host *
   ProxyCommand /usr/local/bin/connect-proxy -H 127.0.0.1:1080 %h %p
```
4. Git协议：默认情况下Git使用的是Git协议（git://），而这种协议默认使用端口9418，在一些网络环境下该端口被屏蔽，所以需要切换到HTTPS协议推送。

