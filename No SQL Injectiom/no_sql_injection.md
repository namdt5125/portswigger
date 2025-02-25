![image](https://github.com/user-attachments/assets/c854eb27-5071-4ef9-86b4-86e5a4844d4b)

![image](https://github.com/user-attachments/assets/9534d268-13df-4410-8869-a0fdc6ab7035)

Khi tôi đổi category thành dấu ' thì nó bị lỗi 

![image](https://github.com/user-attachments/assets/7deaacf8-cf6c-41c6-9f7d-2033be8d541d)

Khi dùng payload `Gifts'+'` thì có thể dễ thấy lỗi của nó 

![image](https://github.com/user-attachments/assets/e2080ecb-ee82-482d-9f81-659b536b0b52)

Dùng `Gifts'||1||'`, trong đó dấu ' là để đóng cái string lại và || 1 || trong JavaScript, toán tử || (OR) hoạt động như thường, do có số 1 nên cả cái này luôn đúng:

![image](https://github.com/user-attachments/assets/1a2600f3-56f1-49a8-bd27-cf8e9a3f00d7)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/01dd3297-eb28-4dd2-a32a-c9c54411e91c)

Để ý đến cái request login:

![image](https://github.com/user-attachments/assets/b04b5836-0be6-40c2-9465-09c40af8a421)

Tôi đổi cái username từ `"wiener"` thành `{"$ne":""}` thành và có thể login được. Trong MongoDB, $ne (Not Equal) là một toán tử so sánh, dùng để kiểm tra xem một giá trị không bằng giá trị nào đó, $ne: "" nghĩa là chỉ lấy những cái khác rỗng và hầu như đều hợp lệ
, thế nên là có thể đăng nhập được 

![image](https://github.com/user-attachments/assets/bae81d30-96ba-4da7-8843-be901f997d28)

Và tương tự mật khẩu cũng có thể đổi thành `{"$ne":""}` để login

![image](https://github.com/user-attachments/assets/e96cc37c-7bc2-42ed-ab2c-d99cfdbf38e8)

Dùng payload `{"$regex":"admin.*"}` ở username và `{"$ne":""}` ở password để đăng nhập vào với tài khoản bắt đầu bằng admin:

![image](https://github.com/user-attachments/assets/27f53af8-93bf-4b90-9404-f202aafc6125)

![image](https://github.com/user-attachments/assets/a2239487-8b1c-44b7-84c5-21c2a836d046)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/65576890-4176-4949-9de8-01f0694f63b9)

Để ý cái req lookup này, do nó in ra thông tin nên liên quan đến database

![image](https://github.com/user-attachments/assets/bb0bafcd-fb5e-4ef6-a617-a0d03a468f8b)

Tôi đổi thành `wiener'||1||'` thì ra thông tin admin 

![image](https://github.com/user-attachments/assets/3258c9b9-b8de-4977-8915-9ba705c3b740)

Trong trường hợp cả user và cái kia là 0 thì nó sẽ hiển thị `"message": "Could not find user"`

![image](https://github.com/user-attachments/assets/dea08022-daf9-40d3-a41c-8f87008dceaf)

Ném vào intruder để lấy mật khẩu với payload `abc'+||this.password[0]='a`

![image](https://github.com/user-attachments/assets/9aefeeb8-1588-4c9b-8195-77ff3e60a603)

![image](https://github.com/user-attachments/assets/7cbc78a6-538c-4828-ad50-800ee8381cfa)

Và tôi mò ra mật khẩu dài 8 kí tự 

![image](https://github.com/user-attachments/assets/4f3075f1-60be-4297-8206-2f22cef9b6be)


Mật khẩu là `fbvgtrqs`
<br>
Ngoài ra cũng có thể dùng && là `administrator' && this.password.length < 30 || 'a'=='b` thì cái này tốt hơn || kia do || lấy user đầu tiên của db và may mắn là admin nó ở đầu

![image](https://github.com/user-attachments/assets/9a566956-89d0-4100-a0ca-5c712f5d043a)

![image](https://github.com/user-attachments/assets/b6501ed7-e73d-41ed-97d0-48a063329b73)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/710dbf0a-0115-438d-9d21-1d275464b258)

Tôi bật intercept và đổi password thành `{"$ne":""}` để login

![image](https://github.com/user-attachments/assets/36ed51fd-2279-437b-85e5-ec5347f875da)

![image](https://github.com/user-attachments/assets/e99acfb8-09cd-4ff7-9f09-137c5b5173fb)

Khi dùng với carlos thì bị khóa, không vào được 

![image](https://github.com/user-attachments/assets/8030c8be-328c-4214-9522-b563196c0b09)

Tính năng quên mật khẩu thì lại cần email mà tôi không có cái đấy 

![image](https://github.com/user-attachments/assets/14b8b3e3-c709-4df0-ac40-d8f243b2281b)

Có vẻ tôi cần phải tìm token của carlos thì mới đổi được mật khẩu, dùng payload `{"username":"carlos","password":{"$ne":"invalid"}, "$where": "0"}` để test thử, $where là một toán tử trong MongoDB cho phép thực thi JavaScript trong truy vấn. Nó thường được dùng để viết các điều kiện phức tạp mà cú pháp MongoDB thông thường không hỗ trợ, nó có chức năng giống cái WHERE trong SQL ấy 

![image](https://github.com/user-attachments/assets/851bbf54-d4f5-48b2-83b7-63b61353b93c)

![image](https://github.com/user-attachments/assets/332e2fbe-d1f9-4505-8354-7916e65728f2)

Với `"$where":"0"` thì đại diện cho false và `"$where":"1"` là true, có được bật tắt rồi thì chắc là đi mò thôi, dùng payload `{"username":"carlos","password":{"$ne":""}, "$where":"Object.keys(this)[1].match('^.{1}a.*')"}` để tìm tên của trường thứ 2 

![image](https://github.com/user-attachments/assets/bf08bf59-5094-4a34-9b8f-4e7d1d1007e6)

Và có thể dễ thấy đây là trường username, tiếp tục tăng cái `Object.keys(this)[1]` thành `Object.keys(this)[2]` và ra được trường thứ 3 là password:

![image](https://github.com/user-attachments/assets/94ad4ca3-bd03-4acd-9c30-fcd03e3ff7fa)

Tiếp đó là trường thứ 4 là email:

![image](https://github.com/user-attachments/assets/db93fec5-8015-4430-95f5-11deb6138428)

Và cuối cùng cũng ra forgotPwd

![image](https://github.com/user-attachments/assets/d89af80d-b3c1-4795-985f-617197e09ea2)

Đổi payload thành `{"username":"carlos","password":{"$ne":""}, "$where":"this.forgotPwd.match('^.{1}a.*')"}` 

![image](https://github.com/user-attachments/assets/4c02acf8-7fe0-4263-8b4d-f49dfc1bc4b5)

![image](https://github.com/user-attachments/assets/214937d5-1e73-4f68-81c6-c92c48df82b9)

ra được ea2e50370207186a, ném vào cái req forgot password là `https://0a560042049dfa94809290e700300094.web-security-academy.net/forgot-password?forgotPwd=ea2e50370207186a`

![image](https://github.com/user-attachments/assets/9c2653ce-9d36-46fb-ae41-5f93a513008c)

![image](https://github.com/user-attachments/assets/7342fde0-a8b0-4266-82b5-f8782621a54e)







