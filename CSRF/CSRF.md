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

![image](https://github.com/user-attachments/assets/a2777793-6922-41f1-bd65-868b7ff7c599)

Lần này trong cookie có hẳn cái csrfkey 

![image](https://github.com/user-attachments/assets/bfcabbde-b26b-42f0-ba63-afb4e90bfdea)

Tôi thử đổi riêng các token csrf hoặc csrfkey giữa 2 tài khoản thì không có được, xóa cũng không được, nhưng nếu đổi cả token lẫn csrfkey thì lại được:

![image](https://github.com/user-attachments/assets/517178eb-fac4-432a-a854-42a37332b8dd)

Vấn đề là làm sao để có thể lấy được token của nạn nhân hoặc là đưa cái token của mình vào? Để ý cái tính năng search của bài, khi search thì cái req có chứa cái cookie:

![image](https://github.com/user-attachments/assets/690604b0-eb66-4faa-a967-92d23c051aee)

![image](https://github.com/user-attachments/assets/64f572fc-727b-4c16-abe6-ed64552d54ca)

![image](https://github.com/user-attachments/assets/df2f8dbe-7682-4898-a254-5e5fd1ab3c6d)

Với cái này thì dùng loại inject vào trong cái header với payload `?search=lmao%3b%0d%0aSet-Cookie:%20csrfKey=TDJV7g1KMSCZg0S1ZQodg0quVFdxzfiL`, trong đây có đưa con trỏ về đầu bằng %0d và xuống dòng với %0a:

![image](https://github.com/user-attachments/assets/69444495-b94d-4f4a-b8b6-e7274a97ba28)

Tạo cái csrf PoC và sửa thành như này:

![image](https://github.com/user-attachments/assets/f473df5f-c9bb-477f-b2a1-46137f84e761)

![image](https://github.com/user-attachments/assets/ed3ab3a7-c26e-45b1-a9cd-8fac9ad6ff24)







































