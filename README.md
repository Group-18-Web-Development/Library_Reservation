# Library-Reservation
## 开发目标：
图书馆线上占座系统（线上预约图书馆座位。目的：目前图书馆空座率较高，且常常出现一人多座的情况，为了提高图书馆的利用效率，建立完善的图书馆座位预约系统是十分必要的。主要功能：座位查询与预约等。） 

## 软件用户类别： 
普通学生、管理员（包括系统、座位等）

## 功能清单： 
### 学生： 
1.	查看：按时间段查看座位剩余情况；按座位查看可预约时间段
2.	预约：可选择阅览室，进一步预约座位（暂定为可手动选择，亦可由系统自动生成）
3.	取消：取消预约
4.	账号管理：包括注册、登录、姓名、学号、历史记录、修改用户信息（绑定邮箱）
### 管理员：
1.	查看座位信息、座位管理：修改座位使用情况（整体和个体）
2.	查看学生信息：每个人的个人信息只能被自己和管理员查看
3.	学生管理：暂定
### 系统：
1.	展示座位情况
2.	预约用户签离管理
### 座位：
当前以及预约时间段的座位情况（空闲、已被预约、正在使用）
## 功能依赖关系：
座位情况显示->查看->预约->取消
## 后续扩展功能（待定）：
1.	座位属性例如有无电源等
2.	学生信誉系统评估
3.	添加邮件提醒功能

Django 3.0.5  
数据库 sqlite 




###已提交
lzh——test

顾晓然

CHS提交测试
