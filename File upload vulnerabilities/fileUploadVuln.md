![image](https://github.com/user-attachments/assets/c08124b9-1bb4-4f25-bbe9-e466f736fb1e)

![image](https://github.com/user-attachments/assets/502fb8f5-c22b-4c4b-83db-c7460485c6ab)

Sau khi đăng nhập với user:password mà đề cho thì tôi sử dụng chức năng file upload 

![image](https://github.com/user-attachments/assets/e53a39ec-b155-4c20-9974-11b1e6ee7dba)

Sau 1 lúc FUZZ thì thấy có files là 403 

![image](https://github.com/user-attachments/assets/4525deba-ccdf-49da-ba51-ab7a4edd5b9d)

Và sau 1 lúc mò tiếp, sau đó đổi thành `<?php system($_GET['test']); ?>` để remote

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e1c8f262-0a46-4407-a185-c9cc801237de)

Sau khi upload thì ra cái này

![image](https://github.com/user-attachments/assets/24782ffd-6173-4b75-a277-5b8a05a3ade3)

![image](https://github.com/user-attachments/assets/83dd262e-7e65-4794-951e-d9323be6e197)

Đổi `Content-Type: image/png` là ra

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/5fab8c85-70b7-4bb3-81e5-26d9e0a0ad3c)

![image](https://github.com/user-attachments/assets/6c949d19-73fa-4b4c-8432-e3ea7db30e6e)

![image](https://github.com/user-attachments/assets/2e371b31-ae83-4527-977e-c660c22a4716)

Tôi tìm thấy nó ở dạng text, có vẻ bên phía server đã config khi ném vào trong cái files kia là chuyển về dạng text 

![image](https://github.com/user-attachments/assets/a0f2ae92-ce43-4e6c-8e91-f610f7578998)

Thêm 2 cái `..%2f` ở trước để cho nó về cái dir to xem có chạy được không 

![image](https://github.com/user-attachments/assets/8b330aac-ba80-463d-9775-ad3e27c03573)

Xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/fbedc7da-2839-40bd-8ab7-b7d2d6d92ed6)

![image](https://github.com/user-attachments/assets/c3a5f729-1507-4862-b198-d62af2dec36f)

Đề bảo blacklist thì tôi kiếm mấy cái extension khác của php lắp vào xem được không 

![image](https://github.com/user-attachments/assets/8f817cc0-f15d-4d7b-b175-98e8d1af101d)

![image](https://github.com/user-attachments/assets/dfd011a5-b789-45bf-b330-36e4041bb356)

Tiếc là nó ở text, tôi cũng không dùng được path traversal trong bài này 

![image](https://github.com/user-attachments/assets/f354f960-e21a-4648-a4c1-bb9bb5196b9d)

![image](https://github.com/user-attachments/assets/e4c9fcbd-677f-489c-baff-167080bb8250)

Thôi thì mưu hèn kế bẩn, tôi tìm được cái này dùng apache và không lọc tên file có dạng .file nên có thể sẽ dùng được .htaccess 

![image](https://github.com/user-attachments/assets/65d2acac-5bb3-4afe-91b1-88b75375251d)

![image](https://github.com/user-attachments/assets/6cd46e3a-b663-4a44-88fc-df313c567677)

![image](https://github.com/user-attachments/assets/f43bf88b-c2fc-4b37-8117-c986f9745c66)

Xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/215f944f-a911-4ced-8e00-968bd9f898f9)

![image](https://github.com/user-attachments/assets/fd29945f-9d1b-49a7-9173-c2b501daf199)

Do tên đề và tôi đã làm qua mấy bài path traversal nên tôi tò mò thử chèn %00 vào thì nó được, và như tôi đã nói thì nó chỉ xảy ra với phiên bản php cũ

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/ad3c734b-2457-4282-97f7-f48555ee1533)

![image](https://github.com/user-attachments/assets/e87b45a7-337d-4940-9e64-a1199f09732e)

Sau khi chuyển qua nhìn đây tôi biết là nó kiểm tra nội dung file 

![image](https://github.com/user-attachments/assets/e4c1fe39-8012-4bc2-85f6-23470ec3e830)

Tôi để sang gif cho dễ dùng 

![image](https://github.com/user-attachments/assets/38b74abe-c09c-42cb-acbf-ac7c7cd6b76d)

Do bài này hồi xưa tôi chưa làm nên giờ tôi hoàn thiện, thay nội dung file thành `<?php system($_GET['test']); ?>` 

![image](https://github.com/user-attachments/assets/24758379-9344-4977-9f6b-eff055ef7537)

![image](https://github.com/user-attachments/assets/875d5381-8297-41fe-ad42-4c328e787618)

![image](https://github.com/user-attachments/assets/da6e6ea7-789e-4007-a73e-b96f3433cf0b)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/55fc2fbd-46ba-48de-8e80-ecd09ce53848)

![image](https://github.com/user-attachments/assets/c3bf0bb9-d092-47f3-9a06-5280dd5d0b54)

![image](https://github.com/user-attachments/assets/3e8650de-81fc-4602-9c1c-71e130841cca)

Test qua qua chức năng

![image](https://github.com/user-attachments/assets/03d696ca-26b9-44e3-840f-e6a9b84428a8)

![image](https://github.com/user-attachments/assets/95f9725f-e58c-48cc-884e-fc5e01ee5c48)

Nhìn đoạn code tôi thấy server lưu tạm vào trong `files/avatars/`, sau đó tiến chạy 2 hàm, hàm checkViruses thì code không có tiết lộ rõ, đại khái là check virus, tí nữa sẽ nói tiếp về cái check virus<br>Hàm checkFileType là check mỗi tên của file xem có đuôi là png hay jpg không, nếu không thì return false và ngược lại, sau đó sẽ in ra tên file, ngược lại thì xóa file luôn 
<br>
Do cái checkViruses chạy trước, thế nên nó sẽ cần 1 khoảng thời gian để check virus, thời gian có thể vài mili giây nhưng nó đã có sự tồn tại của test.php trong `files/avatars/`, chỉ là bị xóa đi thôi, vậy thì việc của tôi là sau khi upload test.php và đồng thời nhanh chóng truy cập vào đường dẫn `GET /files/avatars/test.php` để đọc nội dung<br>
Để làm được điều đó thì đưa cái request POST, tức cái request upload test.php lên và cái request `GET /files/avatars/test.php` để đọc vào repeater, add 2 cái đó cùng 1 group, chọn cái gửi cùng lúc(gửi song song, parallel), để tăng tỉ lệ thành công thì duplicate cái `GET /files/avatars/test.php` lên nhiều cái, nó sẽ tăng khả năng đọc file hơn:

![image](https://github.com/user-attachments/assets/0d4ac646-5e2d-46bf-b53c-32a4fa171496)

![image](https://github.com/user-attachments/assets/e6d211d0-d1a5-4d10-87d5-a040ef103a36)

Nếu không được thì ấn lại vài lần hoặc duplicate thêm vài cái để nó ra

![image](https://github.com/user-attachments/assets/f637d753-d539-4828-85e8-8bf813f636bf)

![image](https://github.com/user-attachments/assets/dd90a9de-28cc-4aff-9bab-7b436c0f7820)

