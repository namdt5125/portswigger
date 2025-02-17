![image](https://github.com/user-attachments/assets/0688f651-3604-44e7-8770-fb52e2c61ab5)

![image](https://github.com/user-attachments/assets/988b62fa-18d5-4dd1-95bd-446963de1d9b)

![image](https://github.com/user-attachments/assets/8f6584cb-3945-4913-872c-0db1cbf857d3)

![image](https://github.com/user-attachments/assets/206ca057-36f9-46e9-9a4f-cf391e18849e)

Nhớ tắt filter images trong burp đi:

![image](https://github.com/user-attachments/assets/92d6667a-bd2b-495a-b40d-5ab6bc571ceb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/be5e6634-4cb2-4c3d-bd38-10cc930270d2)

![image](https://github.com/user-attachments/assets/8f32f21a-4083-4663-9704-c262a4080ec1)

Lần này nó nhận đường dẫn tuyệt đối thay vì đường dẫn tương đối như ban nãy

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/da8a7eeb-e6e5-484b-9185-20b98857319a)

![image](https://github.com/user-attachments/assets/c059b91f-88b4-4aaf-a31a-7141e7f85ee0)

`....////....////....////....////etc/passwd`, payload này hoạt động là do trong mã nguồn có sử dụng bộ lọc là khi có `..` hoặc `../` là nó tự động xóa đi, nhưng nó chỉ check 1 lần, không có lặp lại, thế nên `....////....////....////....////etc/passwd` 
biến thành `..///..///..///..///etc/passwd`, với cái dấu / kia thì không quan trọng vì có // hay /// hay thậm chí nhiều hơn thì nó vẫn giữ đúng chức năng của nó

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/32bbf4f0-150e-4a69-90dd-f39ebe27f5c5)

Tôi thử với `..%2f..%2f..%2fetc/passwd` thì không có, thử encode phát nữa thì ra `%252E%252E%252F%252E%252E%252F%252E%252E%252F%252E%252E%252Fetc%252Fpasswd`, theo tôi nghĩ thì nó lấy cái thứ 2 về, sau đó decode theo url, rồi vào trong code nó lại decode phát nữa

![image](https://github.com/user-attachments/assets/edaad46c-5c94-4661-99df-8e7cd2606e83)

Ở solution thì nó ngắn hơn `..%252f..%252f..%252fetc/passwd`, nó chỉ encode mỗi / thành `%2f` và tiếp tục encode % thành `%25`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f7b8c620-cd46-490e-85f9-143d8dcb5d02)

![image](https://github.com/user-attachments/assets/41658127-ff13-4ae8-98f6-4fda76a3491a)

![image](https://github.com/user-attachments/assets/e0fbb248-08c0-4c4d-abf1-0e3153eb6a7b)

![image](https://github.com/user-attachments/assets/cf39a19a-96b1-41a2-974d-7007ce72c2e0)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/5e7e7766-c862-42a0-af6b-8b167763c183)

![image](https://github.com/user-attachments/assets/737aaf7e-ccfb-4fd4-9a87-8d82203aef83)

![image](https://github.com/user-attachments/assets/7533c7b3-ec19-4fb6-80bb-7e640cec17c6)

Thì theo như đề bài, tôi để thêm `%00`, tức là byte null vào, vậy là ra, cái này xảy ra ở C, PHP phiên bản cũ vì nó tưởng cái đấy là kết thúc 

<h1>---------------------------------------------------------</h1>
<br>
