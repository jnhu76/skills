# C++ Core Standards

基于 [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) 的编码标准。

## 用途

写、审查、重构 C++ 代码时，确保现代、安全、地道的实践。

## 覆盖范围

- **RAII** — 资源获取即初始化，避免裸指针/手动清理
- **不可变性** — 默认 `const`/`constexpr`
- **类型安全** — 编译期防错
- **值语义** — 优先返回值和作用域对象
- **接口设计** — 表达意图，避免输出参数
- **C++ 设计审查** — 检测 "C with classes" 反模式

## 适用场景

- 新写 C++ 代码（类、函数、模板）
- 审查或重构现有 C++ 代码
- 架构决策（继承 vs 组合 vs 模板 vs variant）
- 跨代码库统一风格

## 不适用

- 非 C++ 项目
- 无法采用现代 C++ 的遗留 C 代码库
- 嵌入式/裸机环境下需选择性适配的场景

## 调用方式

告诉 agent：

> 用 cpp-core-standards 审查这段代码

或

> 用 cpp-core-standards 帮我设计这个类
