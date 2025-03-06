![image](https://github.com/user-attachments/assets/2255a1e4-c223-410e-ba5c-f1d67412240c)

Sau 1 lúc bế tắc vì cái web này chả có chỗ nào để nhập vào cả, tôi đọc src code và thấy cái addEventListener:

![image](https://github.com/user-attachments/assets/9b3fee25-0195-463d-8f0e-878538b0a640)

![image](https://github.com/user-attachments/assets/dcdf2505-2afa-4943-9d08-c89eecda52cc)

Cái addEventListener là đính kèm 1 sự kiện và ở đây là message, vào exploit và dùng `<iframe src="https://0a62002103e430e482d7ce7900d900b6.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=alert(1)>','*')">`, đoạn mã sử dụng <iframe> để nhúng một trang web bên ngoài và ngay sau khi tải xong (onload), nó sẽ gửi một thông điệp (postMessage) đến trang web bên trong iframe

![image](https://github.com/user-attachments/assets/9c23d3be-0156-4356-8099-ca6efe0ae563)

![image](https://github.com/user-attachments/assets/d1071fb9-11a2-49f2-9cdf-5883eaf1af74)

<h1>---------------------------------------------------------</h1>
<br>






