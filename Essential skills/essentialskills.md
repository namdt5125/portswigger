![image](https://github.com/user-attachments/assets/502d3fd3-0f84-4f36-9593-35f7408ff690)

Để ý phần check stock, do trước đó tôi thử mấy cái khác không thấy được, cái này mới được:

![image](https://github.com/user-attachments/assets/9bb13c49-c6c6-4fb0-9101-bc3d64e8d70a)

Đưa req vào active scan:

![image](https://github.com/user-attachments/assets/5e31ff3b-62e1-4ce2-acd9-c20b86dc5de6)

Sau khi quét thì có 1 cái lỗi đỏ:

![image](https://github.com/user-attachments/assets/ffabe89a-a6a8-4b98-b3d6-8f40e2d388f8)

Ném payload thì nó như này đây:

![image](https://github.com/user-attachments/assets/bed760e1-7b56-45f0-9bf8-ad9539d4af36)

![image](https://github.com/user-attachments/assets/e67036dd-32ea-4084-a34a-c34ed0f44e89)

Sửa payload thành
```
<wyh xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></wyh>
```
Giải thích qua qua thì đây là một ví dụ về XML External Entity (XXE) Injection, một kiểu tấn công khai thác lỗi xử lý XML khi một ứng dụng không kiểm soát việc include nội dung từ các tài nguyên bên ngoài

