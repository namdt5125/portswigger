![image](https://github.com/user-attachments/assets/fb6f8ffc-1365-40f1-81dc-4c0afae9e23a)

Giao diện khi đăng nhập với wiener:

![image](https://github.com/user-attachments/assets/4c1deb96-a30f-4ba6-b3fc-dee96659a8f7)

Vào /api theo lý thuyết sách giáo khoa thì đây:

![image](https://github.com/user-attachments/assets/c325949b-3de2-4af3-88d5-6c04b239388f)

Xóa carlos là xong:

![image](https://github.com/user-attachments/assets/db103101-124c-4f35-9b89-c96574744691)

![image](https://github.com/user-attachments/assets/bf930a5a-1b49-41f6-a35f-32c736b8cbb5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/14d9e09c-037b-4670-9f51-6e7f2de0fb04)

Tôi không biết mật khẩu nên bấm bừa vào forgot password 

![image](https://github.com/user-attachments/assets/0f349ce0-fc94-4ac5-9b2d-12f079ae98d6)

Khi username sai thì sẽ hiện ra `{"type":"ClientError","code":400,"error":"Invalid username."}` 

![image](https://github.com/user-attachments/assets/6b438666-c0ae-40c6-bd10-8644106f0fbe)

Thêm bừa 1 cái tham số `%26a=b` thì hiện ra `{"error": "Parameter is not supported."}` cái này còn có ý nghĩa là máy chủ xử lý như một tham số riêng biệt 

![image](https://github.com/user-attachments/assets/dc023cb7-98dc-4fb4-afce-f09689c5f5b3)

Khi thêm %23 tức là # vào thì nó bị mất tham số, tức là nó nằm ở đoạn sau đấy, thêm cái field vào:

![image](https://github.com/user-attachments/assets/4df63e17-6fcb-4864-bb64-b5c328d1c856)

Truyền vào `username=administrator%26field=a%23`, toán tử & và kết thúc bằng # để xem còn tham số không thì có vẻ hết rồi 

![image](https://github.com/user-attachments/assets/0a701cff-03dc-483e-86ea-f4e9e7847d75)

Ném vào intruder để brute cái tên:

![image](https://github.com/user-attachments/assets/0f96c26a-27ca-4a5a-bd29-b31b27f57dfa)

Có mỗi username và email, tôi tưởng sẽ xuất hiện cái token trong đây:

![image](https://github.com/user-attachments/assets/a7b7740f-cd81-4d86-9a78-61abf60d309e)

Do không biết cái token nó dạng như nào, tôi mò mẫm 1 lúc thì mò ra được cái tên của token:

![image](https://github.com/user-attachments/assets/803eb987-c5ca-40d8-82e4-3c131ece4dc2)

Đổi thành `username=administrator%26field=reset_token%23` để lấy token:

![image](https://github.com/user-attachments/assets/31b9c346-360a-4990-9445-dd4c3b36aae1)

![image](https://github.com/user-attachments/assets/15286877-f204-4965-85b5-6f6a6420dc38)

<h1>---------------------------------------------------------</h1>
<br>












































































