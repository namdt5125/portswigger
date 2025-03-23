![image](https://github.com/user-attachments/assets/f3ba873c-1ef7-4f69-85f8-54c784b96e7b)

Đây là req của bài:

![image](https://github.com/user-attachments/assets/020a9526-5cb2-4a5d-99de-884400a6a158)

![image](https://github.com/user-attachments/assets/9be33f03-2f0f-4253-a4d2-044ae67c5126)

Vậy thì muốn biết được thông tin phiên bản bên thứ 3 của web thì tôi nghĩ là check các thông tin trong src code hoặc gây ra lỗi để nó in ra phiên bản:

![image](https://github.com/user-attachments/assets/90fd2de3-530d-48b0-ac10-0775396278f0)

Ở chỗ GET /product?productId= thay vì tôi dùng số thì tôi chuyển sang string để gây ra lỗi:

![image](https://github.com/user-attachments/assets/ba40e942-726e-4e97-b9d7-18f2bbdb09f7)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/83788e00-cec4-4ca1-b8e0-856827910da6)

Để ý khi đọc src code của web thì xuất hiện dòng `<!-- <a href=/cgi-bin/phpinfo.php>Debug</a> -->`

![image](https://github.com/user-attachments/assets/eb210328-c0c6-4ae0-8f71-4161a4f4e895)

Tôi thử truy cập thì xuất hiện phpinfo ở đây, đọc 1 lúc thì xuất hiện cái SECRET_KEY

![image](https://github.com/user-attachments/assets/7205d03f-ae20-418c-b940-c5cb1d429982)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/c2cf593c-be17-4c72-89d6-db1f96cc9ac0)

Khi vào robots.txt thì xuất hiện Disallow: /backup

![image](https://github.com/user-attachments/assets/a12d1d77-83df-47a5-8741-84ac62c43ea9)

Và trong backup thì có ProductTemplate.java.bak

![image](https://github.com/user-attachments/assets/ef6b1a4a-7f14-482a-9d23-585d9fb63be0)

Và trong đó có để lộ src code:

![image](https://github.com/user-attachments/assets/c3c88b87-eaef-4490-8146-d1cd771ae705)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/4c7128c4-e413-4a06-ac34-9a4cd7f059f3)

Và đây là sao khi log in vào với vai trò là wiener:

![image](https://github.com/user-attachments/assets/b21e8052-f3b6-4c77-8b11-4048d6de3359)

Tôi thử vào /admin nhưng không có truy cập vào được, server yêu cầu `Admin interface only available to local users`:

![image](https://github.com/user-attachments/assets/30879213-d522-4bb6-8e04-31b7ff631e4c)

Tôi dùng TRACE method để gửi thử req, khi client gửi một yêu cầu TRACE, server sẽ phản hồi lại chính xác nội dung của yêu cầu đó, giúp kiểm tra xem có bất kỳ sự thay đổi nào xảy ra trong quá trình truyền tải hay không, và để ý response có `X-Custom-IP-Authorization: 113.23.51.229`

![image](https://github.com/user-attachments/assets/2450a5b9-8287-44da-ae1e-ff3bb7820a3f)

Khi thêm X-Custom-IP-Authorization và đổi thành localhost là 127.0.0.1 thì vào được admin panel:

![image](https://github.com/user-attachments/assets/0309f75e-b602-4ddb-b53e-fc42e1c5b21b)

![image](https://github.com/user-attachments/assets/c8a633cd-37bc-4879-86db-6ccd27365d90)

<h1>---------------------------------------------------------</h1>
<br>



