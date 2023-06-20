---
title: 重新学Java
date: 2023-05-30 16:16:46
summary: java第一篇
tags: [Java,迷宫问题,IDEA快捷键]
categories: [Java,java第一篇]
---

# Java基础

## 一、java重要特点
1. oop
2. Java语言健壮性，强类型机制、异常处理、垃圾的自动回收
3. 跨平台
4. 解释性的   还有JavaScript，php  （编译性语言c、c++编译后直接执行）

## 二、JDK JRE JVM关系
1. JDK = JRE + 开发工具集
2. JRE = JVM + Java SE标准类库
3. JDK = JVM + Java SE标准类库 + 开发工具集

## 三、java文档
![](./%E9%87%8D%E6%96%B0%E5%AD%A6Java/first.png)
[java在线api](https://www.matools.com/api/java8)

## 四、java字符类型本质
字符型 
存储: 'a'==>码值97==>二进制（110 0001）==> 存储
读取: 二进制==>码值==>'a'

## 五、基本数据类型转换
1. 有多种类型的数据混合运算时，系统自动转成容量最大的数据类型再计算
2. 把精度大的数据赋值给精度小的数据类型时，会报错，反之自动转换类型
3. （byte，short）和char之间不会自动转换，他们三者可以计算，计算时候转成int类型
4. Boolean 不参与转换
6. 自动提升，表达式结果类型自动提升为操作数中最大的类型

## 六、java递归迷宫问题

```java
package new_java;

public class MiGong {
	// 迷宫问题
	// 建立迷宫 二维数组 规定map数组0可走1障碍物
	public static void main(String args[]) {
		int[][] map = new int[8][7];
		for (int i = 0; i < 7; i++) {
			map[0][i] = 1;
			map[7][i] = 1;
		}
		for (int i = 0; i < 8; i++) {
			map[i][0] = 1;
			map[i][6] = 1;
		}
		// 设计迷宫四周的墙
		map[3][1] = 1;
		map[3][2] = 1;
		map[3][3] = 1;
		map[2][3] = 1;
		map[2][1] = 1;
//		map[3][1] = 1;
//		map[3][2] = 1;

		// 当前地图输出
		System.out.println("===当前地图情况===");
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}

		// 开始找路(i,j)初始位置
		T t1 = new T();
		t1.findWay(map, 1, 1);
		System.out.println("===找完看===");
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
	}
}

class T {
	// 递归思想解决老鼠出迷宫问题
	// 1.findWay 找迷宫路径 找到返回true 否则false
	// 2.map迷宫，i,j初始位置
	// 3. 0可以走 1障碍物 2可以走 3表示走过
	// 4. map[6][5]=2表示找到通路可以结束，否则继续找
	// 5.老鼠找路策略 下->右->上->左
	public boolean findWay(int[][] map, int i, int j) {
		// System.out.println(i);
		if (map[6][5] == 2) {// 找到了
			return true;
		} else {
			if (map[i][j] == 0) {
				map[i][j] = 2;
				if (findWay(map, i + 1, j)) { // 下
					return true;
				} else if (findWay(map, i, j + 1)) {// 右
					return true;
				} else if (findWay(map, i - 1, j)) {// 上
					return true;
				} else if (findWay(map, i, j - 1)) {// 左
					return true;
				} else {
					map[i][j] = 3;
					return false;
				}
			} else {
				return false;
			}
		}
	}
}
```

## 七、方法重载（OverLoad）
**同一个类中，多个同名方法，参数不同**
```java
class MyCalculator {
	public int cal(int n1, int n2) {
		return n1 + n2;
	}

	public double cal(int n1, double n2) {
		return n1 + n2;
	}

	public int cal(int n1, int n2, int n3) {
		return n1 + n2 + n3;
	}
}
```

## 八、可变参数
**可变参数使用**
有点类似传个数组，实参可以是0个活任意多个，也可以是数组
如果里边有普通参数和可变参数，可变参数必须放在最后 eg:`(int i, int... nums)`
```java
public class OverLoad {
	public static void main(String[] args) {
		MyCalculator mc = new MyCalculator();
		System.out.println(mc.sum(1, 2, 3));
	}
}
class MyCalculator {
	// 可变参数
	public int sum(int... nums) {
		int num = 0;
		System.out.println("接收参数个数：" + nums.length);
		for (int i = 0; i < nums.length; i++) {
			num += nums[i];
		}
		return num;
	}
}
```

## 九、对象创建流程分析  ※
```java
class Person{
    int age=90;
    String name;
    Person(String n,int a){//构造函数、构造器
        name=n;
        age=a;
    }
}
Person p = new Person('小明',20);
```
**流程分析（面试题）**
1. 加载Person类信息,只会加载一次
2. 在堆中分配空间(地址)
3. 完成对象初始化 
3.1 默认初始化 age=0,name=null
3.2 显示初始化 age=90,name=null
3.3 构造器初始化 age=20,name=90

## 十、IDEA的使用

### IDEA快捷键
每个人使用习惯不一样，可自己更改设置，以下也非默认
- Ctrl+d 删除一行 （可以自己设置的，setting-》keymap中）
- Ctrl+Alt+向下箭头 复制当前行
- Alt+/ 不全代码 方便
- Ctrl+/ 注释

- Alt+enter 自动导入 需要先设置 setting->genergl->auto import
- Alt+R 自动运行项目
- Ctrl+Alt+L 格式化代码
- Alt+insert 生成构造器，加快开发效率（部分笔记本需要＋fn，关闭即可）
- Ctrl+H 查看类的继承关系
- Ctrl+B 和Ctrl+鼠标左键 一样定位方法

- var 自动分配变量名   `new Scanner(System.in).var` -> `Scanner scanner = new Scanner(System.in);`

### IDEA模板代码
setting -> Live Templates 自行设置更改

## 十一、包命名
命名规则：**只能包含数字、字母、下划线、小圆点，**不能是数字开头，不能是关键字或者保留字
```java
demo.class.exec1 //不行class关键字
demo.12a //12数字开头不行
demo.ab12.aa // 对

//___________________正常
com.公司名.项目名.业务模块名
//例如
com.lhledu.oa.model;
```
常用的个包
```java
java.lang.*  //lang包基本包，默认引入
java.util.* //util系统提供的工具包，工具类 scanner
java.net.* //网络包，网络开发
java.awt.* //做java的开发界面，GUI
```

## 十二、super关键字
主要访问父类的东西,不能访问private修饰的
super.熟悉  super.方法
访问父类构造器 super（参数列表），**只能放在第一句**

## 十三、方法重写
- 方法覆盖（重写）就是子类有一个方法，和父类某个方法的名称、返回类型、参数一样
且访问权限子类不能小于父类

## 十四、多态
- 重写和重载都是多态的一种体现
- 方法多态 （没啥好说的了 简单例子sum（1，2），sum(1,2,3)
- 对象多态：
>1）一个对象的编译类型和运行类型可以不一致
2）编译类型在定义对象时，就可以确定了，不能改变
3）运行类型是可以变化的
4）编译类型看定义时 =号 的左边， 运行类型看 =号 右边
```java
// 例如 Animal 是 Dog 和 Cat的父类
Animal animal = new Dog(); //animal编译类型 是Animal，运行类型是Dog
animal.cry(); // 小狗汪汪叫
animal = new Cat();
animal.cry(); // 小猫喵喵喵
```

### 向上转型和向下转型
向下：
- 子类类型  引用名 = （子类类型） **父类引用**
- 只能强转父类的引用，不能强转父类对象
- 要求父类的引用必须指向的是当前目标类型的对象
- 向下转型后，可以调用子类对象中所有的成员
```java
Cat cat =(Cat) animal; //编译类型是Cat 运行类型 Cat
cat.catchMouse();
// 如果再写 Dog dog = (Dog) animal; 报错，可以按照以下理解
// 有两个 cat 和 animal 都指向一个内存  如果再将animal转换成dog 会出现猫是狗的错误
```

## 十五、属性重写问题
属性没有重写的说法，属性的值看编译类型
```java
public class Main {
    public static void main(String[] args) {
        Base base= new Sub();
        System.out.println(base.count);
    }
}
class Base {
    int count = 10;
}
class Sub extends  Base{
    int count = 20;
}
```	

## 十六、instanceof 可以判断运行类型
instanceof是Java中的二元运算符，左边是对象，右边是类；当对象是右边类或子类所创建对象时，返回true；否则，返回false。
- 左边的对象实例不能是基础数据类型
- 左边的对象实例和右边的类不在同一个继承树上
- null用instanceof跟任何类型比较时都是false
eg： `aa instanceof AA`

## 十七、多态数组  ——  instanceof 配合向下转型
```java
//Person父类， Student，Teacher子类 下面是巧妙运用
Person persons[] = new Person[3];
persons[0]= new Person("jack",20);
persons[1]= new Student("smith",28,20);
persons[2]= new Teacher("king",50,2500);
for(int i=0;i<person.length;i++){
	System.out.println(person[i].say());
	// 正常person[i].study(); 输出不了
	if(person[i] instanceof Student){ //判断运行类型
		Student student = (Student)person[i]; //向下转型
		student.study();
	} else if(person[i] instanceof Teacher){
		Teacher teacher = (Teacher)person[i];
		teacher.teach();
	}else{
		System.out.println("类型有误")
	}
}
```

## 十八、属性看编译时类型，方法看运行时类型
多态挺有意思的  看=左右侧具体判断吧

## 十九、动态绑定机制_重要
![](./%E9%87%8D%E6%96%B0%E5%AD%A6Java/duotai.jpg)
主要看运行类型
找不到方法时候向父级找
js原型链能搞懂这个也能

## 二十、hashCode
1. 提高哈希结构容器效率
2. 两个引用，如果指向同一个对象，hash值一样
3. 两个引用，如果指向的是不同对象，hash值不一样
4. hash值主要根据地址号来的，不能完全等价于地址

## 二十一、finalize 垃圾回收机制
1. 当对象被回收时，系统自动调用该对象的finalize方法，子类可以重写该方法，做释放资源的操作
2. 什么时候被回收，当某个对象没有任何引用时，则JVM认为这个对象是一个垃圾对象，就会使用垃圾回收机制来销毁该对象，在销毁对象前，先调用finalize方法
3. 垃圾回收机制的调用，由系统来决定，也可以通过System.gc()主动触发回收机制
```java
Car bmw = new Car("宝马");
bmw = null; // 这时 car对象是一个垃圾
``` 

## 二十二、断点调试 必备技能
- 断点调试过程中，是运行状态，是以对象的 运行类型 执行的

介绍：
1. 断点调试是指在程序的某一行设置一个断点，调试时，程序运行到这一行会停住，然后你可以一步一步往下调试，调试过程中可以看各个变量当前的值，出错的话，调试到出错的代码行既显示错误，停下。
2. 程序员必备
3. 断点调试能帮我们查看java底层源代码的执行过程，提高程序员水平

- F7（跳入） shift+F8（跳过，下一步） F9（resume，执行下一个断点）

## 二十三、类变量
static修饰的变量 在静态方法区域（具体在哪和版本有关系） 所有类共享，一个改变另一个也变
```java
public class Child {
    public static void main(String[] args) {
        Lt l1 = new Lt();
        Lt l2 = new Lt();
	//	Lt.count++; static修饰的可以用类名调用
        l1.count++;
        System.out.println(l1.count); //1
        System.out.println(l2.count); //1
    }
}
class Lt{
    public static int count =0;
    public void add(){
        count++;
    }
}
```
静态方法不能访问普通变量，只能访问修改static修饰的
普通的不带static修饰的全能

## 二十四、深入理解main方法
main方法形式`public static void main(String[] args){}`
1. main 方法是虚拟机调用
2. java虚拟机需要调用类的main（）方法，所以该方法访问权限必须是public
3. java虚拟机子啊执行main（）方法时不必创建对象，所以该方法必须是static
4. 该方法接收String类型的数组参数，该数组中保存执行java命令时传递给所运行的类的参数，
5. java类 参数一 参数二 参数三
```java
// 输入传参即可观察，如tom cat jack
public static void main(String[] args) {
        // 观察args 如何传入
        for(int i=0;i<args.length;i++){
            System.out.println(args[i]);
        }
    }
```

- mian特别说明，不可以访问本类的非静态成员，要访问必须要先创建一个对象，new Main（）；之后用创建的对象再调用这个非静态成员。




