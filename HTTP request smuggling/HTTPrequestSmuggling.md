HTTP Smuggling (HTTP Request Smuggling) là một kỹ thuật tấn công web trong đó kẻ tấn công lợi dụng sự không nhất quán trong cách các máy chủ web hoặc proxy xử lý tiêu đề HTTP 
(Content-Length, Transfer-Encoding, v.v.). Mục tiêu là gửi một yêu cầu HTTP được thiết kế đặc biệt để máy chủ xử lý sai, từ đó có thể bỏ qua tường lửa hoặc cơ chế bảo mật,
 tấn công request của người dùng khác (đánh cắp thông tin, chiếm phiên, thực hiện CSRF,...), kích hoạt lỗ hổng bảo mật trên ứng dụng web,...

![image](https://github.com/user-attachments/assets/e58891de-81bf-4276-bfa0-a5502125fe30)

Trong cái req này thì là http 2 và phải cho nó xuống 1.1 mới làm được bài này:

![image](https://github.com/user-attachments/assets/fad6ad0b-0d4e-400f-9e87-953ee1cbb2c6)

![image](https://github.com/user-attachments/assets/83f59e25-b128-4467-b39e-9d7e121744b0)

Tôi chuyển method sang POST và dùng thử cái payload trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Request%20Smuggling/README.md):

![image](https://github.com/user-attachments/assets/c8009207-e0f7-45f1-9e89-0f459bbe806d)

![image](https://github.com/user-attachments/assets/938e8979-8093-402f-8721-43e7ea303e88)

Sửa mỗi cái host, sửa req thì chạy vẫn trả về 200

![image](https://github.com/user-attachments/assets/8e53888c-0021-4688-bb9d-e8f76a0e4b96)

Sau đó tôi chèn thêm 1 cái req GET ở dưới và nó thành 404 not found:

![image](https://github.com/user-attachments/assets/29493e2c-455b-4e04-9b46-f47b4a6fd59e)

![image](https://github.com/user-attachments/assets/1010dcf7-b073-4eb7-a383-20442c0d5425)

<h1>---------------------------------------------------------</h1>
<br>
