![image](https://github.com/user-attachments/assets/0f90b5c0-cc53-4adb-939f-b59d104e70bf)

Đây là giao diện sau khi đăng nhập bằng wiener:peter 

![image](https://github.com/user-attachments/assets/944abff0-fd2d-4b9f-a3c8-5af4e40e332e)

Khi tôi cố tình truy cập vào /admin thì nó chặn lại và không cho

![image](https://github.com/user-attachments/assets/b9db5c3b-4dd3-47fc-9be9-eb091e414013)

Bây giờ thì tôi sẽ đi lượn qua history xem có gì không 

![image](https://github.com/user-attachments/assets/05930bd5-f958-4509-87fc-ad4524e86481)

Mấy cái được highlight màu xanh lá là của extension jwt editor

![image](https://github.com/user-attachments/assets/7628ee77-3ea4-4511-8dc2-cf678d373773)

Dịch cái jwt ra thì tôi thấy đây là user wiener

![image](https://github.com/user-attachments/assets/f48789f7-a5c4-41cd-997e-e4e6002b39ea)

Tôi ném vào repeater và sửa lại thành administrator để vào thử 

![image](https://github.com/user-attachments/assets/871f5f31-b229-4727-965d-55c18e9e89ec)

Và hiện ra giao diện của admin, xóa user là xong 

![image](https://github.com/user-attachments/assets/2740e8ed-52ec-4c16-acbc-d8620f1d2fd5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e724e22f-7207-461e-9ad0-782cc2d52d4c)

![image](https://github.com/user-attachments/assets/d1ccb581-667c-41f7-b2e9-0c2e3643c7c0)

Tôi làm y hệt bài trước nhưng bài này bắt phải login cơ

![image](https://github.com/user-attachments/assets/7d6c643c-c64c-4f41-b4d2-0afc9338a95f)

Tôi thử intercept cơ mà cái này có csrf nên không làm gì được, 

![image](https://github.com/user-attachments/assets/47fa0437-0a10-4233-8194-da13912ac8c6)

Sau 1 lúc lay hoay thì tôi đọc lại đề bài, nó bảo là bypass via flawed signature verification, mà cái signature được mã hóa bằng RS256 ở cuối của jwt, ở cái đoạn đầu có ghi, tôi search google và đổi sang none rồi gửi xem nó như thế nào:

![image](https://github.com/user-attachments/assets/b7ee71d5-f793-485a-bd7f-f13dcea8a9e6)

![image](https://github.com/user-attachments/assets/b919feb6-7f29-4ae5-b3fc-c9afbbd77bf7)

Và xóa cả đoạn sau nữa, vì đoạn sau được mã hóa RS256, nó là cái chữ kí, nếu thuận toán là none thì đút thêm cái mã hóa vào làm gì, thế nên xóa từ dấu . trở đi

![image](https://github.com/user-attachments/assets/d90101ce-0562-4d78-8713-ceafd7308af6)

![image](https://github.com/user-attachments/assets/6333c73e-f1c7-419d-a066-a55341c00ab3)




































































































