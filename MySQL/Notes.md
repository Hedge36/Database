# 基本说明

> Mysql主流版本号为5.6，安装版本号为8.0.24，命令上有不小差异，具体差异参见官网，以官网为准。
>
> + MySQL语句关键字和库名及数据表名 在 Windows 下不区分大小写，但在 **Linux 下区分大小写**。因此，数据库名、 表名、字段名，都不允许出现任何大写字母，避免节外生枝。
> + 使用函数时，函数名与其后的括号之间**不能有空格**。
> + MySQL 中语句的结束不是行的结束，而是 **“;”** 。
>
> **<u>*以下命令大多基于5.6, 实际运行请以参考资料为准，此处未同步至新版。*</u>**



# 1.基础

## 0. 

## 1. 系统变量



## 2. 自定义变量

自定义变量（全局变量）通过 `Set` 命令实现，其后紧跟 `@name=` 表示变量的表示符与其值，无需特别声明变量类型，除此之外，还可以通过``Select` 语句进行赋值，如：

```SQL
SELECT * FROM TABLE INTO Var TABEL_EXPR
```

其中，EXPR值原SELECT语法后序声明部分。

在函数体或存储过程内部，可以使用 `DECLARE`声明局部变量，局部变量不需要使用 `@` 符号，其语法格式如下：

```SQL
DECLARE Var Type [DEFAULT Value];
```



### 1.1 字符串

> **Mysql中，字符串使用单引号‘’或两个单引号闭合，而双引号表示识别转义符，一般情况下无需使用。**

# 2.基本操作概览


## 0. 启动操作

```shell
systemctl start mysqld.service	# 启动
mysql -V	# 查看版本
```
##  1. 帐户管理

通过控制台登陆账户：

```shell
mysql -u *user -p	# Run on machine where you login 
mysql -h *host -u user -p	# Run on other machine
```

账户管理：

```sql
Select * from mysql.user	# Show user info
Create user name identified by 'password'	# Create account/user
Delete from mysql.user Where condition	
Update mysql.user set password=Password('password') where user='account'	# Update account and password
```



## 2. 数据库操作

> 以下列表参数中，大写字母表示关键字，小写表示参数名。

| Function | Description                  |
| -------- | ---------------------------- |
| USE      | 指定默认状态下要操作的数据表 |
| CREATE   | 创建数据库                   |
| SHOW     | 查看指定（所有）数据库       |
| DROP     | 删除指定数据库               |
| ALTER    | 修改数据库                   |

## 3. 数据表操作

> 以下列表参数中，大写字母表示关键字，小写表示参数名。

| Function | Object | Description                      |
| -------- | ------ | -------------------------------- |
| CREATE   | 表     | 创建新的数据表或者复制原有数据表 |
| ALTER    | 表     | 修改指定表                       |
| DESCRIBE | 表     | 查看指定数据表，可指定列         |
| DROP     | 表     | 删除数据表，可指定列             |

## 4. 记录操作

| Function | Description                      |
|   ----   | ----                                  |
| ADD      | 指定默认状态下要操作的数据表     |
| CHANGE   |                                  |
| MODIFY   |                                  |
| DROP    |                                  |
| UPDATE | |
| RANAME   |                                  |
| INSERT   |                                  |

## 5. 辅助操作符

| FUNCTION      | DESCRIBE                     |
| ------------- | ---------------------------- |
| WHERE         | 过滤数据后分组               |
| Having        | 分组后过滤数据               |
| IN            | 包含                         |
| AS            | 别名                         |
| FROM          | 来源                         |
| JOIN          | 连接                         |
| UNION         | 合并                         |
| LIKE          | 模式匹配                     |
| REGEXP        | 正则匹配                     |
| BEWTEEN AND   | 范围比较                     |
| GROUND BY     | 分类                         |
| ORDER BY      | 排序                         |
| HAVEING       | 分组后过滤数据               |
| LIMIT         | [限制数据偏移量与]最大记录数 |

## 6. 功能函数

### 6.1 MATH

| FUNCTION | DESCRIPTION |
|      ----         |           ----                   |
| ABS(X) | 返回X的绝对值 |
| ROUND(X, D) | 取整并保留到D位小数 |
| SQRT(X) | 返回X的平方根 |
| RAND(N) | 随即返回一个浮点数(0-1)，N为随机数种子； |
| FLOOR(X) | 返回不大于X的最大整数 |
| PI() | 返回 $ \pi $ 默认七位 |
| TRUNCATE(X,D) | 截断小数X到D位 |
| LEAST(X1, X2, ...) | 返回序列最小值 |
| GREATEST(X1, X2,...) | 返回序列最大值 |
| BIN(X) | 返回X的二进制值 |
| OTC(X) | 返回X的八进制值 |
| HEX(X) | 返回X的十六进制值 |

### 6.2 AGG

| FUNCTION             | DESCRIPTION      |
| -------------------- | ---------------- |
| SUM([DISTINCT] EXPR) | 返回EXPR的和     |
| AVG(EXPR)            | 返回EXPR的平均值 |
| COUNT(EXPR)          | 返回EXPR的记录数 |
| MAX(EXPR)            | 返回表中最大值   |
| MIN(EXPR)            | 返回表中最小值   |

### 6.3 STR

| FUNCTION                  | DESCRIPTION                |
| ------------------------- | -------------------------- |
| LENGTH(STR)               | 返回字符位长度             |
| CONCAT(STR1, STR2)        | 返回拼接后的字符串         |
| REPEAT(STR, COUNT)        | 返回字符的COUNT次重复      |
| FIND_IN_SET(STR, STRLIST) | 返回STR在STRLIST中的位置   |
| LOCATE(SUBSTR, STR)       | 返回SUBSTR第一次出现的位置 |
| INSTR()                   | 返回SUBSTR第一次出现的位置 |
| LEFT(STR, LEN)            | 截取左侧N个字符            |
| RIGHT(STR, LEN)           | 截取右边N个字符            |
| SUBSTRING(STR, POS)       | 截取中间POS位置的字符      |
| LCASE(STR)                | 全部小写                   |
| REPLACE(STR， FROM, TO)   | 将STR中FROM替换为TO字符    |
| REVERSE(STR)              | 反转字符                   |
| SPACE(N)                  | 返回N个空白组成字符串      |

### 6.4 DATE

| FUNTION         | DESCRIPTION                      |
| --------------- | -------------------------------- |
| CURDATE()       | 返回当前日期                     |
| CURTIME()       | 返回当前时间                     |
| NOW()           | 返回当前日期和时间               |
| YEAR(EXPR)      | 返回EXPR的年份，同理月日周时分秒 |
| DAYOFYEAR(EXPR) | 返回这一天对应的年、月、星期序数 |

### 6.5 FORMAT

FORMAT(X, D) / DATE_FORMAT(DATE, FORMAT) /TIME_FORMAT(TIME, FORMAT)

| FORMAT | DESCRIPTION |
| ------ | ----------- |
| %S     | 秒          |
| %I     | 分          |
| %H     | 24时制时间  |

略

# 3. 视图与索引

## 1. 视图介绍

> **视图是**从一个或多个表（或视图）中导出的**表**。视图是用数据库的用户使用数据库的观点，它与表有很多相似之处，也由若干字段和表组成，也可以作为SELECT的数据源。然而视图中的数据并不像索引和表那样需要占用存储空间，它的本质仅为一个SQL命令（集合），其数据都来自表，因而数据表又称基表或基本表，视图又称虚表。
>
> 与直接从数据表中提取数据相比，视图的特点如下：
>
> + **使操作变简单**：使用视图可以简化数据查询操作，对于常用的查询，最好将其封装成一个视图；
> + **避免数据冗余**：由于视图保存的是一条命令，所有的数据保存在数据库表中，为不同应用程序提供服务的同时又不会造成数据冗余；
> + **增强数据安全性**：同一个数据库表中可以创建不同的视图，为不同的用户分配不同的视图，这样就可以实现不同的用户只能查询或修改阈值对应的数据，继而增强了数据的安全性；
> + **提高数据的逻辑独立性**：如果没有视图，应用程序直接建立在数据库表上，而视图的存在，可以在一定程度上逻辑分离两者。

## 2. 创建视图

创建视图需要有CREATAE VIEW的权限，并且对于查询设计的列有SELECT权限。

```SQL
CREATE [OR REPLACE] [ALGORITHM = {UNDEFINE | MERGE |TEMPTABLE}]
	VIEW View_name [(Columns_list)]
	AS Select_statement
	[WITH [CASCADED | LOCAL] CHECK OPTION]
