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




























