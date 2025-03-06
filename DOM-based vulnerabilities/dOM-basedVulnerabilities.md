![image](https://github.com/user-attachments/assets/2255a1e4-c223-410e-ba5c-f1d67412240c)

Sau 1 lúc bế tắc vì cái web này chả có chỗ nào để nhập vào cả, tôi đọc src code và thấy cái addEventListener:

![image](https://github.com/user-attachments/assets/9b3fee25-0195-463d-8f0e-878538b0a640)

![image](https://github.com/user-attachments/assets/dcdf2505-2afa-4943-9d08-c89eecda52cc)

Cái addEventListener là đính kèm 1 sự kiện và ở đây là message, vào exploit và dùng `<iframe src="https://0a62002103e430e482d7ce7900d900b6.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=alert(1)>','*')">`, đoạn mã sử dụng <iframe> để nhúng một trang web bên ngoài và ngay sau khi tải xong (onload), nó sẽ gửi một thông điệp (postMessage) đến trang web bên trong iframe

![image](https://github.com/user-attachments/assets/9c23d3be-0156-4356-8099-ca6efe0ae563)

![image](https://github.com/user-attachments/assets/d1071fb9-11a2-49f2-9cdf-5883eaf1af74)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/3a073471-af7a-421c-b7f1-c151b66fc4f4)

Cũng gần giống bài trước nhưng code này đổi 1 chút:

![image](https://github.com/user-attachments/assets/761f6cea-0dfd-48e4-85b8-f03e828041d8)

Tóm tắt thì là đoạn mã JavaScript này lắng nghe sự kiện message từ postMessage và điều hướng (redirect) trình duyệt đến URL nhận được, khi một trang web hoặc iframe gửi một message bằng postMessage, đoạn mã này sẽ nhận sự kiện đó.
Lấy dữ liệu từ e.data, là dữ liệu mà trang khác gửi đến, kiểm tra xem dữ liệu có chứa http: hoặc https: không và cuối cùng là điều hướng (redirect) trình duyệt đến URL đó

Dùng `<iframe src="https://0aab008b03a4b37f8160661b002d00e7.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')">`

Khi iframe tải xong, đoạn JavaScript bên trong sẽ chạy, this.contentWindow: Truy cập vào cửa sổ (window) của trang bên trong iframe, postMessage(...): Gửi dữ liệu đến trang trong iframe, 'javascript:print()//http:' là nội dung của message được gửi đi, '*' có nghĩa là không giới hạn nguồn nhận (có thể gửi đến mọi trang), cái đoạn script bị bypass bằng cách //http:

![image](https://github.com/user-attachments/assets/a4c847f9-a695-4124-ad12-f1c8a5672bbb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/2d54c477-187a-482f-85ac-9b5fe66cceb9)

Như bài trước nhưng lần này script dài hơn

![image](https://github.com/user-attachments/assets/51a191af-ba50-44ae-affd-8b53649888d8)

Đoạn mã này sẽ xử lý nội dung nhận được khi lắng nghe sự kiện message từ postMessage, document.createElement('iframe'): Tạo một thẻ <iframe> mới, document.body.appendChild(iframe): Chèn <iframe> này vào trang.
Phân tích dữ liệu nhận được (JSON.parse), nếu dữ liệu không phải JSON hợp lệ, nó sẽ bị bỏ qua (return), ACMEplayer có thể là một trình phát video/stream nhúng (tôi cũng chả rõ nó là cái gì) và một trang bên ngoài có thể gửi postMessage để điều khiển việc hiển thị nội dung của iframe.

Dùng `<iframe src=https://0a33008e04037137810e03e70022001c.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>`:

Dùng postMessage để gửi javascript:print() vào iframe, nó sẽ thực thi cái print kia, nếu không có \, trình duyệt sẽ hiểu nhầm dấu " trong JSON là dấu " kết thúc chuỗi onload, ví dụ không có \ trình duyệt sẽ hiểu "type" là kết thúc của chuỗi đầu tiên và gây lỗi, tóm lại là quan trọng

![image](https://github.com/user-attachments/assets/4f2898c6-de06-4a0f-8b2f-7017c2505872)

<h1>---------------------------------------------------------</h1>
<br>



