```

参数说明：

> + OR REPLACE：若存在同名视图，替换同名视图；
> + ALGORITHM：选择SQL运行算法，不展开介绍；
> + View_name：视图名称；
> + Columns_list：视图列的明确名称，若保持不变，则可省略；
> + Select_statement：创建视图的查询语句；
> + WITH [CASCADED | LOCAL] CHECK OPTION：视图更新检查，若不满足where条件，则不更新；

## 3. 视图操作

> 查看视图是查看数据库中已存在的视图的定义，查看视图必须有 SHOW VIEW的权限，其查询方法包括三种：`Describe` 、`Show table status` 与 `Show create view`，更新视图的方法包括：`Insert`、`Update`与`Delete` ，删除视图使用 `Drop` 方法。

```SQL
INSERT INTO View
VALUES(values,,,);

UPDATE View
	SET attr = +_*?;

DELETE FROM View
	WHERE Condition;

ALTER VIEW View
AS
	SELECT Statement;
	
DROP VIEW [IF EXISTS]
View_name [, View_name,,,]
[RESTRICT | CASCADE]
```

## 4. 索引

> 索引是数据库表中字段值的复制，该字段称为索引的关键字，MYSQL在搜索时，优先对索引进行检索，若无结果，则对全表检索，此外，索引可以有多个值。，索引具备以下特点：
>
> + 通过创建唯一索引，可以保证数据库表中的每一行数据的唯一性；
> + 可以大大加快查询速度；
> + 可以实现数据的参照完整性，加速表与表之间的连接；
> + 在使用分组和排序自居进行数据查询时，可以显著减少查询中分组和排序的时间。
>
> 索引的分类：
>
> + 普通索引和唯一索引：
> + 单列索引和组合索引：
> + 全文索引：
> + 空间索引：

## 5. 索引操作

创建索引可以在创建表的同时进行，同时，对于降低数据库性能的索引，可以删除。

```SQL
CREATE Table
(
	...
    PRIMARY KEY(Col1, Col2,,,)
    INDEX cj(Col3)
);

DROP INDEX name ON Table;
```



# 4. 内部存储与触发

> 内部存储包括存储过程与存储函数，存储过程是一组为了完成特定功能的SQL语句集，经编译后存储在数据库中，用户通过指定存储过程的名字并给定参数来调用执行它，存储函数与其定义语法类似，但内容不同且限制比较多，一般来说，前者功能更复杂，后者更具功能针对性。
>
> 此外，用于协助管理操作数据库，还有触发器与事件类型，前者用于激活对象，后者用于事件管理与响应。

## 1. 存储过程

```SQL
CREATE PROCEDURE Name(proc[Params])
	[CHARACTERSIC]
	BODY

/*
proc:[IN | OUT | INOUT]
存储过程参数输入与输出，IN表示输入的参数，OUT表示输出的参数，INOUT表示既输入又输出的参数。
*/
/* CHARACTERISC
	LANGUAGE SQL	编译过程使用语言，未来支持PHP
	| [NOT] DETERMINISTIC	同样的输入是否得到同样的输出
	| { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA}
	| SQL SECURITY { DEFINER | INVOKER}	许可证选择
	| COMMENT	注释
*/
```

创建后，存储过程需要调用，调用通过`CALL`方法实现；同时，值得注意的是存储过程可能因为包含多条SQL语句，所以同样有开始标记和结束标记，分别是 DELIMIETRT $ $ 与DELIMITER。

```SQL
Delimiter $ $ 
Create procedure sele(in zk char(20))
/*body*/
begin
select * from student where zkzh=zk
end 
/*body*/
$ $	delimiter;

call sele(1201010101)
```

## 2.  存储函数

```sql
Create Function name ([params])
	Return type
	[Characterisic]
	body
```



## 3. 触发器

触发器是MySQL提供给程序员和数据分析员来保证数据完整性的一种方法，他是与表事件相关联的特殊的存储过程，它的执行由表操作出发，用于加强数据的完整性约束和业务规则等。

```SQL
Create Trigger name time event
	On table For EACH ROW stmt
```

参数说明:

> + name是触发器的名字；
> + time是触发程序的动作时间，它可以是Before或者After,以指明触发程序触发时间与事件时间先后顺序；
> + event表明触发程序的语句类型，可以是 [ INSERT, UPDATE, DELETE]

触发器的删除依然通过`Drop`实现。

## 4. 事件

系统管理或者数据库管理中，经常要周期性地执行某一个命令或者SQL命令，类似与Linux服务中的cron计划服务，能很方便地定期运行指定命令。

```sql
Show Variables Like 'event_scheduler';
Select @@event_Scheduler;
Show processlist;
```

如果看到事件状态为on就说明该事件已经启动，如果为off则表明该事件为启动，我们可以通过以下命令启动它：

```SQL
Set Global event_scheduler = ON;
```

创建事件则可以通过以下命令：

```SQL
Create [Definer= {user|current_user} ]
Event [if not exists ] name
On Schedule schedule
[On Completion [Not] Perserve]
[ENABLE | Disable | Disable On Slave]
[Comment 'Comment']
Do 
body;

/*schedule
At timestamp [+ Interval]...|Every interval
[Starts timestamp [+ Interval]...]
[Ends timestamp [+ Interval]...]
*/
```

如：

```sql
Delimiter $ $
Create Event instu
On Schedule every 1 month
Starts curdate() + Interval 1 month
Ends '2030-12-31'
Do 
Begin
	Delete Form testinfo;
End $ $
Delimiter;
```

该事件每月启动一次，下个月开始，2030年结束。

事件的修改与删除同样使用`Alter`与`Drop`方法。

## 5. Example——Login

```sql
Drop procedure if exists login;
Delimiter $ $
Create procedure login(in account char(8), in password char(10), out status int)
Begin
Declare name char(10);
Select username into name from users where username=account and pwd = Password(password);
If name = account then 
	Set status = 200;
Else
	Set status = 404;
