---
title: Vue后台管理系统项目总结
date: 2023-05-24 13:19:58
tags:  [前端,Vue,项目]
categories: [前端,Vue,项目]
---

2023-5-20
# Vue后台项目总结
1. token、路由导航守卫、劫持request添加authorization
2. 组件分类及命名，eslint检测，熟悉配置文件
3. 接口请求、跨域、301永久重定向，不允许更换请求（出现服务器请求服务器状况）、前端请求代理、熟悉后端部分
4. 熟悉element-ui，cascader 部分有个动态属性类，用它改变样式，之前还有bug
5. 全局css、按需引入等
6. 性能优化：vue ui使用
   >1） babel.config.js 配置插件 发布时不带console
   2） vue.config.js 自定义配置webpack
   3） externals 加载外部CDN资源 直接房dist里 index.js cdn引入
   4） gzip压缩等
7. 配置https SSL证书  [https://freessl.org](https://freessl.org),    pm2管理
8. git流程

## 缺点
1. 面包屑部分没封装， axios暴漏


---
[这个用的Gitee，在这里！https://gitee.com/lhlsnowing/vue_shop_project](https://gitee.com/lhlsnowing/vue_shop_project)

