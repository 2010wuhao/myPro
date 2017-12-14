## 请求接口

### 1、请求天气接口：

#### HTTP Method：
GET

#### URI： 

http://[hostname]/weather/api/v1.0/get_weather

#### Parameter:

名称	|类型	|是否必须	|描述
---|---|---|---
city|	STRING	|可选	|城市名称，比如：海淀区
citycode|	STRING|	可选|城市天气代号
location|	STRING|	可选|	经纬度 纬度在前，,分割 如：39.983424,116.322987

city,location,citycode三者任选其一。

#### 返回：
成功则返回对应天气json。失败则返回错误码

错误码 | 错误信息 | 描述
---|---|---
201	|City and city ID and city code are empty|城市和城市ID和城市代号都为空
202	|City does not exist	|城市不存在
203	|There is no weather information in this city	|此城市没有天气信息
210	|No information	|没有信息

### 2、请求城市列表：

#### HTTP Method：
GET

#### URI： 

http://[hostname]/weather/api/v1.0/get_citylist

#### parameter

无

#### 返回：

返回城市列表或者空数据

## 数据库