End If;
End $ $
Delimiter;
```



# 5. 事务处理与并发操作

## 1. 事务

事务是满足 ACID 特性的操作，可以通过 Commit 提交事务，也可以使用 Rollback 进行回滚。

> **A（Atomicity）原子性**：事务被视为不可分割的小单元，事务的所有操作要么全部提交成功，要么全部失败回滚。
>
> **C（Consistency）一致性**：数据库在事务执行前后都保持一致性状态。在一致性状态下，所有事务对一个数据的读取结果都是相同的。
>
> **I（Isolation）隔离性**：事务之间的操作是相互隔离的。
>
> **D（Durability）持久性**：一旦事务提交，则其所做的修改将会永远保存到数据库中。

## 2. 并发一致性

> 在并发环境下，容易造成并发一致性问题，导致隔离性被破坏。假设目前有两个事务，分别命名为A和B，在并发环境下，容易出现以下问题。
>
> **丢失更新**：A、B同时修改数据，A先，B后，A提交后B提交，B操作覆盖了A的操作，导致A丢失更新。
>
> **读脏数据**：A修改数据，B读取数据；随后A撤销操作，则B读到脏数据。
>
> **不可重复读**：B读取数据，A修改数据，B再次读取数据，发现数据和第一次读时不一致。
>
> **幻读**：A读取了某个范围的数据，B在此范围内插入一条数据；A再次读取，结果不一样。

## 3. 锁

在并发环境下，为解决并发一致性问题保证事务的隔离性，可采取封锁机制。当一个事务在进行操作时加锁，限制另一个事务的操作。

一般而言，为保证效率，锁的粒度不宜太大。在MySQL中，提供了行锁和表锁。

> **行锁**：事务A操作数据时，只封锁被操作的行，事务B可以操作其他行的数据，并发程度高；
>
> **表锁**：事务A操作数据时，封锁整个表，事务B要等A完成才能操作，并发度较低。



在读写方面数据库锁也分为读锁（共享锁）和写锁（排他锁）。

> **读锁**：若事务A加了此锁，A可以对数据进行读取操作，但不能更新；其它事务也可以读，但不能修改；
>
> **写锁**：若事务A加了此锁，A可以对数据进行读和写操作，其它事务不能读写，否则会阻塞。

 

上面所说的是悲观锁，MySQL中InnoDB也提供了乐观锁的实现——MVCC（多版本并发控制）。用通俗的方式解释悲观锁和乐观锁大概是这样：

> **悲观锁**：认为每次操作都会修改数据，每次都在操作前上锁；
>
> **乐观锁**：认为每次操作都不会修改数据，不上锁，但是会记录一个版本号或者时间戳，用来对比。

**MVCC**则是乐观锁的实现，它在每行记录后面都保存着两个隐藏的列，用来存储创建版本号和删除版本号。

## 4. 隔离级别

若锁的操作要用户自己控制，会比较复杂，因此数据库管理系统提供了事务的隔离级别，使问题简单化。MySQL的隔离级别有四种，分别是：未提交读、已提交读、可重复读、可序列化。它们与并发一致性问题的关系如下表所示。MySQL默认隔离级别为：可重复读

| 隔离级别 | 脏读 | 不可重复读 | 幻读 |
| -------- | ---- | ---------- | ---- |
| 未提交读 | ✔    | ✔          | ✔    |
| 已提交读 | ❌    | ✔          | ✔    |
| 可重复读 | ❌    | ❌          | ✔    |
| 可序列化 | ❌    | ❌          | ❌    |

> **未提交读**：事务修改数据，即使未提交，其它事务依旧可见。
>
> **已提交读**：事务修改数据提交之前，其他事务不可见。
>
> **可重复读**：事务多次读取数据的结果都一样。
>
> **可序列化**：解决了幻读问题。

## 5. 存储引擎

说到数据库的并发问题，就要提一下MySQL的存储引擎。MySQL的存储引擎有很多种，最常用的还是MyISAM和InnoDB，它们的区别如下：

|          | MyISAM                     | InnoDB             |
| -------- | -------------------------- | ------------------ |
| 事务     | 不支持                     | 支持               |
| 锁的粒度 | 表锁                       | 行锁               |
| 索引缓存 | 只缓存索引，不缓存真实数据 | 缓存索引和真实数据 |
| 表空间   | 小                         | 大                 |
| 关注点   | 性能                       | 事务               |

因此，一般在读操作比较多的情况下，MyISAM的效率更高，因为相比于InnoDB，它维护的东西要少，比如版本号，索引数据等。

但是InnoDB支持事务，而且在并发环境下优势显著。至于如何选择存储引擎，应根据具体情况而定。

## 6. 扩展技术*

> 1. 并发插入技术
> 2. 锁调度技术
> 3. 锁竞争消减技术
> 4. 死锁避免技术
> 5. 性能优化技术



# 6. 数据备份与恢复

## 1. 数据备份介绍

### 1.1 为何要备份

在生产环境中我们数据库可能会遭遇各种各样的不测从而导致数据丢失, 大概分为以下几种.

> - 硬件故障
> - 软件故障
> - 自然灾害
> - 黑客攻击
> - 误操作 (占比最大)

须知在生产环境中，服务器的硬件坏了可以维修或者换新，软件崩溃可以修复或重新安装, 但是如果数据没了那可就毁了，生产环境中最重要的应该就是数据了。所以, 为了在数据丢失之后能够恢复数据, 我们就需要定期的备份数据。

在之前的章节里我们介绍过innodb存储引擎有自动的数据恢复功能，在执行一条写操作并且commit成功时innodb存储引擎会将新数据其写入redo log，此时如果数据库挂掉，重启后仍然可以依据redo log来恢复尚未执行完毕的数据，这跟本节讲的数据备份与恢复是两回事，试问，如果你一张表的数据不小心删掉了，redo log能帮你恢复吗，no，它只能帮你完成你尚未完成的操作，而对于你已经完成的操作，它帮不了你。所以不要混淆，为了防止数据意外丢失，我们还是应该做好定期的数据备份工作。

### 1.2 备份对象

> 一般情况下, 我们需要备份的数据分为以下几种
>
> - 数据
> - 二进制日志, InnoDB事务日志
> - 代码(存储过程、存储函数、触发器、事件调度器)
> - 服务器配置文件

### 1.3 备份的类型

#### 1）冷备、温备、热备

按照备份时数据库的运行状态，可以分为三种

> 1）**冷备**：停库、停服务来备份，即当数据库进行备份时, 数据库不能进行读写操作, 即数据库要下线。
>
> 2）**温备**：不停库、不停服务来备份，会(锁表)阻止用户的写入，即当数据库进行备份时, 数据库的读操作可以执行, 但是不能执行写操作。
>
> 3）**热备**（建议）：不停库、不停服务来备份，也不会(锁表)阻止用户的写入
> 即当数据库进行备份时, 数据库的读写操作均不是受影响。

`MySQL`中进行不同类型的备份还要考虑存储引擎是否支持

- MyISAM

	热备 ×

	温备 √

	冷备 √

- InnoDB

	热备 √

	温备 √

	冷备 √

#### 2）物理与逻辑

按照备份的内容分，可以分为两种

> - 1、物理备份：直接将底层物理文件备份
> - 2、逻辑备份：通过特定的工具从数据库中导出sql语句或者数据，可能会丢失数据精度

#### 3）全量、差异、增量

按照每次备份的数据量，可以分为

- 全量备份/完全备份（Full Backup）：备份整个数据集( 即整个数据库 )
- 部分备份：备份部分数据集(例如: 只备份一个表的变化)

> 而部分备份又分为：差异备份和增量备份两种
>
> 1. 差异备份（Differential Backup）:每次备份时，都是基于第一次完全备份的内容，只备份有差异的数据(新增的、修改的、删除的)
> 2. 增量备份（Incremental Backup ）:每次备份时，都是基于上一次备份的内容（注意是上一次，而不是第一次），只备份有差异的数据(新增的、修改的、删除的)，所以增量备份的结果是一条链。

![img](/home/hedge/Typora/Temp-image/32-1.jpg)

针对上述三种备份方案，如何恢复数据呢

> 1、全量备份的数据恢复
>
> 只需找出指定时间点的那一个备份文件即可，即只需要找到一个文件即可
>
> 2、差异备份的数据恢复
>
> 需要先恢复第一次备份的结果，然后再恢复最近一次差异备份的结果，即需要找到两个文件
>
> 3、增量备份的数据恢复
>
> 需要先恢复第一次备份的结果，然后再依次恢复每次增量备份，直到恢复到当前位置，即需要找到一条备份链

综上，对比三种备份方案
1、占用空间：全量 > 差异 > 增量
2、恢复数据过程的复杂程度：增量 > 差异 > 全量

### 1.4 备份的工具

| 备份工具           | 备份速度 | 恢复速度 | 便捷性                   | 适用存储引擎                         | 支持的备份类型                                               | 功能 | 应用场景           |
| ------------------ | -------- | -------- | ------------------------ | ------------------------------------ | ------------------------------------------------------------ | ---- | ------------------ |
| cp、tar等（物理）  | 快       | 快       | 一般                     | 所有                                 | 冷备、全量、差异、增量                                       | 很弱 | 少量数据备份       |
| lvm2快照（物理）   | 快       | 快       | 一般                     | 所有                                 | 支持几乎热备（即差不多是热备，哈哈），是借助文件系统管理工具进行的备份 | 一般 | 中小型数据量的备份 |
| xtrabackup（物理） | 较快     | 较快     | 是一款非常强大的热备工具 | 由`percona`提供，只支持InnoDB/XtraDB | 热备、全量、差异、增量                                       | 强大 | 较大规模的备份     |
| mysqldump（逻辑）  | 慢       | 慢       | 一般                     | 所有                                 | 支持温备、完全备份、部分备份、对于**InnoDB**存储引擎支持热备 | 一般 | 中小型数据量的备份 |

此外，如果考虑到增量备份，还需要结合binlog日志（binlog只属于增量恢复），需要用到工具mysqlbinlog，相当于逻辑备份的一种

## 2. 设计备份策略

### 2.1 备份策略设计的参考值

备份数据的策略要根据不同的应用场景进行定制, 大致有几个参考数值, 我们可以根据这些数值从而定制符合特定环境中的数据备份策略

> - 能够容忍丢失多少数据
> - 恢复数据需要多长时间
> - 需要恢复哪一些数据

### 2.2 三种备份策略及应用场景

针对不同的场景下, 我们应该制定不同的备份策略对数据库进行备份, 一般情况下, 备份策略一般为以下三种

> - **直接cp,tar复制数据库文件**
> - **mysqldump+复制BIN LOGS**
> - **lvm2快照+复制BIN LOGS**
> - **xtrabackup+复制BIN LOGS**

以上的几种解决方案分别针对于不同的场景

> 1. 如果数据量较小, 可以使用第一种方式, 直接复制数据库文件
> 2. 如果数据量还行, 可以使用第二种方式, 先使用mysqldump对数据库进行完全备份, 然后定期备份BINARY LOG达到增量备份的效果
> 3. 如果数据量一般, 而又不过分影响业务运行, 可以使用第三种方式, 使用`lvm2`的快照对数据文件进行备份, 而后定期备份BINARY LOG达到增量备份的效果
> 4. 如果数据量很大, 而又不过分影响业务运行, 可以使用第四种方式, 使用`xtrabackup`进行完全备份后, 定期使用`xtrabackup`进行增量备份或差异备份

## 3. 备份实战

### 3.1 使用cp进行备份

备份步骤

```bash
#1、向所有表施加读锁
FLUSH TABLES WITH READ LOCK;  

