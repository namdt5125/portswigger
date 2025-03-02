![image](https://github.com/user-attachments/assets/501f1660-f46c-4ba8-8b64-195e70a5ebaa)![image](https://github.com/user-attachments/assets/2249d955-38cd-4c2b-906b-b48d85762217)

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

Có vẻ collaboratỏ của tôi có vấn đề rồi:

![image](https://github.com/user-attachments/assets/4e445066-f424-4360-a8d5-67285b796f7e)

![image](https://github.com/user-attachments/assets/a18bd17c-a4db-48f2-b2c2-5320acafee16)

Chắc là skip bài này...

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/beee699e-460a-4d28-8658-d35147d7cb2d)

Tôi làm cái payload `<img src=lmao onerror='alert(1)'>` là nó báo Attack detected: Event handler luôn mà:

![image](https://github.com/user-attachments/assets/cfae15e1-f69e-4227-952a-a282efc861ca)

Vào blacklist luôn:

![image](https://github.com/user-attachments/assets/4cb29974-62f9-413f-b164-4c90d17b8594)

Thêm cái `X-Forwarded-For: google.com` để kết nối lại, thêm cái này vào thì mọi req đều có x-forward-for:

![image](https://github.com/user-attachments/assets/4e3f7fb3-410d-4ed4-b725-87bb3eab903f)

Sau 1 lúc test thử thì có vẻ server không cấm các dấu <>' các thứ, chỉ cấm cái từ khóa onerror và alert() thôi:

![image](https://github.com/user-attachments/assets/9b592017-70a6-4b70-851c-eaca63250fb6)

Dùng payload `<img src=1 oNeRrOr=alert``1``>` để bypass, trong có 1 dấu backstick thôi chứ không phải 2 cái:

![image](https://github.com/user-attachments/assets/e36e6f93-829e-42cc-a3e9-69970c0208a8)




















