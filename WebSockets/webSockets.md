![image](https://github.com/user-attachments/assets/2249d955-38cd-4c2b-906b-b48d85762217)

Đây là chức năng livechat của web:

![image](https://github.com/user-attachments/assets/9eb75977-705b-4cad-984c-e367aef9fbc5)

Thử với `<scrtip>alert(1)</script>` thì không có được

![image](https://github.com/user-attachments/assets/4a1e5393-1867-4e97-8df3-c9faa5300fd5)

Tôi nghĩ là nó phải luên quan đến tính năng hiển thị như img chẳng hạn, tôi dùng `<img src="lmao" onerorr="alert(1)">`:

![image](https://github.com/user-attachments/assets/f980aa7e-ce2f-4c8a-99dc-b53e32638756)

Và tôi vẫn thấy không được, đọc src code thì thấy đã bị mã hóa, tôi thử bật intercept lên xem nó như nào:

![image](https://github.com/user-attachments/assets/7f9d0e17-6575-4a2f-aa06-cf016b861ae8)

Khi gửi payload thì tôi nhận ra là `<img src="lmao" onerorr="alert(1)">` đã được filter trước khi gửi

![image](https://github.com/user-attachments/assets/ec76225c-fc73-4356-949e-403747496903)

Tôi loại bỏ mấy cái filter các dấu đi và đổi nháy đôi thành nháy đơn `<img src='lmao' onerorr='alert(1)'>` để đỡ nhầm với dấu nháy đôi của json kia:

![image](https://github.com/user-attachments/assets/40e494cc-abe9-41c7-a07f-8d68df5fa34f)

Nhưng vẫn không chạy được, tôi thử đổi thành `<img src=lmao onerorr='alert(1)'>`, tức là bỏ dấu ' đi thì được, có vẻ lúc đấy mới xảy ra lỗi và chạy alert(1):

![image](https://github.com/user-attachments/assets/d582b344-23aa-4e97-b359-dcdda804d6ea)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/c7932a50-0ee4-43fd-8c75-81e922c85a42)

Đây là cái live chat của web:

![image](https://github.com/user-attachments/assets/74ce17c5-191d-407a-b1a7-3a98dafc9fb8)

Không có xss xảy ra ở đây:

![image](https://github.com/user-attachments/assets/71e0201e-51c0-4a55-9dd0-e365eca1ac90)

Vào websockets history thì có chứa lịch sử của cuộc trò chuyện từ lúc tôi truy cập vào web:

![image](https://github.com/user-attachments/assets/40983f88-9d46-415f-a42a-4266291f3f82)

Nếu để ý thì thấy có cái READY, cái READY thường xuất hiện trong giao thức WebSockets, nó cho biết kết nối WebSocket đã được thiết lập thành công và máy chủ đã gửi thông tin khởi tạo về client:

![image](https://github.com/user-attachments/assets/41a8173f-1e9d-4e25-9df7-3f4c4d5bed5c)

Khi ném vào repeater và gửi thì nó hiển thị toàn bộ lịch sử cuộc trò chuyện của người đó do server sẽ check cookie và gửi lại lịch sử cuộc trò chuyện:

![image](https://github.com/user-attachments/assets/b58336aa-13de-4428-944c-103ee66ea703)

Viết 1 script gửi READY và trả kết quả về burp collaborator:

![image](https://github.com/user-attachments/assets/02945ddd-226d-41b3-8e88-cf029cbbd9ac)

Đưa lên exploit:

![image](https://github.com/user-attachments/assets/bd9a5f54-d8ba-4cac-a57f-32c8430d6755)
