#2、备份数据文件
mkdir /jason_bak
cp -a /var/lib/mysql/* /jason_bak
```

模拟数据丢失并恢复

```bash
# 数据丢失
rm -rf /var/lib/mysql/*

# 恢复数据
cp -a /jason_bak/* /var/lib/mysql

# 重启服务
systemctl restart mysql
```

### 3.2 使用mysqldump+复制BINARY LOGS备份

mysqldump命令

```bash
#==========语法
mysqldump  -h 服务器  -u用户名  -p密码  选项与参数 > 备份文件.sql

===选项与参数
1、-A/--all-databases	         所有库
2、-B/--databases bbs db1 db2	 多个数据库
3、db1                          数据库名
4、db1 t1 t2		            db1数据库的表t1、t2
5、-F                           备份的同时刷新binlog
6、-R 备份存储过程和函数数据（如果开发写了函数和存储过程，就备，没写就不备）
7、--triggers 备份触发器数据（现在都是开发写触发器）
8、-E/--events 备份事件调度器
9、-d 仅表结构
10、-t 仅数据
11、--master-data=1  备份文件中 change master语句是没有注释的，默认为1
用于已经制作好了主从，现在想扩展一个从库的时候使用
如此备份，扩展添加从库时导入备份文件后
便不需要再加mater_pos了
change matser to
master_host='10.0.0.111'
master_user='rep'
master_password=123
master_log_pos=120
master_log_file='master-bin.000001'
                             
12、--master-data=2  备份文件中 change master语句是被注释的 
 
13、--lock-all-tables 备份过程中所有表从头锁到尾，简单粗暴
在mysqldump导出的整个过程中以read方式锁住数据库中所有表，类似 flush tables with read lock 的全局锁），
这是一个全局读锁，只允许读不允许写，以此保证数据一致性。
比如当前数据库有如下schema：
information_schema（不会导出）
mysql
performance_schema（不会导出）
sys（不会导出）
test
test1
test2
那么我们在使用mysqldump导出时：
mysqldump --lock-all-tables --set-gtid-purged=on -AER > test.sql
指定--lock-all-tables参数，那么从一开始就对整个mysql实例加global read lock锁。
这整个全局读锁会一直持续到导出结束。
所以在这个过程中，数据库实际严格处于read only状态。
所以导出的数据库在数据一致性上是被严格保证的，也就是数据是一致性的。
由于这个参数会将数据库置于read only状态（也相当于不可使用状态），所以默认不加该参数。
这相当于脱机备份的感觉，所以生产数据库的备份策略上，也很少使用该参数。

该参数本身默认off,但使用该参数的话，也会自动将 --single-transaction 及 --lock-tables 参数置于 off 状态,他们是互斥的。

对于支持事务的表例如InnoDB和BDB，推荐使用--single-transaction选项，因为它根本不需要锁定表

14、--single-transaction： 快照备份 （搭配--master-data可以做到热备）
保证各个表具有数据一致性快照。
指定 --single-transaction 参数，那么导出过程中只能保证每个表的数据一致性（利用多版本特性实现，目前只能针对InnoDB事务表）。
比如有一个大表，mysqldump对该表的导出需要1分钟，那么在这1分钟的过程中，该表时可以被正常访问的。
（正常访问包括增删改查，但是alter table等对表结构发生更改的语句要被挂起。）
mysqldump能够保证从开始对该表进行导出，一直到对该表的导出结束，该表的数据都是开始的一致性数据快照状态。
所以该参数明显不能保证各个表之间的数据一致性（特别是外键约束的父表和子表之间）。
但是该参数能够让数据库处于可使用（就是应用感觉数据库可用）状态，相当于联机备份，所以被经常使用。
该参数默认off。

15、--lock-tables：如果是备份所有库，那么备份到某个库时只锁某个库，其他库可写，而--lock-all-tables是从始自终都全都锁定

保证各个schema具有数据一致性快照。
指定 --lock-tables 参数，那么在导出过程中能够保证各个schema的数据一致性。
比如导出 cms 库（该库有155张表）时：
mysqldump --lock-tables --set-gtid-purged=off -ER -B cms>test.sql
从命令开始，就对 cms 库的155张表加类似 lock table xxx read 的读锁。
这会导致在导出整个cms库的过程中，cms库实际上整体处于read only状态。
但是如果我们指定如下命令：
mysqldump --lock-tables --set-gtid-purged=on -AER >test.sql
来导出全部mysql库，那么当导出cms库的过程中，其他 schema 实际上是可以被正常访问的。
这个正常访问就是可以接受所有合法的sql语句。
所以该参数只能保证各个schema自己的数据一致性快照。
该参数默认on。

#==========完整语句 
mysqldump -uroot -pEgon@123 -A -E -R --triggers --master-data=2 --single-transaction > /backup/full.sql

#====文件太大时可以压缩 gzip ，但是gzip不属于mysql独有的命令，可以利用管道
mysqldump -uroot -pEgon@123 -A -E -R --triggers --master-data=2 --single-transaction | gzip > /tmp/full$(date +%F).sql.gz

#====导出时压缩了，导入时需要解压，可以使用zcat命令，很方便
zcat /backup/full$(date +%F).sql.gz | mysql -uroot -p123
```

储备知识：binlog内容很多，如何定位到某个固定的点

```bash
===> 1、grep过滤

===> 2、检查事件：依据End_log_pos的提示，来确定某一个事件的起始位置与结束位置
mysql> show binlog events in 'mybinlog.000001'; 
如果事件很多，可以分段查看
mysql> show binlog events in 'mybinlog.000001' limit 0,30; 
mysql> show binlog events in 'mybinlog.000001' limit 30,30; 
mysql> show binlog events in 'mybinlog.000001' limit 60,30; 

===> 3、利用mysqlbinlog命令
生产中很多库，只有一个库的表被删除，我不可能把所有的库都导出来筛选，因为那样子binlog内容很多，辨别复杂度高，我们可以利用

[root@jason mysql]# mysqlbinlog -d db1 --start-position=123 --stop-position=154 mybinlog.000001 --base64-output=decode-rows -vvv | grep -v 'SET'

参数解释：
1）-d 参数接库名
mysqlbinlog -d database --base64-output=decode-rows -vvv mysql-bin.000002
2）--base64-output  显示模式
3）-vvv			显示详细信息
```

备份：

```bash
# 1、先打开binlog日志
vim /etc/my.cnf
[mysqld]
server_id=1
log-bin=/var/lib/mysql/mybinlog
binlog_format='row' #(row,statement,mixed)    
binlog_rows_query_log_events=on
max_binlog_size=100M

# 2、登录数据库，插入测试数据
mysql> create database db3;
mysql> use db3;
mysql> create table t1(id int);
mysql> insert t1 values(1),(2),(3);

# 3、在命令行执行命令，进行全量备份
[root@jason mysql]# mysqldump -uroot -pEgon@123 -A -R --triggers --master-data=2 --single-transaction | gzip > /tmp/full.sql.gz

# 4、在命令行执行命令，刷新binlog，便于日后查找
[root@jason mysql]# mysql -uroot -pEgon@123 -e "flush logs"

# 5、登录数据库，再插入一些数据，模拟增量，这些数据写入了新的binlog
mysql> use db3;
mysql> insert t1 values(4),(5),(6);
```

模拟数据损坏恢复

```bash
# 模拟数据丢失
mysql> drop database db1;

# 恢复数据
# 1、mysql数据导入时，临时关闭binlog，不要将恢复数据的写操作也记入
mysql> set sql_log_bin=0;

# 2、先恢复全量
mysql> source /tmp/full.sql

如果是压缩包呢，那就这么做
mysql> system zcat /tmp/full.sql.gz | mysql -uroot -pEgon@123

# 3、再恢复增量
导出：注意导出binlog时不要加选项--base64-output
[root@jason mysql]# mysqlbinlog mybinlog.000002 --stop-position=531 > /tmp/last_bin.log
导入
mysql> source /tmp/last_bin.log

# 4、开启二进制日志
mysql> SET sql_log_bin=ON; 
```

测试在线热备份

可以先准备一个存储过程，一直保持写入操作，然后验证热备

```bash
#1. 准备库与表
create database if not exists db1;
use db1;
create table s1(
id int,
name varchar(20),
gender char(6),
email varchar(50)
);

#2. 创建存储过程，每隔3秒插入一条
delimiter $$ #声明存储过程的结束符号为$$
create procedure auto_insert1()
BEGIN
    declare i int default 1;
    while(i<3000000)do
        insert into s1 values(i,'jason','male',concat('jason',i,'@oldboy'));
	    select concat('jason',i,'_ok') as name,sleep(3);
		set i=i+1;
    end while;
END$$ #$$结束
delimiter ;

#3. 查看存储过程
show create procedure auto_insert1\G 
```

备份：

```bash
# 1、先打开binlog日志
略

# 2、登录数据库，执行存储过程
mysql> use db1;
mysql> call auto_insert1();

若想杀死存储过程
mysql> show processlist; -- 查出id
mysql> kill id号;


# 3、在命令行执行下述命令，进行全量备份
[root@jason mysql]# mysqldump -uroot -pEgon@123 -A -R --triggers --master-data=2 --single-transaction | gzip > /tmp/full.sql.gz

# 4、全量备份完毕后的一段时间里，数据依然插入，写入了mybinlog.000001中
#    然后我们在命令行刷新binlog，产生了新的mybinlog.000002
[root@jason mysql]# mysql -uroot -pEgon@123 -e "flush logs"

# 5、此时数据依然在插入，但都写入了最新的mybinlog.000002中，所以需要知道的是，增量的数据在mysqlbinlog.000001与mybinlog.000002中都有
我们登录数据库，杀掉存储过程，观察到最新的数据插到了id=55的行
mysql> show processlist; -- 查出id
mysql> kill id号;
```

删除数据

```bash
drop database db1;
```

恢复数据

```bash
# 登录数据库，先恢复全量
mysql> set sql_log_bin=0;
mysql> system zcat /tmp/full.sql.gz | mysql -uroot -pEgon@123
mysql> select * from db1.s1; -- 查看恢复到了id=28，剩下的去增量里恢复

# 在命令行导出mybinlog.000001中的增量，然后登录库进行恢复
查找位置，发现@1=29即第一列等于29，即id=29的下一个position是10275
mysql> show binlog events in 'mybinlog.000001';  
[root@jason mysql]# mysqlbinlog mybinlog.000001 --start-position=10038  --stop-position=11340 --base64-output=decode-rows -vvv | grep -v 'SET' | less

在命令行中执行导出
[root@jason mysql]# mysqlbinlog mybinlog.000001 --start-position=10275 > /tmp/1.sql

在库内执行导入,发现恢复到了39
mysql> source /tmp/1.sql  -- 最好是在库内恢复，因为sql_log_bin=0，导入操作不会记录
mysql> select * from db1.s1;

# 在命令行导出mybinlog.000002中的增量，然后登录库进行恢复
上面恢复到了id=39，我们接着找id=40的进行恢复，查找位置
发现@1=40的position是432
发现@1=55的position是6464
mysql> show binlog events in 'mybinlog.000002'; 
[root@jason mysql]# mysqlbinlog --base64-output=decode-rows -vvv mybinlog.000002|grep -v 'SET'|grep -C20 -w '@1=40'
[root@jason mysql]# mysqlbinlog --base64-output=decode-rows -vvv mybinlog.000002|grep -v 'SET'|grep -C20 -w '@1=55'


导出
[root@jason mysql]# mysqlbinlog mybinlog.000002 --start-position=432 --stop-position=6464> /tmp/2.sql

在库内执行导入,发现恢复到了55
mysql> source /tmp/2.sql  
mysql> select * from db1.s1;

# 开启binlog
mysql> SET sql_log_bin=ON; 
```

问题：能否利用binlog做全量恢复

```bash
可以，但直接使用binlog做全量恢复，成本很高，我们只用起来做增量恢复。

正确的方案是：全备+binlog增量
每天或者每周全备一次，全备之后，那个位置点之前的binlog全都可以删除，不可能一年有上百个binlog的库都导出来筛选，因为那样子binlog内容很多，辨别复杂度高，我们可以利用
```

### 3.3 使用lvm2快照备份数据

**部署lvm环境**

```bash
# 1、添加硬盘; 这里我们直接实现SCSI硬盘的热插拔, 首先在虚拟机中添加一块硬盘, 无需重启
echo '- - -' > /sys/class/scsi_host/host0/scan 
echo '- - -' > /sys/class/scsi_host/host1/scan 
echo '- - -' > /sys/class/scsi_host/host2/scan 

# 2、创建逻辑卷
pvcreate /dev/sdb
vgcreate vg1 /dev/sdb
lvcreate -n lv1 -L 5G vg1 

# 3、格式化制作文件系统并挂载
mkfs.xfs /dev/mapper/vg1-lv1  
mkdir /lv1
mount /dev/mapper/vg1-lv1 /var/lib/mysql
chown -R mysql.mysql /var/lib/mysql

# 4、修改mysql配置文件的datadir如下
[root@node1 ~]# rm -rf /var/lib/mysql/*  # 删除原数据
[root@node1 ~]# vim /etc/my.cnf    
[mysqld]
datadir=/var/lib/mysql

# 5、重启MySQL、完成初始化
[root@node1 ~]# systemctl restart mysqld 

# 6、往数据库内插入测试数据
create database db3;
use db3;
create table t1(id int);
insert t1 values(1),(2),(3);
```

**创建快照卷并备份**

```
mysql> FLUSH TABLES WITH READ LOCK;     #锁定所有表
Query OK, 0 rows affected (0.00 sec)

[root@node1 lvm_data]# lvcreate -L 1G -s -n lv1_from_vg1_snap /dev/vg1/lv1   #创建快照卷

mysql> UNLOCK TABLES;  #解锁所有表
Query OK, 0 rows affected (0.00 sec)

[root@node1 lvm_data]# mkdir /snap1  #创建文件夹
[root@node1 lvm_data]# mount -o nouuid /dev/vg1/lv1_from_vg1_snap /snap1

[root@localhost snap1]# cd /snap1/

[root@localhost snap1]# tar cf /tmp/mysqlback.tar *  

[root@localhost snap1]# umount /snap1/ -l
[root@localhost snap1]# lvremove vg1/lv1_from_vg1_snap
```

**恢复数据**

```sql
rm -rf /var/lib/mysql/*

# 恢复
tar xf /tmp/mysqlback.tar -C /var/lib/mysql/
```

### 3.4 物理备份之Xtrabackup

#### （1）介绍

`Xtrabackup`是由`percona`提供的`mysql`数据库备份工具，据官方介绍，这也是世界上惟一一款开源的能够对innodb和xtradb数据库进行热备的工具。特点：

1. 备份过程快速、可靠；
2. 备份过程不会打断正在执行的事务；
3. 能够基于压缩等功能节约磁盘空间和流量；
4. 自动实现备份检验；
5. 还原速度快；

使用`xtrabackup`使用InnoDB能够发挥其最大功效, 并且InnoDB的每一张表必须使用单独的表空间, 我们需要在配置文件中添加 `innodb_file_per_table = ON` 来开启

#### （2）安装

版本选择

```bash
mysql 5.7以下版本，可以采用percona xtrabackup 2.4版本

mysql 8.0以上版本，可以采用percona xtrabackup 8.0版本，xtrabackup8.0也只支持mysql8.0以上的版本

比如，接触过一些金融行业，mysql版本还是多采用mysql 5.7，当然oracle官方对于mysql 8.0的开发支持力度日益加大，新功能新特性迭代不止。生产环境采用mysql 8.0的版本比例会日益增加。
```

![img](/home/hedge/Typora/Temp-image/34.png)
![img](/home/hedge/Typora/Temp-image/35.png)

安装方式一

```bash
# 安装yum仓库
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm -y

# 安装XtraBackup命令
yum install percona-xtrabackup-24 -y
```

安装方式二

```bash
#下载epel源
wget -O /etc/yum.repos.d/epel.repo  https://mirrors.aliyun.com/repo/epel-7.repo

#安装依赖
yum -y install perl perl-devel libaio libaio-devel perl-Time-HiRes perl-DBD-MySQL

#下载Xtrabackup
wget https://downloads.percona.com/downloads/Percona-XtraBackup-2.4/Percona-XtraBackup-2.4.23/binary/redhat/7/x86_64/percona-xtrabackup-24-2.4.23-1.el7.x86_64.rpm

# 安装
yum localinstall -y percona-xtrabackup-24-2.4.4-1.el6.x86_64.rpm
```

安装完后会生成命令

```bash
xtrabackup      以前使用该命令
innobackupex    现在使用该命令

innobackupex是xtrabackup的前端配置工具，使用innobackupex备份时, 会调用xtrabackup备份所有的InnoDB表, 复制所有关于表结构定义的相关文件(.frm)、以及MyISAM、MERGE、CSV和ARCHIVE表的相关文件, 同时还会备份触发器和数据库配置文件信息相关的文件, 这些文件会被保存至一个以时间命名的目录.
```

#### （3）Xtrabackup 备份方式（物理备份）

```bash
1.对于非innodb表（比如myisam）是直接锁表cp数据文件，属于一种温备。

2.对于innodb的表（支持事务），不锁表，cp数据页最终以数据文件方式保存下来，并且把redo和undo一并备走，属于热备方式。

3.备份时读取配置文件/etc/my.cnf
```

#### （4）Xtrabackup全量备份

```bash
#1、创建备份目录，会把mysql的datadir中的内容备份到改目录中
mkdir /backup

#2、全备
#2.1 在本地执行下述命令，输入登录数据的本地账号与密码
#2.2 指定备份目录为/backup下的full目录
innobackupex --user=root --password=123 /backup/full

#3、查看：默认会在备份目录下生成一个以时间戳命名的文件夹
[root@localhost ~]# cd /backup/full/
[root@localhost full]# ls
2021-07-16_16-09-47
[root@localhost full]# ls 2021-07-16_16-09-47/ #备份目录
。。。
[root@localhost full]# ls /var/lib/mysql # 数据目录
。。。

# 4、去掉时间戳，让备份数据直接放在备份目录下
我们在写备份脚本和恢复脚本，恢复的时候必须指定上一次备份的目录，如果备份目录带着时间戳，该时间戳我们很难在脚本中确定，无为了让脚本编写更加方便，我们可以使用选项--no-timestamp去掉时间戳，让备份内容直接放置于我们指定的目录下（ps：金融公司喜欢每天全备，每小时增备，如果备份目录带着时间戳，看似合理，但确实会很让头疼）
[root@localhost full]# rm -rf 2021-07-16_17-45-53/
[root@localhost full]# innobackupex --user=root --password=123 --no-timestamp /backup/full

# 补充：关于备份目录下新增的文件说明，可用cat命令查看
xtrabackup_checkpoints 存储系统版本号，增备的时候会用到
xtrabackup_info 存储UUID，数据库是由自己的UUID的，如果相同，做主从会有问题
xtrabackup_logfile 就是redo
```

#### （5）Xtrabackup增量备份

```bash
#一 基于上一次备份进行增量,参数说明:
--incremental：开启增量备份功能
--incremental-basedir：上一次备份的路径
	
#二 加上上一次命令
innobackupex --user=root --password=123 --no-timestamp --incremental --incremental-basedir=/backup/full/ /backup/xtra
	
#三 判断数据备份是否衔接
cat /backup/full/xtrabackup_checkpoints
    backup_type = full-backuped
    from_lsn = 0
    to_lsn = 1808756
    last_lsn = 1808756
    compact = 0
    recover_binlog_info = 0
    flushed_lsn = 1808756
	
cat /backup/xtra/xtrabackup_checkpoints 
    backup_type = incremental
    from_lsn = 1808756  # 值应该与全被的to_lsn一致
    to_lsn = 1808756
    last_lsn = 1808756
    compact = 0
    recover_binlog_info = 0
    flushed_lsn = 1808756
```

更多参数详见：https://www.cnblogs.com/linhaifeng/articles/15021166.html

#### （6）企业实战：Xtrabackup + Binlog恢复

mysql配置文件：数据目录与binlog放在不同的文件夹下

```bash
[mysqld]
datadir=/var/lib/mysql
default-storage-engine=innodb
innodb_file_per_table=1
server_id=1
log-bin=/data/binlog/mybinlog  
binlog_format='row' #(row,statement,mixed)    
binlog_rows_query_log_events=on
max_binlog_size=100M
```

为binlog日志创建目录

```bash
mkdir -p /data/binlog/
chown -R mysql.mysql /data/
```

启动mysql

```bash
systemctl restart mysql
```

模拟数据

```bahs
create database full charset utf8mb4;
use full;
create table t1 (id int);
insert into t1 values(1),(2),(3);
commit;
```

进行周日的全备

```bash
# 1、事先创建好备份目录
[root@db01 backup]# rm -rf /backup 
[root@db01 backup]# mkdir /backup   

# 2、全备
[root@db01 backup]# innobackupex --user=root --password=123 --no-timestamp  --parallel=5  /backup/full
```

模拟周一的数据变化

```bash
create database inc1 charset utf8mb4;
use inc1;
create table t1 (id int);
insert into t1 values(1),(2),(3);
commit;
```

进行周一的增量备份

```bash
innobackupex  --user=root --password=123 --no-timestamp --incremental --incremental-basedir=/backup/full /backup/inc1 
```

检查本次备份的LSN

```bash
[root@localhost backup]# cat /backup/full/xtrabackup_checkpoints 
backup_type = full-backuped
from_lsn = 0
to_lsn = 1817002
last_lsn = 1817002
compact = 0
recover_binlog_info = 0
flushed_lsn = 1817002
[root@localhost backup]# cat /backup/inc1/xtrabackup_checkpoints 
backup_type = incremental
from_lsn = 1817002
to_lsn = 1825905
last_lsn = 1825905
compact = 0
recover_binlog_info = 0
flushed_lsn = 1825905
[root@localhost backup]# 
```

模拟周二数据变化

```bash
create database inc2 charset utf8mb4;
use inc2;
create table t1 (id int);
insert into t1 values(1),(2),(3);
commit;
```

周二的增量

```bash
innobackupex   --user=root --password=123 --no-timestamp --incremental --incremental-basedir=/backup/inc1 /backup/inc2 
```

周三的数据变化

```bash
create database inc3 charset utf8mb4;
use inc3;
create table t1 (id int);
insert into t1 values(1),(2),(3);
commit;
```

模拟上午10点数据库崩溃

```bash
systemctl stop mysql # pkill -9 mysqld
\rm -rf /var/lib/mysql/*
```

恢复思路

```bash
1. 停业务,挂维护页
2. 查找可用备份并处理备份:full+inc1+inc2 
3. 找到binlog中: inc2 到 故障时间点的binlog
4. 恢复全备+增量+binlog
5. 验证数据
6. 起业务,撤维护页
```

恢复前的准备
[rml_read_more]：

```bash
所有增量必须要按顺序合并到全备当中才能用于恢复

#(1) 整理full，--use-memory越大效率越高，但是不要超过内存大小，超过则报错
innobackupex --apply-log --use-memory=3G --redo-only  /backup/full

--apply-log：该选项表示同xtrabackup的--prepare参数,一般情况下,在备份完成后，数据尚且不能用于恢复操作，因为备份的数据中可能会包含尚未提交的事务或已经提交但尚未同步至数据文件中的事务。因此，此时数据 文件仍处理不一致状态。--apply-log的作用是通过回滚未提交的事务及同步已经提交的事务至数据文件使数据文件处于一致性状态。

#(2) 合并inc1到full,并整理备份
innobackupex --apply-log --use-memory=3G --redo-only  --incremental-dir=/backup/inc1 /backup/full 

#(3) 合并后对比inc1与full的LSN号:last_lsn保持一致
cat /backup/full/xtrabackup_checkpoints 
cat /backup/inc1/xtrabackup_checkpoints 

#(4) 合并inc2到full,并整理备份 (合并最后一个增量备份时不要加--redo-only)
innobackupex --apply-log --use-memory=3G --incremental-dir=/backup/inc2 /backup/full 

#(5) 合并后对比inc2与full的LSN号:last_lsn保持一致
cat /backup/full/xtrabackup_checkpoints 
cat /backup/inc2/xtrabackup_checkpoints 

#(6) 最后一次整理ful
innobackupex --use-memory=3G --apply-log  /backup/full

#(7) 截取二进制日志
# 起点
cat /backup/inc2/xtrabackup_binlog_info
输出内容如下
mysql-bin.000031    1997    aa648280-a6a6-11e9-949f-000c294a1b3b:1-17,
e16db3fd-a6e8-11e9-aee9-000c294a1b3b:1-9

# 终点:
mysqlbinlog /data/binlog/mysql-bin.000031 |grep 'SET'

SET @@SESSION.GTID_NEXT= 'e16db3fd-a6e8-11e9-aee9-000c294a1b3b:12'/*!*/;

