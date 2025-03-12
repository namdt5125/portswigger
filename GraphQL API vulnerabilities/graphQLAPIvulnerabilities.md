![image](https://github.com/user-attachments/assets/61a44a82-60f8-4d7d-bc4d-919e7c05a8d2)

Đây là giao diện của trang web:

![image](https://github.com/user-attachments/assets/f3e9f9a8-8106-4623-b070-923ec5b090d3)

Đây là cái req của graphql:

![image](https://github.com/user-attachments/assets/e2c19e35-dca3-4ad0-9772-ea48faa0aa71)

Đây là GraphQL:

![image](https://github.com/user-attachments/assets/b4ae0033-94e7-44f5-830e-b33ae11fa4a8)

Tôi sửa thành `{"query": "{__schema{queryType{name}}}"}` và ấn gửi thì ra cái này:

![image](https://github.com/user-attachments/assets/00f77dcc-5e33-4b71-8fb9-507526b353fa)

Tôi chèn cái [Full introspection query](https://gist.github.com/franzejr/d0a178286d0e23d3ed50999288806068) vào GraphQL và ra cái này:

![image](https://github.com/user-attachments/assets/49859ddf-3ef0-425a-b4e4-67498b2a9fbb)

Tôi chuyển sang raw và paste vào trong [GraphQL Visualizer](https://nathanrandal.com/graphql-visualizer/):

![image](https://github.com/user-attachments/assets/53c0b49d-0a75-4bf3-8da0-eb7bf27c64f2)

![image](https://github.com/user-attachments/assets/11f1ab63-0d5e-4644-b583-0d1f0d953a36)

Cho vào đây để dễ nhìn hơn thay vì đọc từng cái 1 và có xuất hiện cái postPassword thuộc kiểu string, tôi thêm cái postPassword vào GraphQL nhưng kết quả trả lại là NULL:

![image](https://github.com/user-attachments/assets/0511d91b-aaf8-45ad-acb3-069b17c9e31c)

Nếu để ý mấy cái id trả về thì không có id là 3, tôi ấn bừa 1 bài post, lấy req và thay đổi id thành 3

![image](https://github.com/user-attachments/assets/d1caf60e-43f4-450e-9c32-e69db05e772f)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9bc7ae96-ee63-40d1-ac4e-40c3b4f803a5)

Khi tôi thử tính năng log in với cred là admin:admin kết quả trả về là json

![image](https://github.com/user-attachments/assets/e765cd4c-c419-487d-aabe-2c766a6c5089)

Thêm cái extension InQL vào và bấm analyze thì ra cái này:

![image](https://github.com/user-attachments/assets/002634d2-025d-4f94-acd9-e58437d2307a)

Và ở đây có getUser là lấy username và password dựa trên id của user:

![image](https://github.com/user-attachments/assets/cd9349b2-ba7a-4a78-a5f2-3a25e10519e9)

Vào trong repeater và sửa thành getUser, id=1:

![image](https://github.com/user-attachments/assets/2713b635-082c-4140-8db3-b4c08e2d9f99)

![image](https://github.com/user-attachments/assets/cd950ab2-85b0-4c91-8d91-fed4caeaafb1)

<h1>---------------------------------------------------------</h1>
<br>








