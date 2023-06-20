---
title: java小记
date: 2023-06-06 15:52:22
summary: java第二篇
tags: [java小记,增强for,collection,iterator遍历,单例设计模式,抽象类,接口]
categories: [Java,Java第二篇]
---

## 一、java中s.length() 和 s.length区别
- s.length是针对java中数组的，length是数组的一个属性，用来表示数组的长度
- s.length()则是字符串的一个方法，用来返回字符串的长度的

## 二、代码块
代码块的顺序优先于构造器，多个类构造器相同代码可提入代码块
```java
[修饰符]{

}// 如果加了static只会执行一次
```
细节
>1. static代码块——静态代码块，随着类加载只会执行一次
2. 类什么时候被加载【重要】
1）创建对象实例时候（new）
2）创建子类对象实例，父类也会被加载
3）使用类的静态成员时候（静态属性，静态方法）
```JAVA
public class CodeStatic {
    public static void main(String[] args) {
      //  BB bb = new BB();  (1)
        System.out.println(AA.n1);// (2)
    }
}
class AA{
    public static int n1=9;
    static{
        System.out.println("AAAAAAAAA代码块");
    }
}
class BB extends AA{
    static {
        System.out.println("BBBBBBB代码块");
    }
}

//(1) 输出顺序
//AAAAAAAAA代码块
//BBBBBBB代码块
//(2) 输出顺序
//AAAAAAAAA代码块
//9
```
>4）创建一个对象时，在一个类调用顺序是：【重点，难点】
>>1、调用静态代码块和静态属性初始化
2、调用普通代码块和普通属性的初始化
3、调用构造方法

>5）构造器 的最前面其实因隐藏了super() 和调用普通代码块

## 三、单例设计模式
1. 采用一定的方法，在整个软件系统中，对某个类只能存在一个对象实例，并且该类只提供一个去的对象实例的方法
2. 两种模式 1）饿汉式 2）懒汉式
二者主要区别在于创建对象**时机不同**，懒汉式存在线程安全问题，饿汉式存在浪费资源的可能
步骤如下：
>1）构造器私有化，防止直接new
2）类的内部创建对象
3）向外暴漏一个静态的公共方法
4）代码实现
```java
//饿汉
public class Single {
    public static void main(String[] args) {
        GirlFriend instance1 = GirlFriend.getInstance();
        GirlFriend instance2 = GirlFriend.getInstance();
        System.out.println(instance2 == instance1);//true
    }
}
class GirlFriend{
    private String name;
    // 保障只创建一个 GirlFriend 对象
    private static GirlFriend gf = new GirlFriend("小红");
    private GirlFriend(String name){
        this.name=name;
    }
    public static GirlFriend getInstance(){
        return gf;
    }
}
```
```java
//懒汉
public class Single2 {
    public static void main(String[] args) {
        Cat cat = Cat.getInstance();
    }
}
class Cat{
    private String name;
    private static Cat cat;
    private Cat(String name){
        this.name=name;
    }
    public static Cat getInstance(){
        if(cat == null){
            cat = new Cat("喵喵");
        }
        return cat;
    }
}
```

## 四、final关键字
使用情况：
1. 不希望类被继承时
2. 不希望父类的某个方法被子类覆盖/重写时候，但该方法可继承
3. 不希望类中某个属性值被修改
4. 不希望某个局部变量被修改
- final修饰的属性一般叫常量 `final double a = 0;`定义时候必须初始化

## 五、抽象类 Abstract
当父类的某些方法需要声明，但又不能确定如何实现时候，可以将其声明为抽象方法，那么这个类就是抽象类
1. 抽象类不能被实例化
2. 抽象类不一定要含有abstract方法
3. 一旦保安了abstract方法，这个类必须声明为abstract
4. abstract只能修饰类和方法，不能修饰属性和其他的
5. 抽象类可以拥有任意成员
6. 抽象方法不能有主体 `abstract void aa{}`,即{}不应存在
7. 如果一个类继承了抽象类，则必须实现抽象类的所有抽象方法

## 六、接口 interface
- 一个类可以实现多个接口
- 一个接口可以继承多个接口

## 七、类的五大成员
[属性、方法、构造器、代码块、内部类]
内部类还分为局部内部类（通常在方法中）、匿名内部类（无类名）
- 局部内部类：作用域在方法或者代码块中、不能添加访问修饰符、但是可以使用final
外部其他类不能访问局部内部类，如果外部类和局部内部类的成员重名时候，遵循就近原则，
如果想访问外部类成员可以用（外部类名.this.成员）
- （Anonymous匿名的）匿名内部类：同时还是一个对象，系统jdk会分配个名字
```java
IA tiger = new IA(){
    @Override
    public void cry(){
        System.out.println("老虎叫---")；
    }
}
tiger.cry();
```

## 八、java反编译
hello.java ——> hello.class   (javac编译)
hello.java <—— hello.class   (javap反编译)

## 九、enum 枚举类型
可以这么写   实际上用 java.lang.enum
```java
enum classname{
    SPRING("春天","复苏"),what;// what调用无参构造器，也可以写what();
    public static final String name;
    public static final String desc;
    // 构造器 省略不写了就
}
```