# 导出：
mysqlbinlog --skip-gtids --include-gtids='e16db3fd-a6e8-11e9-aee9-000c294a1b3b:10-12' /data/binlog/mysql-bin.000031>/backup/binlog.sql

或：
mysqlbinlog /data/binlog/mybinlog.000003  --start-position=1648 > /backup/binlog.sql恢复备份的数据
cp -a  /backup/full/* /var/lib/mysql
chown -R mysql.mysql /var/lib/mysql
systemctl start mysql
mysql -uroot -p123
> set sql_log_bin=0;
> source /backup/binlog.sql
```

验证

```bash
select * from full.t1;
select * from inc1.t1;
select * from inc2.t1;
select * from inc3.t1;
```

恢复

## 4. 自动备份脚本

### 4.1 备份计划

```bash
1. 什么时间  2:00
2. 对哪些数据库备份
3. 备份文件放的位置
```

### 4.2 备份脚本

```bash
备份脚本：
[root@jason ~]# vim /mysql_back.sh
#!/bin/bash
back_dir=/backup
back_file=`date +%F`_all.sql
user=root
pass=123

if [ ! -d /backup ];then
        mkdir -p /backup
fi

# 备份并截断日志
mysqldump -u${user} -p${pass} --events -R --triggers --master-data=2 --single-transaction --all-databases > ${back_dir}/${back_file}

mysql -u${user} -p${pass} -e 'flush logs'

# 只保留最近一周的备份
cd $back_dir
find . -mtime +7 -exec rm -rf {} \;
```

### 4.3 手动测试

```bash
手动测试：
chmod a+x /mysql_back.sh
chattr +i /mysql_back.sh
bash /mysql_back.sh
```

### 4.4 配置计划任务

```bash
配置cron：
[root@jason ~]# crontab -l
0 2 * * * /mysql_back.sh
```

## 5. 企业案例

### 5.1 背景

```bash
1.正在运行的网站系统，MySQL数据库，数据量25G，日业务增量10-15M。

2.备份策略：每天23：00，计划任务调用mysqldump执行全备脚本

3.故障时间点：上午10点开发人员误删除一个核心业务表，如何恢复？
```

### 5.2 处理故障思路

```bash
1.停业务避免数据的二次伤害
2.找一个临时的库，恢复前一天的全备
3.截取前一天23：00到第二天10点误删除之间的binlog，恢复到临时库
4.测试可用性和完整性
5.开启业务前的两种方式
	1）直接使用临时库顶替原生产库，前端应用割接到新
	2）将误删除的表单独导出，然后导入到原生产环境
6.对外开放业务
```

### 5.3 故障模拟

#### 1）准备初始数据

```bash
#刷新binlog使内容更清晰
flush logs;
#查看当前使用的binlog
show master status;

#准备测试库与数据
create database dbtest;
use dbtest;
create table t1(id int,name varchar(16));
insert t1 values
(1,"jason1"),
(2,"jason2"),
(3,"jason3");

create table t2 select * from t1;
```

#### 2）全备

```bash
[root@db01 ~]# mkdir /backup
[root@db01 ~]# mysqldump -uroot -pEgon@123 -A -R --triggers --master-data=2 --single-transaction |gzip > /backup/full.sql.gz  # 通常备份文件应该带时间，此处略
```

#### 3）模拟23:00到10:00的操作

```bash
use dbtest;
create table t3 select * from t1;
select * from t3;
update t1 set name="EGON" where id=2;
delete from t2 where id>2;
```

#### 4）模拟10：00删库操作

```bash
#删库、跑路
drop database dbtest;
```

### 5.4 恢复数据

#### 1）先停生产库,避免数据二次伤害

```bash
[root@db01 ~]# systemctl stop mysql
```

#### 2）准备新库，在新库中完成数据恢复操作后再更新给生成库

#### 3）通过binlog找到23:00到第二天10:00之间新增的数据

```bash
#1.找到结束位置点：
mysql> show master status;
mysql> show binlog events in 'mybinlog.000002';
[root@localhost backup]# cd /var/lib/mysql
[root@localhost mysql]# mysqlbinlog --base64-output=decode-rows -vvv --start-datetime="2021-07-16 02:00:00" mybinlog.000002 

3.取出位置点之间新增的数据
[root@db01 ~]# mysqlbinlog --start-position=694 --stop-position=1249 mybinlog.000002 > /backup/xin.sql 
```

#### 4）将前一天的全备数据和新增的数据拷贝到新数据库

```bash
scp /backup/full.sql.gz  172.16.1.52:/tmp/  
scp /backup/xin.sql  172.16.1.52:/tmp/
```

#### 5）将前一天的全备与增量恢复到新库

```bash
mysql> set sql_log_bin=0;
mysql> system zcat /tmp/full.sql.gz | mysql -uroot -pEgon@123

mysql> source /tmp/xin.sql;
```

#### 6）查看表和数据验证数据完整

```bash
mysql> use dbtest;
mysql> show tables;
mysql> select * from t1;
mysql> select * from t2;
mysql> select * from t3;
```

#### 7）恢复生产环境提供服务

```bash
1.将恢复的表导出，导入到生产库（如果核心业务表很小）
	1）导出指定表
		[root@db02 mysql]# mysqldump dbtest t1 t2 t3 > /tmp/test.sql
	2）将sql传输到生产库
		[root@db02 mysql]# scp /tmp/test.sql 172.16.1.51:/tmp/
	3）指定库导入表
		[root@db01 data]# mysql backup < /tmp/test.sql

2.应用服务修改数据库配置连接到新库（如果核心业务表很大）
```



# 7. 用户权限管理

## 1. 权限简介

  关于mysql的权限简单的理解就是mysql允许你做你全力以内的事情，不可以越界。比如只允许你执行select操作，那么你就不能执行update操作。只允许你从某台机器上连接mysql，那么你就不能从除那台机器以外的其他机器连接mysql。

  那么Mysql的权限是如何实现的呢？这就要说到mysql的两阶段验证，下面详细介绍：第一阶段：服务器首先会检查你是否允许连接。因为创建用户的时候会加上主机限制，可以限制成本地、某个IP、某个IP段、以及任何地方等，只允许你从配置的指定地方登陆。第二阶段：如果你能连接，Mysql会检查你发出的每个请求，看你是否有足够的权限实施它。比如你要更新某个表、或者查询某个表，Mysql会查看你对哪个表或者某个列是否有权限。再比如，你要运行某个存储过程，Mysql会检查你对存储过程是否有执行权限等。

| **权限**                | **权限级别**           | **权限说明**                                                 |
| ----------------------- | ---------------------- | ------------------------------------------------------------ |
| CREATE                  | 数据库、表或索引       | 创建数据库、表或索引权限                                     |
| DROP                    | 数据库或表             | 删除数据库或表权限                                           |
| GRANT OPTION            | 数据库、表或保存的程序 | 赋予权限选项                                                 |
| REFERENCES              | 数据库或表             |                                                              |
| ALTER                   | 表                     | 更改表，比如添加字段、索引等                                 |
| DELETE                  | 表                     | 删除数据权限                                                 |
| INDEX                   | 表                     | 索引权限                                                     |
| INSERT                  | 表                     | 插入权限                                                     |
| SELECT                  | 表                     | 查询权限                                                     |
| UPDATE                  | 表                     | 更新权限                                                     |
| CREATE VIEW             | 视图                   | 创建视图权限                                                 |
| SHOW VIEW               | 视图                   | 查看视图权限                                                 |
| ALTER ROUTINE           | 存储过程               | 更改存储过程权限                                             |
| CREATE ROUTINE          | 存储过程               | 创建存储过程权限                                             |
| EXECUTE                 | 存储过程               | 执行存储过程权限                                             |
| FILE                    | 服务器主机上的文件访问 | 文件访问权限                                                 |
| CREATE TEMPORARY TABLES | 服务器管理             | 创建临时表权限                                               |
| LOCK TABLES             | 服务器管理             | 锁表权限                                                     |
| CREATE USER             | 服务器管理             | 创建用户权限                                                 |
| PROCESS                 | 服务器管理             | 查看进程权限                                                 |
| RELOAD                  | 服务器管理             | 执行flush-hosts, flush-logs, flush-privileges, flush-status, flush-tables, flush-threads, refresh, reload等命令的权限 |
| REPLICATION CLIENT      | 服务器管理             | 复制权限                                                     |
| REPLICATION SLAVE       | 服务器管理             | 复制权限                                                     |
| SHOW DATABASES          | 服务器管理             | 查看数据库权限                                               |
| SHUTDOWN                | 服务器管理             | 关闭数据库权限                                               |
| SUPER                   | 服务器管理             | 执行kill线程权限                                             |

  MYSQL的权限如何分布，就是针对表可以设置什么权限，针对列可以设置什么权限等等，这个可以从官方文档中的一个表来说明：

| 权限分布 | 可能的设置的权限                                             |
| -------- | ------------------------------------------------------------ |
| 表权限   | 'Select', 'Insert', 'Update', 'Delete', 'Create', 'Drop', 'Grant', 'References', 'Index', 'Alter' |
| 列权限   | 'Select', 'Insert', 'Update', 'References'                   |
| 过程权限 | 'Execute', 'Alter Routine', 'Grant'                          |

##  2.权限经验原则

  权限控制主要是出于安全因素，因此需要遵循一下几个经验原则：

> 1. 只授予能满足需要的最小权限，防止用户干坏事。比如用户只是需要查询，那就只给select权限就可以了，不要给用户赋予update、insert或者delete权限。
> 2. 创建用户的时候限制用户的登录主机，一般是限制成指定IP或者内网IP段。
> 3. 初始化数据库的时候删除没有密码的用户。安装完数据库的时候会自动创建一些用户，这些用户默认没有密码。
> 4. 为每个用户设置满足密码复杂度的密码。
> 5. 定期清理不需要的用户，回收权限或者删除用户。

## 3. 权限操作

###   1. GRANT

  先来看一个例子，创建一个只允许从本地登录的超级用户jack，并允许将权限赋予别的用户，密码为：jack.

```SQL
mysql> grant all privileges on *.* to jack@'localhost' identified by "jack" with grant option;
```

  GRANT命令说明：
  ALL PRIVILEGES 是表示所有权限，你也可以使用select、update等权限。

  ON 用来指定权限针对哪些库和表。

  *.* 中前面的*号用来指定数据库名，后面的*号用来指定表名。

  TO 表示将权限赋予某个用户。

  [jack@'localhost'](mailto:jack@'localhost') 表示jack用户，@后面接限制的主机，可以是IP、IP段、域名以及%，%表示任何地方。注意：这里%有的版本不包括本地，以前碰到过给某个用户设置了%允许任何地方登录，但是在本地登录不了，这个和版本有关系，遇到这个问题再加一个localhost的用户就可以了。

  IDENTIFIED BY 指定用户的登录密码。

  WITH GRANT OPTION 这个选项表示该用户可以将自己拥有的权限授权给别人。注意：经常有人在创建操作用户的时候不指定WITH GRANT OPTION选项导致后来该用户不能使用GRANT命令创建用户或者给其它用户授权。

备注：可以使用GRANT重复给用户添加权限，权限叠加，比如你先给用户添加一个select权限，然后又给用户添加一个insert权限，那么该用户就同时拥有了select和insert权限。

###   2.  刷新权限

  使用这个命令使权限生效，尤其是你对那些权限表user、db、host等做了update或者delete更新的时候。以前遇到过使用grant后权限没有更新的情况，只要对权限做了更改就使用FLUSH PRIVILEGES命令来刷新权限。

```SQL
mysql> flush privileges;
```

###   3. 查看权限

```SQL
# 查看当前用户的权限：
mysql> show grants;
+-------------------------------------------------------------+
| Grants for root@localhost                                   |
+-------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
| GRANT PROXY ON ''@'' TO 'root'@'localhost' WITH GRANT OPTION|
+-------------------------------------------------------------+


# 查看某个用户的权限：
mysql> show grants for 'jack'@'%';
+-------------------------------------------------------------+
| Grants for jack@% 										  |
+-------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'jack'@'%' IDENTIFIED BY PASSWORD '*9BCDC990E611B8D852EFAF1E3919AB6AC8C8A9F0' |
+-------------------------------------------------------------+
1 row in set (0.00 sec)
```

###  4. 回收权限

```SQL
mysql> revoke delete on *.* from 'jack'@'localhost';
```

###  5. 删除用户

```SQL
mysql> select host,user,password from user;
+-----------+------+-------------------------------------------+
| host      | user | password                                  |
+-----------+------+-------------------------------------------+
| localhost | root |                                           |
| rhel5.4   | root |                                           |
| 127.0.0.1 | root |                                           |
| ::1       | root |                                           |
| localhost |      |                                           |
| rhel5.4   |      |                                           |
| localhost | jack | *9BCDC990E611B8D852EFAF1E3919AB6AC8C8A9F0 |
+-----------+------+-------------------------------------------+

mysql> drop user 'jack'@'localhost';
```

### 6. 对账户重命名

```SQL
mysql> rename user 'jack'@'%' to 'jim'@'%';
```

### 7. 修改密码

```SQL
# 1、用set password命令
mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123456');

# 2、用mysqladmin
  [root@rhel5 ~]# mysqladmin -uroot -p123456 password 1234abcd
#  格式：mysqladmin -u用户名 -p旧密码 password 新密码

# 3、用update直接编辑user表
mysql> use mysql

mysql> update user set PASSWORD = PASSWORD('1234abcd') where user = 'root';

mysql> flush privileges;

# 4、在丢失root密码的时候：
[root@rhel5 ~]# mysqld_safe --skip-grant-tables &
[1] 15953
[root@rhel5 ~]# 130911 09:35:33 mysqld_safe Logging to '/mysql/mysql5.5/data/rhel5.4.err'.
130911 09:35:33 mysqld_safe Starting mysqld daemon with databases from /mysql/mysql5.5/data

[root@rhel5 ~]# mysql -u root
mysql> \s
...

mysql> use mysql
...

mysql> update user set password = PASSWORD('123456') where user = 'root';
...

mysql> flush privileges;
```

## 4. 数据库维护与升级

> 关于数据库的维护与升级，此处不作详细展开。

## 5. 权限相关技术

> 使用证书管理工具对数据库进行加密防护。



# 8. SQL语言编程

## 1. Select

> Select选择语句，可以从对应的表中提取所需要的数据记录，也可以用于简单的显示信息。其基本语法如下：

```sql
Select Table.Columns As Alias
From Table
Where Condition
Group by
Order by
...;
```

> + 若需要全选列，则可使用‘`*`’代替；
> + 筛选的列仅表示为返回值，条件处的数据只需要在表中而无需筛选出来；
> + Columns As Alias表示引入列Columns并用别名表示，同时若表只有一张或者该属性只有一张表有，可省略`Table.`，连续多列可通过`Table.column1, columns2...`来实现；
> + `Condition`多条件可通过`and`连接；
> + 唯一化采用参数 `DISTINCT` （位于SELECT后表前）；

## 2. Join 连接

join 连接支持的基本语法如下：

```sql
Table_reference [Inner | Cross] Join table_factor [join condition]
```

其中`table_reference` 指定了要连接的表，`On condition`指定连接条件，同时连接包括三类：

> + `Inner join`:     内连接，默认值，取得两个表中完全匹配的记录；
> + `Left join`:       左连接，外连接，取左表完全记录，即左表有而右表没有的；
> + `Right join`:     右连接，外连接，取右表完全记录。

如果要指定连接的表中的列名相同，则可以通过`Using` 或者`Natural Join`

```sql
Select name From table Join name2 Using(columns);
Select name From table Natural Join name2;
```

## 3. 模式匹配

MySQL提供标准的SQL模式匹配(Like)，也支持基于 Unix的正则表达式匹配 (regexp)。

### 3.1 Like

LIKE匹配可以使用特殊字符 ‘`_`’ 和 “`%`”进行模糊查询，其中前者代表RYE一个字符，后者代表任意多个字符。通常情况下，LIKE拥有更高的匹配效率。

同时，若匹配内容中出现了特殊字符，则可通过EXCAPE定义转义符，如下：

```SQL
'$_%' ESCAPE '$'
```



### 3.2 Regexp

> 正则表达式定义了一个字符串的规则，是定义复杂查询的一个强有力的工具。MySQL中使用REGEXP操作符来进行正则表达式的匹配。REGEXP操作符不是SQL标准，但是具有强大的功能，能实现比LIKE复杂很多的匹配。下表提供了一些基本的用法，由于该方法属于通用方法，在python、matlab等语言中都有使用，此处不展开介绍。

| PATTERN | DESCRIPTION                |
| ------- | -------------------------- |
| ^       | 开头匹配                   |
| $       | 结尾匹配                   |
| .       | 任意字符                   |
| []      | 包括，某一字符的可能性集合 |
| [^]     | 不包括，某一字符的排除集合 |
| \|      | 或                         |
| *       | 任意次数                   |
| +       | 一次及以上                 |
| ?       | 零次或一次                 |
| {N, M}  | N次到M次                   |

> **值得注意的是，此处的次数指字符的次数，而汉字占用两个字符位。**

## 4. 子查询

当一个查询是另一个查询的条件时，称之为子查询。子查询可以使用几个简单的命令构成复杂的命令，子查询会返回一个标量或者数据组，常用的命令包括：

| Command | Description                 |
| ------- | --------------------------- |
| In      | 包括于                      |
| Any     | 子查询任意值                |
| All     | 子查询全体值                |
| Some    | 子查询部分值                |
| Exists  | 子查询是否为空，是返回False |

