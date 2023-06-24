---
title: webpack
date: 2023-06-02 08:59:41
summary: Webpack五大核心概念、基础、处理各种资源，开发模式、生产模式等
tags: [webpack5,webpack.config.js,webpack生产/开发模式]
categories: [webpack,webpack基础]
---

# Webpack
整理一下webpack的基础知识吧，具体看右侧TOC

## Webpack五大核心概念
1. entry(入口)：指示Webpack从哪个文件开始打包
2. output(输出)：指示Webpack打包完文件输出到哪，如何命名等
3. loader（加载器）Webpack本身只能处理js、json等资源，其他资源需要借助loader,Webpack才能解析
4. plugins(插件) 扩展Webpack功能
5. mode（模式）：开发模式development 和 生产模式production


### 下载依赖
打开终端，来到项目根目录。运行以下指令：

- 初始化package.json
`npm init -y`
此时会生成一个基础的 `package.json` 文件。
需要注意的是 package.json 中 name 字段不能叫做 webpack, 否则下一步会报错

- 下载依赖
`npm i webpack webpack-cli -D`
### 启用 Webpack

- 开发模式
`npx webpack ./src/main.js --mode=development`
- 生产模式
`npx webpack ./src/main.js --mode=production`
`npx webpack`: 是用来运行本地安装 Webpack 包的。
`./src/main.js`: 指定 Webpack 从 main.js 文件开始打包，不但会打包 main.js，还会将其依赖也一起打包进来。
`--mode=xxx`：指定模式（环境）。

位置：会生成在dist目录下

### 准备 Webpack 配置文件
在项目根目录下新建文件：`webpack.config.js`
```javascript
const path = require('path'); //node.js核心模块，处理路径问题

module.exports = {
    // 入口
    entry: "./src/main.js",
    // 输出
    output: {
        path: path.resolve(__dirname,"dist"),
        // 入口文件输出文件名
        filename: "js/main.js",
        clean: true,// 自动将上次打包目录资源清空
    },
    // 加载器
    module: {
        rules: [
            {
                // loader配置
            }
        ]
    },
    // 插件
    plugins:[],
    // 模式
    mode: "development",
}
```
`Webpack` 是基于` Node.js` 运行的，所以采用 `Common.js` 模块化规范
`npx webpack`即可运行

