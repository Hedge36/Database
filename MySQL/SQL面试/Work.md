## 题目(30min)

### 题目描述

> 公司现在有两张表，按照需求计算相关字段。table1——司机订单表order，字段有（driver_id‘司机编号’, order_id’订单编号’，order_amt‘订单金额’ , order_date ‘接单日期’）。table2——司机画像表driver_label，字段有（driver_id‘司机编号’, age‘司机年龄’,city‘司机城市’）

### 数据结构

表1——司机订单表order

| 字段       | 意义     | 属性 |
| ---------- | -------- | ---- |
| driver_id  | 司机编号 |      |
| order_id   | 订单编号 |      |
| order_amt  | 订单金额 |      |
| order_date | 接单日期 |      |

表2——司机画像表driver_label

| 字段      | 意义     | 属性 |
| --------- | -------- | ---- |
| driver_id | 司机编号 |      |
| age       | 司机年龄 |      |
| city      | 城市     |      |

## 问题

> **Q1：**统计各个城市每个司机2021年11月1号的订单总金额，订单总数，并按照城市进行降序排序。
>
> 
>
> **Q2：**假如今天是2021年10月20号请用一个sql统计出2021年10月1号到20号的司机数，日均单量，以及近７日的司机数和司机日均单量。
>
> 
>
> **Q3：**取出司机城市是北京，同时2021年10月1号到10月30号司机30日日均总金额超过100的司机数（假设司机每天订单不限）。
>
> 
>
> **Q4：**取出司机年龄在30-50岁，在2021年11月1号当天司机完单量在全国排名第50的司机ID。
>



## 作答

### 1

乱七八糟hhhh

```SQL
select count(order.'订单编号') as 各司机订单数, sum(order.'订单金额') as 订单总金额, order.'接单日期', order.'司机编号',driver_label.'司机编号' ,driver_label.'司机城市',
from driver_label
left join order
on order.'司机编号' = driver_label.'司机编号'
where order.'接单日期' == '2021.11.1'
order by driver_label.'司机城市' desec
```

### 2

```SQL
Select Count(driver_id), Count(order_id)/20, 
From order 
Join driver_label
on driver_id
Where order_date Between '2021-10-01' And '2021-10-20'
Group By order_date
Union 
Select Count(driver_id), Count(order_id)/7, 
From order 
Join driver_label
on driver_id
Where order_date Between '2021-10-14' And '2021-10-20'
Group By order_date
```



### 3

```SQL
Select Count(*)
From driver_label
Join order On driver_id
Where city='北京'
A order_date Between '2021-10-01' And '2021-10-30'
And Avg(order_amt) > 100
Group By order_date
```

### 4

```SQL
Select driver_id
From driver_label 
Where age Between 30 And 50
Union 
Select driver_id
From 
	(Select top 50 driver_id, Count(order) As total
	 From order
     Where Not in 
     	(Select top 49 driver_id, Count(order) As total
	 	From order
        Where order_date='2021-11-01'
     	Group By total
        )
     Group By total
     )

```