## 十、注解 Annotation
### 注解概念及应用
1. 注解被称为元数据，用于修饰解释包、类、方法、属性、构造器、局部变量等数据
2. 和注释一样，注解不影响程序逻辑，但可以被编译或者运行，相当于嵌入在代码中的补充信息
3. 在javaSE中，注解的使用简单，如 标记过时的功能、忽略警告等
4. 在javaEE中，注解的更重要，如 【配置应用程序的任何切面，代替java EE旧版中所遗留的繁冗代码和XML配置等。】

### 三个基本注解
1. @Override ：限定某个方法，是重写父类方法，该注解只能用于方法
如果写了@Override 编译器会检查该方法是否真的重写了，没重写会报错！
2. @Deprecated: 用于表示某个程序元素（类，方法）已经过时
并不是不能用
3. @SuppressWarnings: 抑制编译器警告 （suppress-抑制）
@SuppressWarnings({""})  -all所有，null 等等

@interface 不是interface 是个注解类

### 元注解
修饰注解的注解
1. Retention 指注解的作用范围
2. Target 指定注解可以在哪些地方使用
3. Documented 指定该注解是否会在Javadoc体现
4. Inherited 子类会继承父类注解

## 十一、java常用类
1. 包装类
2. String
3. StringBuffer
4. StringBuildr
5. Math
6. Date、Calendar、LocalDate。。
7. System
8. Arrays
9. BigInteger BigDecimal

### 八大wrapper类
boolean Boolean
char    Character
byte    Byte
short   Short
int     Integer
long    Long
float   Float
double  Double

### 拆箱装箱
其他包装类与此类似
```java
public class Wrapper {
    public static void main(String[] args) {
        int n=1;
        //手动装箱 int -> integer
        Integer integer = Integer.valueOf(n);
        Integer integer1 = new Integer(n);
        System.out.println(integer);
        //手动拆箱 integer -> int
        int i = integer.intValue();

        //jdk5以后可以自动装箱和拆箱
        //自动装箱 int -> integer
        Integer integer2 = n; //底层用的Integer.valueOf()
        //自动拆箱
        int n2 = integer2;//底层用的 integer.intValue()
    }
}
```

### 面试题
![](./java%E5%B0%8F%E8%AE%B0/integer.png)

## 十二、String 和 StringBuffer 和 StringBuilder
1. String 保存的是字符串常量，每次更改会改变地址
2. StringBuffer 保存的是字符串变量，每次更改到空间不够的时候会新增空间，之后改变地址
字符串缓冲区，初始为16个字符
StringBuffer里边有char[] value,不是每次都创建新对象

### StringBuffer常用方法
1. 增 append
2. 删 delete（start，end）
3. 改 replace（start，end，string）
4. 查 indexOf 找到第一次的索引，找不到的话返回-1
5. 插 insert
6. 获取长度 length
7. stringbuffer转string  toString()方法

### price转换案例
```java
public class StringBufferP {
    public static void main(String[] args) {
        String price="2123124773.50";
        StringBuffer strBuff = new StringBuffer(price);
        int len = strBuff.lastIndexOf(".");
        for(int i=len-3;i>0;i=i-3){
            strBuff.insert(i,",");
        }
        System.out.println(strBuff);//2,123,124,773.50
    }
}
```

### StringBuilder
1. StringBuilder继承了AbstractStringBuilder
2. 实现了 `Serializable`，说明StringBuilder对象可串行化
3. StringBuilder 是`final`类 不能被继承
4. StringBuilder 对象字符序列仍然存放在其父类的 AbstractStringBulider的 `char[] value`中
5. StringBuilder 的方法没有synchronized，无互斥处理

### 三者区别
![](./java%E5%B0%8F%E8%AE%B0/String.jpg)

## 十三、Arrays
里面包含一些静态方法，用于管理或操作数组
1. toString 返回数组字符串形式
2. sort 排序
3. binarySearch 二分法查找（必须要求排好序）
eg：`int index = Arrays.binarySearch(arr,3);`
4. copyOf 数组元素的复制
`Integer[] newArr = Arrays.copyOf(arr,arr.length);`
5. fill 数组填充
6. equals 比较两个数组元素内容是否完全一致
7. asList 将一组值转化为list

## 十四、System类
1. exit 退出当前程序
2. arraycopy 复制数据元素
3. currentTimeMillens 返回当前时间距离1970-1-1的毫秒数
4. gc 运行垃圾回收机制 System.gc();

## 十五、BigInteger和BigDecimal类
1. BigInteger 适合保存比较大的整型
2. BigDecimal 适合保存浮点数

## 十六、Date类 Calendar类

## 十七、Collection接口
collection继承了Iterable接口
![](./java%E5%B0%8F%E8%AE%B0/collection.png)

### iterator迭代器
获取collection的iterator遍历
```java
public class Itera {
    public static void main(String[] args) {
        Collection col = new ArrayList();
        col.add("三国");
        col.add("演绎");
      //  System.out.println(col);
        Iterator iterator = col.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }
}
```
```java
// 快捷键打出 itit
    while (iterator.hasNext()) {
            Object next =  iterator.next();
            
        }
```

### 增强for遍历collection
```java
public class CollectionFor {
    public static void main(String[] args) {
        Collection col = new ArrayList();
        col.add("三国");
        col.add("水浒");
        for(Object book : col){
            System.out.println(book);
        }
    }
}
```





