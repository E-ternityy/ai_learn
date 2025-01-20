# Python 编程概念全面总结

## 基础语法

- **注释**：
  - 单行注释：使用 `#`。
  - 多行注释：使用 `'''` 或 `"""`。

- **变量**：
  - 动态类型，无需声明类型。
  - 命名规则：字母、数字、下划线，不能以数字开头。

- **输入输出**：
  - 输入：`input("Prompt")`
  - 输出：`print("Message")`

## 数据类型

- **数值类型**：
  - `int`：整数
  - `float`：浮点数
  - `complex`：复数

- **字符串**：
  - 定义：使用单引号 `'` 或双引号 `"`
  - 多行字符串：使用 `'''` 或 `"""`
  - 常用方法：`strip()`, `lower()`, `upper()`, `split()`, `find()`, `replace()`

- **布尔类型**：
  - 值：`True` 和 `False`

- **None**：
  - 表示空值或未定义状态

## 数据结构

- **列表** (`list`)：
  - 定义：`[item1, item2, ...]`
  - 可变，支持索引、切片、方法如 `append()`, `remove()`, `pop()`

- **元组** (`tuple`)：
  - 定义：`(item1, item2, ...)`
  - 不可变，支持索引、切片

- **集合** (`set`)：
  - 定义：`{item1, item2, ...}`
  - 无序不重复，支持集合操作如并集、交集

- **字典** (`dict`)：
  - 定义：`{key1: value1, key2: value2, ...}`
  - 键值对集合，支持方法如 `keys()`, `values()`, `items()`

## 条件控制

- **if 语句**：
  ```python
  if condition:
      # do something
  elif another_condition:
      # do something else
  else:
      # do something different
  ```

## 循环控制

- **for 循环**：
  - 遍历序列或迭代器。
  ```python
  for item in iterable:
      # do something
  ```

- **while 循环**：
  - 基于条件执行。
  ```python
  while condition:
      # do something
  ```

- **循环控制语句**：
  - `break`：终止循环
  - `continue`：跳过当前迭代
  - `pass`：占位符，什么也不做

## 推导式

- **列表推导式**：
  ```python
  [expression for item in iterable if condition]
  ```

- **字典推导式**：
  ```python
  {key_expression: value_expression for item in iterable if condition}
  ```

- **集合推导式**：
  ```python
  {expression for item in iterable if condition}
  ```

## 错误和异常捕获

- **try-except 语句**：
  ```python
  try:
      # code that may raise an exception
  except SomeException as e:
      # handle exception
  else:
      # execute if no exception
  finally:
      # execute always
  ```

## 函数式编程

- **map**：
  - 对序列中每个元素应用函数。
  ```python
  map(function, iterable)
  ```

- **lambda**：
  - 创建匿名函数。
  ```python
  lambda arguments: expression
  ```

- **filter**：
  - 过滤序列。
  ```python
  filter(function, iterable)
  ```

- **reduce**：
  - 累积序列元素。
  ```python
  from functools import reduce
  reduce(function, iterable)
  ```

## 面向对象编程

- **类与实例化**：
  ```python
  class MyClass:
      def __init__(self, attribute):
          self.attribute = attribute

  instance = MyClass(value)
  ```

- **类变量与方法**：
  - 类变量：所有实例共享
  - 实例方法：`def method(self):`
  - 类方法：`@classmethod` 装饰器
  - 静态方法：`@staticmethod` 装饰器

- **私有变量和方法**：
  - 使用 `__` 前缀定义，如 `__private_var`

- **封装**：
  - 通过方法访问私有变量

- **继承**：
  - 子类继承父类。
  ```python
  class SubClass(SuperClass):
      def __init__(self, args):
          super().__init__(args)
  ```

- **多态**：
  - 不同类实现相同方法，使用相同接口调用

- **抽象类**：
  - 使用 `abc` 模块定义抽象基类