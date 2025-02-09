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

![image](https://github.com/user-attachments/assets/ef70974c-20ab-4ecc-904a-0f7ffd5fbe85)

![image](https://github.com/user-attachments/assets/4f7d52ab-76f5-44c9-a1e4-be50d6be6096)

Ở trong mã nguồn thì bài này dùng document.write để lấy đầu vào từ location.search, query chính là cái được lấy từ parameter search, thứ mà tôi nhập vào và có 1 cái thẻ img trong đó, tôi sẽ sử dụng payload `aaaa"> <img src="lmao" onerror="alert(1337)`, cái aaaa"> là để đóng thẻ cũ, sau đó mở thẻ mới và do trong mã nguồn có sẵn "> nên tôi không cần thêm vào, thêm vào nó bị thừa

![image](https://github.com/user-attachments/assets/a30467cc-7c11-4f0b-a741-fc7d3119b249)

Hoặc là dùng `"><svg onload=alert(1)>` theo solution

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/19af90be-7e78-4f59-a354-7f90d1d318d5)

![image](https://github.com/user-attachments/assets/be2214f4-2ed3-40c0-9071-6db2e87d6f0e)

![image](https://github.com/user-attachments/assets/4596f09d-a2cb-455e-a690-9d42c3a27495)

Bài này khác bài trước ở chỗ là dùng document.getElementById('searchMessage').innerHTML = query; 

![image](https://github.com/user-attachments/assets/98989063-c11e-41f7-9466-bb5fc28c83b4)

Đây là điểm khác biệt giữa 2 cái

![image](https://github.com/user-attachments/assets/93b8c3d4-86e2-4fe1-9dda-f952ae2a4a39)

Sau khi tôi nhập `<script>alert(1337)</script>` thì không thấy, tôi dùng payload `aaaa"> <img src="lmao" onerror="alert(1337)">` thì ra:

![image](https://github.com/user-attachments/assets/fab5fb62-da33-4b89-8413-f3c1bb092c14)

Payload của solution cũng thế

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f0f74602-4134-4702-a22d-86f230670eb6)

Khai thác từ phần submit feedback 

![image](https://github.com/user-attachments/assets/846b74d9-90db-4221-a30d-f77233d3541c)

Đại khái thì là `$('#backLink')` là  `<a id="backLink">Back</a>`, attr trong jQuery được dùng để lấy hoặc thiết lập giá trị của thuộc tính, trong đây tức là thiết lập giá trị href là window.location.search chính là cái returnPath 

![image](https://github.com/user-attachments/assets/9507d160-c6b1-4197-85f7-c59af406083d)

![image](https://github.com/user-attachments/assets/df1f2521-044c-40b9-a879-6e70e3e6daa1)

Để dễ hiểu hơn thì khi tôi nhập https://www.google.com/ vào returnPath và ấn vào Back thì nó đưa đến google.com vì khi tôi ấn cái Back là tôi thực thi lệnh 

![image](https://github.com/user-attachments/assets/8e57ce77-f42d-4fd8-9cb2-08836f035b7a)

Đây là tôi thử với payload `<script>alert(1337)</script>`, rõ ràng là không được vì nó chính là copy paste cái payload đó trên thanh trình duyệt, khi tôi thử đến javascript:alert(1337); thì nó không cho tôi chèn vì chrome nó cấm, sử dụng `javascript:alert(document.cookie)` ở trong burp, dùng `javascript:alert(document.cookie)` là vì cái này nó thực thi trên thanh trình duyệt, đối với cũ thì được còn mấy cái mới thế này thì nó không cho

![image](https://github.com/user-attachments/assets/cc7cd68d-0265-40c0-b004-21ab8f265cd6)

<h1>---------------------------------------------------------</h1>
<br>





