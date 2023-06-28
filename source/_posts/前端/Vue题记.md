---
title: Vue题记
top: false
cover: false
toc: true
mathjax: true
date: 2023-06-28 10:27:44
summary: Vue一些题记
tags: [前端,Vue,render,v-bind在css中使用]
categories: [前端,Vue]
---

## 一、动态颜色 v-bind 在css中使用
```vue
<script setup>
import { ref } from "vue"
const theme = ref("red")

const colors = ["blue", "yellow", "red", "green"]

setInterval(() => {
  theme.value = colors[Math.floor(Math.random() * 4)]
}, 1000)

</script>

<template>
  <p>hello</p>
</template>

<style scoped>
/* Modify the code to bind the dynamic color */
p {
  color:  v-bind(theme)
}
</style>
```

## 二、全局css ：global()
```vue
<template>
  <p>Hello Vue.js</p>
</template>

<style scoped>

p {
  font-size:20px;
  color:red;
  text-align: center;
  line-height: 50px;
}

/* Make it work */
:global(body) {
  width: 100vw;
  height: 100vh;
  background-color: burlywood;
}
</style>
```

## 三、Teleport 将插槽内容渲染到另一个DOM
```vue
<script setup>

const msg = "Hello World"

</script>

<template>
  <!-- Renders it to a child element of the `body` -->
  <Teleport to="body">
    <span >{{ msg }}</span>
  </Teleport>
</template>
```

## 四、render  h 的使用
mybutton.ts
```ts
import { defineComponent, h } from 'vue';
//import { emit } from 'process';

export default defineComponent({
  name: 'MyButton',
  props: {
    disable: {
      default: true,
      type: Boolean,
    },
  },
  render(context) {
    return h(
      /** do someting */
      'button',
      {
        onClick: () => {
          context.$emit('custom-click');
        },
      },
      context.$slots
    );
  },
});
```

App.vue
```Vue
<script setup lang="ts">
import MyButton from "./MyButton"

const onClick = () => {
  console.log("onClick")
}

</script>

<template>
  <MyButton :disabled="false" @custom-click="onClick">
    my button 
  </MyButton>
  <!-- <h2>sdaio</h2> -->
</template>
```

## 五、
