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

![image](https://github.com/user-attachments/assets/366586a1-30fd-46e8-b2d2-0e3a989f0dc8)

Sau 1 lúc khám phá thì để ý cái nút back to blog:

![image](https://github.com/user-attachments/assets/ceaa1099-a24d-43b7-aa22-05043f6f580c)

Cái href="#" khi nhấp vào liên kết này, trình duyệt sẽ không điều hướng đến URL khác ngay lập tức mà chỉ thực thi JavaScript trong sự kiện onclick, /url=(https?:\/\/.+)/: là một regex nhằm tìm kiếm một phần của URL có dạng url=https://example.com, .exec(location) thì kiểm tra xem location (đại diện cho URL hiện tại của trang web) có khớp với regex không. Nếu có, nó sẽ trả về một mảng kết quả với phần tử đầu tiên là toàn bộ chuỗi khớp, và phần tử thứ hai là URL thực tế, nếu returnUrl tìm thấy URL hợp lệ, trình duyệt sẽ điều hướng đến returnUrl[1] (tức là trang blog)

![image](https://github.com/user-attachments/assets/da282009-bf62-4a86-8c95-b0e5943a850a)

Để dễ hiểu hơn thì khi tôi thêm `&url=https://google.com` vào, sau đó ấn back to blog thì web sẽ dẫn đến địa chỉ https://google.com

![image](https://github.com/user-attachments/assets/752e4433-c141-4eaf-98c8-cb8c9ff8ab6d)

Req của nó đây:

![image](https://github.com/user-attachments/assets/40b4a377-b248-4c69-9a6f-5beaeca4f391)

Đưa link exploit vào là xong:
                                                                                            
![image](https://github.com/user-attachments/assets/40ca71b7-1d76-4e4c-b3e5-b7a955b0d1cd)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e8157373-7d34-4e6b-bf8c-245f1f105de2)

Để ý sau khi xem 1 bài post thì ở cookie có xuất hiện lastViewedProduct:

![image](https://github.com/user-attachments/assets/da111c19-3e50-467d-9412-a71f8c36e9d1)

![image](https://github.com/user-attachments/assets/c307ae5f-7c34-4337-9713-0cc7c71f0cf8)

Và đây là kết quả sau khi tôi sửa cookie thành `https://0a8200cc04b9058a87bca17900200028.web-security-academy.net/product?productId=2&https://0a8200cc04b9058a87bca17900200028.web-security-academy.net/product?productId=1&%27%3E%3Cscript%3Eprint%28%29%3C%2Fscript%3E`

![image](https://github.com/user-attachments/assets/2bfadf07-969e-465c-a508-293f01f0a9de)

![image](https://github.com/user-attachments/assets/e0d60a6b-1e7d-4950-bcec-d52c2d6f7302)

Giờ chỉ cần đưa vào exploit là xong:

```<iframe src="https://0a8200cc04b9058a87bca17900200028.web-security-academy.net/product?productId=3&'><script>print()</script>" onload="if(!window.x)this.src='https://0a8200cc04b9058a87bca17900200028.web-security-academy.net';">```

window: Là đối tượng toàn cục trong trình duyệt, đại diện cho cửa sổ trình duyệt hiện tại, điều kiện if (!window.x) kiểm tra xem window.x có tồn tại hoặc có giá trị khác false, undefined, 0, null, NaN hay không, nếu window.x chưa tồn tại, trình duyệt sẽ thay đổi src của <iframe>, sau đó gán window.x = 1 để ngăn việc thay đổi này lặp lại

![image](https://github.com/user-attachments/assets/203e1799-61cd-4331-8ad7-e20acd0fb2e7)






