## 处理样式资源
Webpack如何处理Css、Less、Sass、Styl
[webpack官方文档](https://webpack.js.org/loaders/)
```javascript
 // 加载器 webpack.config.js中
    module: {
        rules: [
            {
                // loader配置
                test: /\.css$/, //正则匹配只检测.css文件
                use: [
                    "style-loader", // 将js中css通过创建style标签在html中生效
                    "css-loader", //css资源编译成common.js模块到js中
                ], // 执行顺序 从下到上
            },
            {
               test: /\.less$/ ,
               use: [
                    "style-loader", // 将js中css通过创建style标签在html中生效
                    "css-loader", //css资源编译成common.js模块到js中
                    "less-loader", //将less编译成css
                ], // 执行顺序 从下到上
            }
        ]
    },
```
sass和less配置都类似 看官方下载个loader就行

## 处理图片资源
- Webpack4 时，我们处理图片资源通过 `file-loader` 和 `url-loader` 进行处理
- Webpack5 已经将两个 Loader 功能内置到 Webpack 里了，我们只需要简单配置即可处理图片资源
```javascript 
// webpack.config.js->module->rules中
{
                test: /\.(png|jpe?g|gif|webp)$/,
                type: "asset",
                // 优点：减少请求数量
                // 缺点：体积变得更大
                // 图片资源优化
                parser: { //将小于某个大小的图片转化成 data URI 形式（Base64 格式）
                    dataUrlCondition: {
                      maxSize: 10 * 1024 // 小于10kb的图片会被base64处理
                    }
                },
                generator: {
                    // 输出图片名称
                    // [hash:10]hash值取前面10位
                    filename: "static/images/[hash:10][ext][query]"
                }
},
```

## 处理js资源
Webpack 对 js 处理是有限的，只能编译 js 中 ES 模块化语法，不能编译其他语法，导致 js 不能在 IE 等浏览器运行，需要做一些兼容性处理。
- 针对 js 兼容性处理，我们使用 Babel 来完成
- 针对代码格式，我们使用 Eslint 来完成
### Eslint
可组装的 JavaScript 和 JSX 检查工具。
这句话意思就是：它是用来检测 js 和 jsx 语法的工具，可以配置各项功能
我们使用 Eslint，关键是写 Eslint 配置文件，里面写上各种 rules 规则，将来运行 Eslint 时就会以写的规则对代码进行检查

#### 1、配置文件
配置文件由很多种写法：

>`.eslintrc.*`：新建文件，位于项目根目录
`.eslintrc`
`.eslintrc.js`
`.eslintrc.json`
区别在于配置格式不一样
`package.json` 中 `eslintConfig`：不需要创建文件，在原有文件基础上写
ESLint 会查找和自动读取它们，所以以上配置文件只需要存在一个即可

#### 2、具体配置
`.eslintrc.js`,以下配置
```js
module.exports = {
  // 解析选项
  parserOptions: {
        ecmaVersion: 6, // ES 语法版本
        sourceType: "module", // ES 模块化
        ecmaFeatures: { // ES 其他特性
            jsx: true // 如果是 React 项目，就需要开启 jsx 语法
        }
  },
  // 具体检查规则
  rules: {
        semi: "error", // 禁止使用分号
        'array-callback-return': 'warn', // 强制数组方法的回调函数中有 return 语句，否则警告
        'default-case': [
            'warn', // 要求 switch 语句中有 default 分支，否则警告
            { commentPattern: '^no default$' } // 允许在最后注释 no default, 就不会有警告了
        ],
        eqeqeq: [
            'warn', // 强制使用 === 和 !==，否则警告
            'smart' // https://eslint.bootcss.com/docs/rules/eqeqeq#smart 除了少数情况下不会有警告
        ],
  },
  // 继承其他规则
  extends: [],
  // ...
};
```
- rules中具体规则
>`"off"` 或 `0` - 关闭规则
`"warn"` 或 `1` - 开启规则，使用警告级别的错误：`warn` (不会导致程序退出)
`"error"` 或 `2` - 开启规则，使用错误级别的错误：`error` (当被触发的时候，程序会退出)

- extends 继承
个人感觉还是继承方便，重写rules难受~~
```js
// 例如在React项目中，我们可以这样写配置
module.exports = {
  extends: ["react-app"],
  rules: {
    // 我们的规则会覆盖掉react-app的规则
    // 所以想要修改规则直接改就是了
    eqeqeq: ["warn", "smart"],
  },
};
```

#### 3、在 Webpack 中使用eslint
1. 老规矩，没有的得先下载
`npm i eslint-webpack-plugin eslint -D`
2. 定义 Eslint 配置文件
- `.eslintrc.js`
```js
module.exports = {
  // 继承 Eslint 规则
  extends: ["eslint:recommended"],
  env: {
    node: true, // 启用node中全局变量
    browser: true, // 启用浏览器中全局变量
  },
  parserOptions: {
    ecmaVersion: 6,
    sourceType: "module",
  },
  rules: {
    "no-var": 2, // 不能使用 var 定义变量
  },
};
```
记得要在main.js导入

- `webpack.config.js` 中写入 `ESLintWebpackPlugin`
```js
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "static/js/main.js", // 将 js 文件输出到 static/js 目录中
    clean: true, // 自动将上次打包目录资源清空
  },
  module: {
    rules: [
      {
        // 用来匹配 .css 结尾的文件
        test: /\.css$/,
        // use 数组里面 Loader 执行顺序是从右到左
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.less$/,
        use: ["style-loader", "css-loader", "less-loader"],
      },
      {
        test: /\.s[ac]ss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.styl$/,
        use: ["style-loader", "css-loader", "stylus-loader"],
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: "asset",
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024, // 小于10kb的图片会被base64处理
          },
        },
        generator: {
          // 将图片文件输出到 static/imgs 目录中
          // 将图片文件命名 [hash:8][ext][query]
          // [hash:8]: hash值取8位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: "static/imgs/[hash:8][ext][query]",
        },
      },
      {
        test: /\.(ttf|woff2?)$/,
        type: "asset/resource",
        generator: {
          filename: "static/media/[hash:8][ext][query]",
        },
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "src"),
    }),
  ],
  mode: "development",
};
```

### Babel
主要用于将 ES6 语法编写的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中,像es6->es5

#### 1、配置文件
配置文件由很多种写法：

- `babel.config.*`：新建文件，位于项目根目录
`babel.config.js`
`babel.config.json`
- `.babelrc.*`：新建文件，位于项目根目录
`.babelrc`
`.babelrc.js`
`.babelrc.json`
- `package.json` 中 `babel`：不需要创建文件，在原有文件基础上写
Babel 会查找和自动读取它们，所以以上配置文件只需要存在一个即可

#### 2、具体配置
`babel.config.js`为例子
```js
module.exports = {
    //预设
  presets: ["@babel/preset-env"],
};
```
presets 预设
简单理解：就是一组 Babel 插件, 扩展 Babel 功能

- `@babel/preset-env`: 一个智能预设，允许使用最新的 JavaScript。
- `@babel/preset-react`：一个用来编译 React jsx 语法的预设
- `@babel/preset-typescript`：一个用来编译 TypeScript 语法的预设

#### 3、在 Webpack 中使用
1. 先下载
`npm i babel-loader @babel/core @babel/preset-env -D`
2. 定义 Babel 配置文件,如上代码块
`webpack.config.js`
```js
//在module->rules数组里面加上
      {
        test: /\.js$/,
        exclude: /node_modules/, // 排除node_modules代码不编译
        loader: "babel-loader",
      },
```
3. npx webpack 打包
打开打包后的 `dist/static/js/main.js` 文件查看，会发现箭头函数等 ES6 语法已经转换了

## 处理 Html 资源
1. 下载包
`npm i html-webpack-plugin -D`
2. 配置`webpack.config.js`
```js
// 加上
const HtmlWebpackPlugin = require("html-webpack-plugin");
//plugins数组中加入
 new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "public/index.html"),
    }),
```
3. 修改 public中的index.html
去掉引入的 js 文件，因为 HtmlWebpackPlugin 会自动引入
4. 运行`npx webpack`
此时 dist 目录就会输出一个 index.html 文件

## 开发服务器&自动化
自动编译代码，无需手动输入指令
1. 下载`npm i webpack-dev-server -D`
2. 配置`webpack.config.js`
```js
// plugins中
// 开发服务器
  devServer: {
    host: "localhost", // 启动服务器域名
    port: "3000", // 启动服务器端口号
    open: true, // 是否自动打开浏览器
  },
```
3. `npx webpack serve`

## 生产模式
生产模式是开发完成代码后，我们需要得到代码将来部署上线。
上线肯定就要性能好，性能好就要优化
优化主要从两个角度出发:
1. 优化代码运行性能
2. 优化代码打包速度

### 文件目录
这个有篇文章vue项目总结里面有项目实例...
```
├── webpack-test (项目根目录)
    ├── config (Webpack配置文件目录)
    │    ├── webpack.dev.js(开发模式配置文件)
    │    └── webpack.prod.js(生产模式配置文件)
    ├── node_modules (下载包存放目录)
    ├── src (项目源码目录，除了html其他都在src里面)
    │    └── 略
    ├── public (项目html文件)
    │    └── index.html
    ├── .eslintrc.js(Eslint配置文件)
    ├── babel.config.js(Babel配置文件)
    └── package.json (包的依赖管理配置文件)
```

### 修改 webpack.dev.js
rules 我清楚了 看着方便，主要改动 目录变化 路径退回上一层
运行开发模式指令
`npx webpack serve --config ./config/webpack.dev.js`

```js
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: undefined, // 开发模式没有输出，不需要指定输出目录
    filename: "static/js/main.js", // 将 js 文件输出到 static/js 目录中
    // clean: true, // 开发模式没有输出，不需要清空输出结果
  },
  module: {
    rules: [
    ]
  },
  plugins: [
    new ESLintWebpackPlugin({
      // 指定检查文件的根目录
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      // 以 public/index.html 为模板创建文件
      // 新的html文件有两个特点：1. 内容和源文件一致 2. 自动引入打包生成的js等资源
      template: path.resolve(__dirname, "../public/index.html"),
    }),
  ],
  mode: "development",
};
```
### 修改 webpack.prod.js
可以 对比以下开发模式的配置
运行上线模式的指令：
`npx webpack --config ./config/webpack.prod.js`

```js
const path = require("path");
const ESLintWebpackPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  output: {
    path: path.resolve(__dirname, "../dist"), // 生产模式需要输出
    filename: "static/js/main.js", // 将 js 文件输出到 static/js 目录中
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  plugins: [
    new ESLintWebpackPlugin({
      context: path.resolve(__dirname, "../src"),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "../public/index.html"),
    }),
  ],
  mode: "production",
};
```

### 配置运行指令
开发vue项目时候都习惯了npm ...的脚本命令
像直接`npm run build`打包
为了方便运行不同模式的指令，我们将指令定义在 package.json 中 scripts 里面
```json
// package.json
{
  // 其他省略
  "scripts": {
    "start": "npm run dev",
    "dev": "npx webpack serve --config ./config/webpack.dev.js",
    "build": "npx webpack --config ./config/webpack.prod.js"
  }
}
```

---
[webpack项目配置及一些高级知识](https://yk2012.github.io/sgg_webpack5/project/)
