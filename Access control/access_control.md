![image](https://github.com/user-attachments/assets/7148c292-427d-4648-be44-3ef286b1c8ee)

vào cái robots.txt có cái dir của admin 

![image](https://github.com/user-attachments/assets/b5cf07d5-6f48-4e6d-bdc2-19f02b3cc9d8)

![image](https://github.com/user-attachments/assets/dbfdef31-af5c-427b-acdc-77b9166609b8)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/73461095-2ca1-48bc-8663-a135f5f85457)

Lần này thì không có robots.txt nữa 

![image](https://github.com/user-attachments/assets/092ffa2a-a10c-441b-8d05-10277b368f06)

Fuzz thử thì ra có thế này 

![image](https://github.com/user-attachments/assets/8f3f09dd-f566-4da2-ad09-dbc2ff876527)

Sau 1 lúc tìm tòi, tôi đọc thử src code thì có cái `/admin-z8osff` 

![image](https://github.com/user-attachments/assets/08b8a790-9d05-407b-b821-2d18e87eee60)

![image](https://github.com/user-attachments/assets/7ebdcaa3-0fa5-4d2d-a279-374083ae4ed2)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/6e000587-75b7-4726-b1ce-8a276a12b209)

Lần này /admin chặn rồi 

![image](https://github.com/user-attachments/assets/53e604fa-eb4b-41e4-8553-86aecc8c0375)

Để ý đến cái cookie trong req vào admin 

![image](https://github.com/user-attachments/assets/0699170f-33b9-4c9b-a1cf-c4470379ce1c)

Ném và repeater, sửa thành true và gửi đi:

![image](https://github.com/user-attachments/assets/60626b48-076d-4ad6-b5bb-1f19cd732a54)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/827ddecf-0f00-4b64-a8df-5bffa5bd2de6)

Đăng nhập bằng wiener:peter

![image](https://github.com/user-attachments/assets/e3188080-ad80-40f5-81e5-2ff2991f69ef)

Khi dùng tính năng đổi email thì có hết các thông tin của user, có cả roleid

![image](https://github.com/user-attachments/assets/01d8f523-261b-46d9-a469-3be88f2d93a6)

Bật intercept lên và sửa roleid thành 2 

![image](https://github.com/user-attachments/assets/52f82c0b-72df-4308-bd1a-b499fe992a6d)

À làm thế nó không có đổi được, tôi thử thêm cái roleid vào dưới email xem như nào

![image](https://github.com/user-attachments/assets/93d79e58-b805-42d0-a81a-afdfc2d21ef5)

![image](https://github.com/user-attachments/assets/85de01dd-83aa-4697-8803-19a98de4eda1)

Và đã vào được 

![image](https://github.com/user-attachments/assets/a2082abc-d5a2-4c3d-a037-2730faf791cc)

<h1>---------------------------------------------------------</h1>
<br>







