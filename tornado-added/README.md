
mac上遇到的问题：

ModuleNotFoundError: No module named 'MySQLdb'

[解决](https://blog.csdn.net/a394268045/article/details/78201682)：

``` ruby
python3 -m pip install mysqlclient 
```

工作量估计：

- 搭建tornado提供web服务（已完成60%，估计三天） [3]
- 尝试打通微服务，为系统提供服务（如果打不通就使用http接口服务的方式） (三天) [3]   
- 模型算法熟悉 [5]   层次分析法、熵值法等算法梳理
- 开发剩余的模型算法  [10]
- 模型算法的梳理整合到系统[5] 


======================================

需要处理的内容:

1.0  OK 删除数据库引入的内容 
1.1  OK 统一数据返回格式  
2.   OK 优化框架，添加http请求示例
4. 异常的统一处理,而不是报错抛出错误原因    是否需要引入实体类
3. 数据请求写法整理,主要是 content-type   www-form-data形式  以及json的形式 