---
title: 各种小资源，网站备份，报错等笔记
date: 2023-06-02 23:53:52
summary: 一些资源链接，报错记录，前后端文档及学习路线等等
tags: [chatgpt,ai工具,插件,git push失败原因及解决,cs自学,证件照,文档]
categories: 资源整合
---

services.msc 打开计算机的服务
# 一些资源链接，报错记录，文档等等
![](./AI%E9%9B%86%E5%90%88%E7%AF%87/ad.jpg)
## 一、国内 ai镜像，梯子，插件等
1. [npm 镜像——freegpt](https://www.npmmirror.com/package/freegpt)
2. [AI工具集合，这个工具很多](https://ai-bot.cn/)
3. [需要梯子，有gpt4和3.5](https://chat.forefront.ai/)
4. [花钱，gpt4，可试用](https://poe.com/GPT-4)
5. [还可以，积分制](https://ai.usesless.com/)
6. [coplit平体](https://codeium.com/playground)
7. [3.5and4,好用](https://ai.kunshanyuxin.com/)
### 便宜的梯子订阅
[存个网址先，https://feiniaoyun.top/#/dashboard](https://feiniaoyun.top/#/dashboard)

### 好用的vs插件
1. Error Lens ， 在后面事实显示错误
2. [Codeium,ai代码插件，类似copilot](https://codeium.com/playground)

---
##  二、git push失败原因
开启梯子（VPN）是为了解决网络访问被封锁或限制的问题，但是对于git push失败可能有以下几个常见原因：

1. 梯子连接不稳定：有些梯子连接质量并不稳定，导致在推送操作时出现意外中断或延迟。
2. 仓库地址错误：如果使用了错误的仓库地址，那么即使使用梯子也无法推送成功。
3. SSH配置错误：如果使用SSH协议进行push操作，在梯子环境下需要将SSH协议的代理设置正确。可以通过在本地`.ssh/config`文件中增加如下内容进行设置：
```
Host *
   ProxyCommand /usr/local/bin/connect-proxy -H 127.0.0.1:1080 %h %p
```
4. Git协议：默认情况下Git使用的是Git协议（git://），而这种协议默认使用端口9418，在一些网络环境下该端口被屏蔽，所以需要切换到HTTPS协议推送。

## 三、blog文章太多 分类创建命令
`hexo new post -p /后端/test.md`

---
## 四、免费壁纸下载推荐 及 免费软件
1. Unsplash（https://unsplash.com/）- 提供高质量的免费照片和壁纸，每日更新。
2. Pexels（https://www.pexels.com/）- 提供高质量的免费照片和壁纸，覆盖各种主题和风格。
3. Pixabay（https://pixabay.com/）- 提供免费的高清图片和壁纸，包括照片、插图和矢量图。
4. Wallpaper Abyss（https://wall.alphacoders.com/）- 提供大量高清壁纸，包括电影、游戏、动漫等各种分类。
5. WallpaperCave（https://wallpapercave.com/）- 提供各种类型的高清壁纸，包括自然风景、艺术、抽象等。
6. https://hdqwalls.com/wallpaper/3840x2160/hogwarts-legacy-8k

- https://www.fuzhugou.com/  免费软件——大神推荐的
---

## 五、CS自学指南
[https://csdiy.wiki/](https://csdiy.wiki/)

## 六、一些转换工具，简历模板，证件照制作等等

### 1.浏览器内搜索，pdf等各种转换
ctrl+f
![浏览器插件，搜图中名字就ok](./AI%E9%9B%86%E5%90%88%E7%AF%87/image.png)
### 2.简历模板 ，制作证件照,换底色
[简历模板，可直接导出:https://www.resumeis.com/edit?id=62bdbfbf9d1c7150ff3ae5f2](https://www.resumeis.com/edit?id=62bdbfbf9d1c7150ff3ae5f2)
[制作证件照,换底色：https://id-photo.cn/](https://id-photo.cn/)
### 3.娱乐游戏 单机等网址
[游侠网：https://www.ali213.net/](https://www.ali213.net/)
[3DM:https://www.3dmgame.com/](https://www.3dmgame.com/)
### 4.程序员开发工具
[格式转换](https://tooltt.com/)

---
## 七、前端相关文档
1. [Vue官方文档](https://cn.vuejs.org/guide/introduction)
2. [TS书籍文档，非官方](http://ts.xcatliu.com/)
3. [MDN_js](https://developer.mozilla.org/zh-CN/)
4. [animate_css动画库](https://animate.style/)
5. [React文档](https://zh-hans.react.dev/)
6. [CDN](https://www.bootcdn.cn/)
7. [Vue-Router](https://router.vuejs.org/zh/guide/)
8. [Pinia](https://pinia.vuejs.org/zh/api/)
9. [Webpack](https://webpack.js.org/)
10. [Vite](https://vitejs.dev/)
11. [iconfont](https://www.iconfont.cn/)
12. [Vue.js在线挑战通关](https://cn-vuejs-challenges.netlify.app/)
13. [uni-app](https://uniapp.dcloud.net.cn/)
14. [react基础-router-Mobx-redux-zustand 文档博客](https://www.yuque.com/fechaichai/qeamqf/xbai87)

### 在线颜色习惯，获取16进制
[https://photokit.com/colors/eyedropper/?lang=zh](https://photokit.com/colors/eyedropper/?lang=zh)

---
## 八、Linux
1. [鸟哥的私房菜——书](https://wizardforcel.gitbooks.io/vbird-linux-basic-4e/content/index.html)
2. [The Linux Kernel Archives](https://www.kernel.org/)
---
## 九、HarmonyOS Developer
[https://developer.harmonyos.com/](https://developer.harmonyos.com/)

---
## 十、申请证书 ssl tls
https://letsencrypt.org/zh-cn/
[freessl:https://freessl.org/](https://freessl.org/)
[cloudflare:https://www.cloudflare.com/zh-cn/](https://www.cloudflare.com/zh-cn/)
---
## 十一、zpxx_nefu
https://ipb8bic1pz.feishu.cn/docx/UE3QdRaVEozJ9cxTFjFcA5Jcnvd
## 十二、实习老师的笔记
[内容挺全的：https://jshand.gitee.io/#/README](https://jshand.gitee.io/#/README)

---
## 十三、后端JAVA
https://www.bilibili.com/read/cv5216534
![java学习路线](./AI%E9%9B%86%E5%90%88%E7%AF%87/Java_learn.png)

[java全栈知识体系：https://pdai.tech/md/resource/tools.html](https://pdai.tech/md/resource/tools.html)


---
- 涤尘 https://zhutix.com/
- FireWin  https://github.com/FWGritTop/node_frontback_2307/tree/main/%E7%AC%94%E8%AE%B02
