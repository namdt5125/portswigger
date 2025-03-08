![image](https://github.com/user-attachments/assets/e8526e75-80b1-4c0e-b9ff-21aa4af77dfc)

Để ý khi vào 1 cái đồ gì đó và bấm check stock thì req có gọi đến stockApi có chứa 1 đường link:

![image](https://github.com/user-attachments/assets/41c42c40-6e54-4bc9-85df-9c6b65c6860b)

Khi đổi bằng địa chỉ `http://localhost/admin` vào thì hiện ra cái admin panel:

![image](https://github.com/user-attachments/assets/38f85298-3d9f-4f8f-933c-5e081a98beb3)

Và xóa carlos là xong:

![image](https://github.com/user-attachments/assets/e5497db2-a228-4618-a21b-0da9461c95b5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/785939fb-f493-4822-9880-e32e1acc3072)

Vẫn như bài cũ:

![image](https://github.com/user-attachments/assets/6344016e-7566-4a26-a8b7-0f503e6e238b)

Vì trong đề có bảo là 192.168.0.x nên tôi đi brute cái x kia:

![image](https://github.com/user-attachments/assets/19c30d91-1577-43a6-bfd8-c5638b2c57b9)

![image](https://github.com/user-attachments/assets/2c5e07c6-99dc-4870-be5d-c691509d0e2a)

Kết quả là `http://192.168.0.65:8080/admin`, xóa carlos là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/919fa439-5786-4a18-9adb-32252d4c46fb)

Khi vào xem 1 cái sản phẩm nào đó thì có 1 cái referer

![image](https://github.com/user-attachments/assets/bfb70a06-61e6-4d57-9d6b-21e4624ef89f)

Tôi thử đưa vào repeater và sửa thành link của collaborator, và có req đã gửi đến:

![image](https://github.com/user-attachments/assets/25692424-c470-4de0-973a-8574a5abb560)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/6f26387a-d2b7-40df-82b3-800bb5dde069)

Vẫn là check stock bằng stockApi:

![image](https://github.com/user-attachments/assets/c8fd06ec-52d6-4d6e-a7f0-d929636076da)

Khi đổi sang `http://localhost/admin` thì đã bị chặn lại:

![image](https://github.com/user-attachments/assets/9cd634a0-a1da-41d3-9e2c-ff13f29d6170)

Đổi sang `http://127.0.0.1/admin` vẫn bị ăn block, tôi dùng cả ipv6 thì vẫn không có được:

![image](https://github.com/user-attachments/assets/461dfbf6-6a21-41d9-8397-6cbe9f7035d8)

Sau 1 lúc search thì tôi tìm được cái này:

![image](https://github.com/user-attachments/assets/46ee988d-5498-4d78-8746-5f979c1f2078)

Tức là có thể truy cập vào bằng 127.1, thêm 1 cái nữa là admin cũng nằm trong blacklist, do tôi thử thay bằng https://google.com thì được nhưng thêm admin thì bị chặn. Dùng `http://127.1/` thì có hiển thị cái admin panel:

![image](https://github.com/user-attachments/assets/fc8ab9aa-aeca-4e8a-b776-d406605f099e)

Vấn đề là vào được admin, tôi dùng url để encode vì sau khi encode url thì cái server vẫn hiểu là đến đường dẫn đó:

![image](https://github.com/user-attachments/assets/107a7443-41ae-4bf7-b7bb-61ee00c40f5e)

![image](https://github.com/user-attachments/assets/3d14a6ca-9e03-4d81-a67a-c02d83098c52)

Gửi đi vẫn không được, tôi thử encode lần 2 thì được, có vẻ do cái filter của server không có đệ quy:

![image](https://github.com/user-attachments/assets/5e808abc-1214-4533-92ce-ec2a627c0a6a)

![image](https://github.com/user-attachments/assets/48dc103b-72a1-42ab-94a0-59dfe430abd6)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/a058dc16-1295-47bd-a752-4d3003615dc5)

Vẫn nằm ở stockApi, có vẻ lần này server chỉ để dir và param ở sau, còn domain ở trước, có vẻ khó để làm gì đó:

![image](https://github.com/user-attachments/assets/e3070edc-e364-404c-9562-f6b709dbf7a1)

![image](https://github.com/user-attachments/assets/a0d16fac-ed34-4568-a936-7be394d192a5)

Và dĩ nhiên là tôi không thể cứ thế chèn vào được:

![image](https://github.com/user-attachments/assets/0f7dc5a3-f705-4445-9847-737bf7f61c1e)

Để ý có cái nút next product, nó có 1 cái path=/product?productId=3 là chứa cái sản phẩm tiếp theo và href đến:

![image](https://github.com/user-attachments/assets/d0c135c7-3a2a-4163-bca4-2a4f222d7f93)

![image](https://github.com/user-attachments/assets/691e715e-00d1-432a-89f6-46418a3a88b4)

Nếu đổi sang `https://google.com/` thì dẫn đến google.com luôn:

![image](https://github.com/user-attachments/assets/746ea682-f5b9-45a4-870a-eee53b1127d6)

Thử đổi stockApi thành `/product/nextProduct?currentProductId=2&path=/product?productId=3` thì dẫn đến trang product đấy luôn

![image](https://github.com/user-attachments/assets/30dcdaca-6b3f-4f5a-875d-7cb14ce0754a)

Giờ thì chèn cái localhost vào `/product/nextProduct%3fcurrentProductId%3d2%26path%3dhttp%3a//192.168.0.12%3a8080/admin`:

![image](https://github.com/user-attachments/assets/6cad5aa6-fc65-46b5-956d-f313eb481128)

![image](https://github.com/user-attachments/assets/3ceb3534-5a5a-4bbc-ad17-192cb30e535b)

<h1>---------------------------------------------------------</h1>
<br>




