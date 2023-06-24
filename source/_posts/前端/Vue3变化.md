---
title: Vue3变化
top: true
date: 2023-06-11 16:47:17
summary: vue2->vue3的一些变化,axios全局配置等等
tags: [Vue3变化,axios全局配置]
categories: [Vue,Vue3变化,axios全局配置]
---

## Vue3变化

1. 用一元素上使用的`v-if`和`v-for`优先级已经更改，但**不推荐**同时使用二者
2. 组件事件需要在`emits`选项中声明
3. `destoryed` 生命周期选项被命名为 `unmounted`
4. `beforeDestory` 生命周期选项被命名为 `beforeUnmount`
5. 自定义指令API已更改为与组件生命周期一致
6. 新增三个组件：`Fragment` 支持多个根节点、`Suspense`可以在组件渲染之前的等待时间显示指定内容、`Teleport`可以让子组件能够在视觉上跳出父组件（如父组件overflow：hidden）
7. 新增指令`v-memo`，可以缓存html模板，比如`v-for`遍历的列表不会变化就会缓存，（内存换时间）
8. 用`proxy`代替`Object.defineProperty`重构响应式系统，可以监听到数组下标变化，及对象新增属性，因为监听的不是对象属性，而是对象本身，还可以拦截`apply`，`has`等13种方法
9. 重构了虚拟DOM，在编译时会将事件缓存、将`slot`编译为`lazy`函数、保存静态节点直接复用（静态提升）、以及添加静态标记、`Diff`算法使用 最长递增子序列，优化了对比流程，使得虚拟DOM生成速度提升200%
10. 支持在<style></style>里使用v-bind，给css绑定js变量（color：v-bind（str））
11. 新增`Composition API` 可以更好的逻辑复用和代码组织，同一功能代码聚集在一起，尽管Vue2种使用了`mixin`实现代码复用，也会存在一些问题，如方法或者属性名冲突，代码来源也不清楚
12. 全局函数`set`和`delete`以及实例方法`$set`和`$delete`移除，基于代理的变化检测已经不再需要他们了
13. Vue3用TS写的，所以对TS的支持度更好
14. Vue3不兼容IE11
15. $on $off $once 实例方法已被移除

---
setup（）最先执行

---
## vue axios全局配置
- 在实际项目开发中，几乎每个组件中都会用到 axios 发起数据请求。此时会遇到如下两个问题：
1. 每个组件中都需要导入 axios
2. 每次发请求都需要填写完整的请求路径
- 可以通过全局配置的方式解决上述问题：
```js
//请求根路径
axios.defaults.baseURL =  'http://api.com'
// 将axios作为全局的自定义属性，每个组件内部可以直接访问 （vue3）
app.config.globalProperties.$http = axios
// 将axios作为全局的自定义属性，每个组件内部可以直接访问 （vue2）
Vue.prototype.$http = axios
```