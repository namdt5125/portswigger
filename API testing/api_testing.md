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

![image](https://github.com/user-attachments/assets/d9401c53-2110-4395-9683-dfaed60ea0a4)

Đăng nhập xong với wiener và ném vào giỏ hàng, tôi thấy là không có đủ tiền để mua, giờ tôi nghĩ có 2 trường hợp, 1 là làm sao đó credit của mình lên bằng giá tiền hoặc làm giá tiền bằng 0

![image](https://github.com/user-attachments/assets/3d763282-06a1-4ce3-822d-1f4f37840e3b)

Đây là json của cái hàng đây thông qua /api/products/1/price

![image](https://github.com/user-attachments/assets/48fb08b2-47a9-4e87-91b1-808cbbce2e75)

Tôi thử ghi đè cho giá về 0 mà không thấy được:

![image](https://github.com/user-attachments/assets/721bb1a6-67f9-4a2b-a84d-9d076c2069f3)

Tôi thử đổi qua method POST thì nó chỉ cho PATCH hoặc GET qua, mà PATCH là liên quan đến sửa đổi nên tôi đổi sang PATCH và hiện ra Unauthorized

![image](https://github.com/user-attachments/assets/3f9f907d-d89b-4c8b-a259-a281b6b5e9dd)

![image](https://github.com/user-attachments/assets/3e71b105-c5c0-4f76-8b87-d9d7e2eeb420)

Sau 1 lúc, quay ra quay vào thì nó lại vào được, hình như do tôi nghịch cái đăng nhập nên cái session hết hạn:

![image](https://github.com/user-attachments/assets/bd8c88ef-6e84-4f05-a7a7-ab392c267a38)

Nhìn cái kết quả trả về thì nó đòi Content-Type thành application/json:

![image](https://github.com/user-attachments/assets/9d5e584c-e125-44fc-a250-57d43ca3eb8f)

Quay lại vào phần Lightweight "l33t" Leather Jacket và ném vào cart:

![image](https://github.com/user-attachments/assets/e3265006-6b4c-4f0b-a2ec-539ddd7170c2)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/6526f35c-7585-4a82-9fc4-bfd12562a051)

Có cái checkout là hiện ra thông tin về cái giá tiền các thứ 

![image](https://github.com/user-attachments/assets/d6b984f5-12fa-4a7d-a533-e30d17b0bd5b)

Tôi thử này nhưng không được:

![image](https://github.com/user-attachments/assets/6fe8706d-0cde-452c-b401-ca9cb8ce98b3)

Tôi thấy còn 1 cái api/checkout nữa:

![image](https://github.com/user-attachments/assets/e668f99e-016f-4992-8aaf-ca955d1750f9)

Tôi đổi price về 0 nhưng không có được:

![image](https://github.com/user-attachments/assets/c38f2c32-6aa6-4a8f-97fb-17c0db9d69fe)

Tôi để ý khi thay đổi percentage thành 999 thì nó báo lỗi, có vẻ đổi thành 100 sẽ hoạt động:

![image](https://github.com/user-attachments/assets/3bf80362-84aa-4e0f-a644-505819b82b72)

![image](https://github.com/user-attachments/assets/84136261-f4f0-4fb4-9e5b-40edd5f783b2)
















































