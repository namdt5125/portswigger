HTTP Smuggling (HTTP Request Smuggling) là một kỹ thuật tấn công web trong đó kẻ tấn công lợi dụng sự không nhất quán trong cách các máy chủ web hoặc proxy xử lý tiêu đề HTTP 
(Content-Length, Transfer-Encoding, v.v.). Mục tiêu là gửi một yêu cầu HTTP được thiết kế đặc biệt để máy chủ xử lý sai, từ đó có thể bỏ qua tường lửa hoặc cơ chế bảo mật,
 tấn công request của người dùng khác (đánh cắp thông tin, chiếm phiên, thực hiện CSRF,...), kích hoạt lỗ hổng bảo mật trên ứng dụng web,...

![image](https://github.com/user-attachments/assets/e58891de-81bf-4276-bfa0-a5502125fe30)

Trong cái req này thì là http 2 và phải cho nó xuống 1.1 mới làm được bài này:

![image](https://github.com/user-attachments/assets/fad6ad0b-0d4e-400f-9e87-953ee1cbb2c6)

![image](https://github.com/user-attachments/assets/83f59e25-b128-4467-b39e-9d7e121744b0)

Tôi chuyển method sang POST và dùng thử cái payload trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Request%20Smuggling/README.md):

![image](https://github.com/user-attachments/assets/c8009207-e0f7-45f1-9e89-0f459bbe806d)

![image](https://github.com/user-attachments/assets/938e8979-8093-402f-8721-43e7ea303e88)

Sửa mỗi cái host, sửa req thì chạy vẫn trả về 200

![image](https://github.com/user-attachments/assets/8e53888c-0021-4688-bb9d-e8f76a0e4b96)

Sau đó tôi chèn thêm 1 cái req GET ở dưới và nó thành 404 not found:

![image](https://github.com/user-attachments/assets/29493e2c-455b-4e04-9b46-f47b4a6fd59e)

![image](https://github.com/user-attachments/assets/1010dcf7-b073-4eb7-a383-20442c0d5425)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/8f3521ac-ff0f-4861-b19c-a2350af3d310)

Vẫn là từ cái payload lần trước:

![image](https://github.com/user-attachments/assets/16e47996-7961-4146-a207-1121919359ca)

Dùng req như trước thì có 500, không có gì đặc biệt cả:

![image](https://github.com/user-attachments/assets/3dd1d209-2637-4904-b2f9-8ec67e9be31f)

Thì tìm hiểu qua qua về Chunked encoding, là một phương pháp truyền dữ liệu trong giao thức HTTP/1.1, giúp máy chủ gửi dữ liệu theo từng phần (chunk) mà không cần biết trước tổng kích thước của nội dung.<br>

Để ý lần đầu gửi req này thì nó mấy kha khá thời gian để trả lại response:

![image](https://github.com/user-attachments/assets/35258098-01cb-4eb7-8710-a3361fbaf3f0)

Tôi sửa thành như này và được 

![image](https://github.com/user-attachments/assets/90279773-bdbf-49f5-88a4-312c902001b0)

Trong đó 5e là độ dài của nội dung ở dưới

![image](https://github.com/user-attachments/assets/09e28659-5313-4de7-a397-5316c82cf89c)

Đầu tiên thì proxy sẽ xử lý Content-Length: 4 tức là 5e\r\n, nhưng 5e là phần đầu của dữ liệu chunked encoding, nghĩa là phần còn lại của request vẫn chưa được proxy xử lý đúng, do đó, phần GPOST / HTTP/1.1... trở thành một request mới nằm trong request đầu tiên, nếu thay GPOST bằng POST, một số hệ thống bảo mật có thể phát hiện request giả mạo và chặn nó<br>
Còn tại sao lại là GPOST thì khi dùng cái GPOST proxy sẽ hiểu là sai và sửa lại thành POST cho đúng, có thể thay bằng cái khác nhưng cái G nó xịn hơn và do nó giống GET nữa

![image](https://github.com/user-attachments/assets/ed336a8b-c984-4161-9879-bd000738410d)

![image](https://github.com/user-attachments/assets/5c4907ea-1917-42ee-b7e1-62573ed4c139)

<h1>---------------------------------------------------------</h1>
<br>

















































































