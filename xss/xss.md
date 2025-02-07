![image](https://github.com/user-attachments/assets/594af6d7-14d6-46bb-8ca1-849dbca3dbec)

![image](https://github.com/user-attachments/assets/d2d037fc-8fe8-4d57-86fe-0391b2053160)

Vào thì thấy 1 cái ô nhập, tôi nhập thử thì dòng chữ có hiện lên màn hình:

![image](https://github.com/user-attachments/assets/c6999a43-5920-4046-9331-98d5121dd1af)

![image](https://github.com/user-attachments/assets/5fa498b4-a823-4cef-9794-da11dbf1df40)

Code không thấy được mã hóa và có dấu ' đi kèm theo, tôi thử payload `a' </h1> <script>alert('abc')</script> <h1>'lmao`, a' </h1> để kết thúc cái thẻ cũ và làm hẳn cái script mới, <h1> đằng sau là để nối cái đuôi </h1>

![image](https://github.com/user-attachments/assets/dc5de93e-f5bc-407c-9e21-2c46567db1d5)

![image](https://github.com/user-attachments/assets/6117369b-9649-48c0-84dc-a125a57a9fc1)

Solution thì ngắn hơn, chắc do tôi nghĩ quá lên

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/754de353-3cfc-45dc-9acb-1f7e612f3d79)

![image](https://github.com/user-attachments/assets/6d68b090-336c-4f6f-bd46-b13b58ce45c5)

Giao diện là các blog với button view ở dưới, và khi vào thì có chỗ comment

![image](https://github.com/user-attachments/assets/7f14671e-6cdd-4439-9222-b9e46129599b)

Sau khi comment thì nó ở đây 

![image](https://github.com/user-attachments/assets/b8ac084e-5042-4cdf-8b64-3ed9af9da170)

![image](https://github.com/user-attachments/assets/e56d85f9-694f-42a3-a2cd-5aafb0e68277)

![image](https://github.com/user-attachments/assets/4dac3fd5-8646-4374-a06f-7738e2fb43ca)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/354960b9-465d-4868-94de-9f856ffae6f0)

![image](https://github.com/user-attachments/assets/796f8ca4-d358-4b6e-8b89-5ca450c4bc72)

Giao diện có ô để nhập, tôi thử chức năng và xem mã nguồn

![image](https://github.com/user-attachments/assets/4f7d52ab-76f5-44c9-a1e4-be50d6be6096)

![image](https://github.com/user-attachments/assets/43e5b066-6a58-43ac-8f6c-a642a8bfac53)

Tôi thử với payload ngắn `<script>alert(1337)</script>` và đã bị được mã hóa

![image](https://github.com/user-attachments/assets/87915969-3e09-43de-9c5c-a1ce35338cbd)

![image](https://github.com/user-attachments/assets/070e6236-e41d-415b-827d-3ec1509de1f5)

Tôi thử payload `<img src="lmao" onerror="alert(1337);">` thì được

![image](https://github.com/user-attachments/assets/e15f72ac-f643-4ebc-9de1-fbcb755c3489)

Hoặc là dùng `"><svg onload=alert(1)>` theo solution

<h1>---------------------------------------------------------</h1>
<br>




























