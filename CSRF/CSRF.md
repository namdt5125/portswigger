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

Với cái này thì dùng loại inject vào trong cái header với payload `?search=lmao%3b%0d%0aSet-Cookie:%20csrfKey=TDJV7g1KMSCZg0S1ZQodg0quVFdxzfiL`, trong đây có đưa con trỏ về đầu bằng %0d và xuống dòng với %0a, cái này để set cái csrfkey cookie của nạn nhân thành giống với cái của wiener:

![image](https://github.com/user-attachments/assets/69444495-b94d-4f4a-b8b6-e7274a97ba28)

Tạo cái csrf PoC và sửa thành như này:

![image](https://github.com/user-attachments/assets/f473df5f-c9bb-477f-b2a1-46137f84e761)

![image](https://github.com/user-attachments/assets/ed3ab3a7-c26e-45b1-a9cd-8fac9ad6ff24)

Sau khi thử thì không thấy nó solve, tôi sửa payload là thành như này, giữ lại `Secure; HttpOnly` và thêm `SameSite=None` là một thuộc tính trong cookie giúp kiểm soát cách trình duyệt gửi cookie khi có yêu cầu từ trang web khác

![image](https://github.com/user-attachments/assets/6f2f1e29-5594-43e4-9f9a-dc123201cc01)

![image](https://github.com/user-attachments/assets/b088b0a4-3898-40c1-a632-23d3ccd20cbd)

Đại khái thì payload này sẽ đổi cookie của nạn nhân, cụ thể là csrfkey và token csrf, sau đó tự động đổi email

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/0b746cb3-cdbc-4e4c-8939-93fa6b281ed2)

Lần này thì token csrf lặp lại cả ở cookie:

![image](https://github.com/user-attachments/assets/ee4270bc-0be7-4d18-be07-454a5b060440)

Tôi dùng tính năng search và inject payload `search=lmao%3b+Secure%3b+HttpOnly%0d%0aSet-Cookie:csrf=8XBVDtGcrz1QayzohITrrK3XldjZXM0x%3b+SameSite=None` vào trong header:

![image](https://github.com/user-attachments/assets/a7181868-1e8f-4aca-8265-0ee1b96c1986)

Và đây là payload, chức năng payload này khá giống bài trước:

![image](https://github.com/user-attachments/assets/8b4dddb5-e402-4616-a96c-6d5e65114842)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/807776ad-8e2e-4c6d-8cdb-dfa8f8184e1f)

Đây là req đổi email thông qua tài khoản wiener:

![image](https://github.com/user-attachments/assets/d0a3e177-cd84-4b86-b31e-bd7c8d55dff3)

Thử dùng csrf PoC mà không được:

![image](https://github.com/user-attachments/assets/0d659fff-b852-49be-b9ae-00a626d76b43)

Tôi thử đổi method sang GET nhưng vẫn không được:

![image](https://github.com/user-attachments/assets/ce37f2d9-fbb3-4661-b6f3-7b367379b4d8)

Tôi tìm được cái `_method` để ghi đè method: 

![image](https://github.com/user-attachments/assets/aab1e973-08db-4fe7-bc43-84d7f3df7fd8)

Tôi đổi method thành GET, lấy csrf PoC và thêm `<input type="hidden" name="_method" value="POST" />`:

![image](https://github.com/user-attachments/assets/f25ff017-7e17-405c-aacf-77177f9d105a)

![image](https://github.com/user-attachments/assets/68698acd-f709-4a7c-aa29-0c1e6499bc6a)

<h1>---------------------------------------------------------</h1>
<br>
























