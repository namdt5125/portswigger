![image](https://github.com/user-attachments/assets/b53f2c58-5001-4bde-8bf8-895fcae4a42d)

Đây là req khi tôi đổi email với user là wiener 

![image](https://github.com/user-attachments/assets/8cb3e453-f5a5-42e5-9579-d36b7d93b2ac)

Tạo 1 cái CSRF PoC:

![image](https://github.com/user-attachments/assets/5e366c9f-17c4-42fe-8868-1d9d165a931e)

Đưa vào trong exploit là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/bc064f7a-63e0-4a21-b6e3-b6a30662835d)

Đây là req của thay đổi email và có cả cái token csrf:

![image](https://github.com/user-attachments/assets/73044eac-8b76-4f79-af3f-5a6a992cde8a)

Token sai là không cho đổi mail:

![image](https://github.com/user-attachments/assets/0b747f5d-6779-47fb-b7e6-ee8748f12f55)

Cơ mà đề bài có nhắc đến thể loại req nên tôi thử chuyển sang GET, ném cái tham số email lên trên và gửi được req:

![image](https://github.com/user-attachments/assets/9e72c5e2-b7c0-4fe0-9549-745b72f617d2)

![image](https://github.com/user-attachments/assets/5b83260c-f62a-4063-a926-a40c3d231ff8)

Ném vào exploit là xong

![image](https://github.com/user-attachments/assets/6c3a014a-f132-4339-a23c-f906256a297a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/61e688d4-2546-4dfe-b7cb-2c3e56e92847)

Đây là req để đổi email:

![image](https://github.com/user-attachments/assets/46d48cbb-1d30-4b12-bf83-fe8e152dd2e0)

Tôi thử xóa hẳn cái token csrf đi và vẫn đổi được mail:

![image](https://github.com/user-attachments/assets/c25009bc-ae65-4e2e-abbc-7042cba93412)

Vậy là chỉ cần xóa token và đưa vào là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f724bab4-0487-456e-bb3d-6b799233dc41)

Sau 1 lúc thử, mỗi lần đổi email là đổi token csrf, không dùng lại được, không xóa đi được

![image](https://github.com/user-attachments/assets/ba5c9cf7-6f2e-4ce8-ad74-0548b05b9d99)

Bật f12 lên thì thấy có giá trị của token csrf, nếu đổi email là sẽ dùng cái token đấy, thử tiếp thì tôi thấy cái token không phân biệt các user khác nhau:

![image](https://github.com/user-attachments/assets/4ccd32c2-1464-4c39-bf66-6185f86f5c78)

Tạo cái CSRF PoC rồi đổi token và email là xong

![image](https://github.com/user-attachments/assets/f79c4b21-6d71-4321-b8c1-195b2c8c217a)

<h1>---------------------------------------------------------</h1>
<br>
























































