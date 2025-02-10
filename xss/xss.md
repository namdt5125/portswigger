![image](https://github.com/user-attachments/assets/eae5fabd-d9d5-4e88-9226-a1cdb3b2d491)![image](https://github.com/user-attachments/assets/d7bcadf8-b063-46a4-930c-c6621899da8f)![image](https://github.com/user-attachments/assets/594af6d7-14d6-46bb-8ca1-849dbca3dbec)

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

![image](https://github.com/user-attachments/assets/8f145eda-5241-40c6-b12d-66c7c64567a5)

![image](https://github.com/user-attachments/assets/8ea46627-d927-490b-a2ff-04fff7df40cf)

Đầu tiên $(window).on('hashchange', function() là để lắng nghe khi phần hash tức là # trong URL được thay đổi, nó sẽ tự động lăn xuống bài viết chứa nội dung đó, chính là cả cái blog-list kia, ở trong thẻ <h2>, window.location.hash.slice(1) là trả về phần hash của URL bao gồm cả dấu #, ví dụ dễ hiểu:

![image](https://github.com/user-attachments/assets/b5310f2e-2410-4e8f-b99a-596c8a896410)

![image](https://github.com/user-attachments/assets/51a27eaa-95c8-4881-87de-f3fe09d524cb)

Hoặc cũng có thể 1 phần trong cái chuỗi dài dài đấy do có cái :contains, còn đoạn sau là nó làm việc với URL để lấy ra nội dung, bỏ dấu # do có slice(1), lấy từ vị trí thứ 2 còn cái `if (post) post.get(0).scrollIntoView();` thì là nhảy xuống bài post đầu tiên chứa cái chuỗi đấy thôi 

![image](https://github.com/user-attachments/assets/5f4212c3-1545-46b2-bc1e-6fd22f435201)

Dùng payload `#lmao" <img src="lmaoo" onerror="alert(1337)">` là được, để bảo dùng print() nên tôi đổi thành `#lmao" <img src="lmaoo" onerror="print()">`, do lần đầu nên chả biết solve kiểu gì, tôi vào xem cái solution thì nó bảo exploit:

![image](https://github.com/user-attachments/assets/ccd200cb-a603-42d7-b9a0-cec6852cb4d4)

Giờ thì được rồi

![image](https://github.com/user-attachments/assets/0f2c63cc-cef1-4f65-b0a0-f0647a665a07)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/166feb60-cc43-4413-98f5-dea213bdc3a7)

Sau khi tôi search aaaa thì nó ra value là aaaa 

![image](https://github.com/user-attachments/assets/34bea22b-892c-435e-b59e-330b95734f3e)

Dấu > được mã hóa thành `&gt;`:

![image](https://github.com/user-attachments/assets/9b8d07d1-b2ae-45b1-9e91-dadf5680fb92)

Có vẻ khó để bypass, thôi thì dùng tạm cách khác làm sao không liên quan đến dấu <>, khi tôi nhập " vào thì màu ở chỗ value lạ lắm:

![image](https://github.com/user-attachments/assets/6fd318a3-c0a1-4418-a9d8-3254e4134d95)

![image](https://github.com/user-attachments/assets/382aa3c1-a556-44d8-85e7-8eaeca4f4634)

Tôi vứt lên cái html editor của w3school cho dễ nhìn hơn, có vẻ tôi sẽ phải kiếm payload nào có dấu " để thoát khỏi string trong value mà không liên quan đến <>

![image](https://github.com/user-attachments/assets/2f961c2f-ddd3-4519-a338-49816ebeb286)

Tôi search được cái này và tôi test thử payload `"onclick="alert(1337);`, dấu " ở đầu là đóng hết cho value, thêm gì đó vào trước " cũng được, tùy, ở cuối không có " do cái dấu đóng " ở value có sẵn rồi, và alert sẽ xuất hiện khi ấn vào ô tìm kiếm:

![image](https://github.com/user-attachments/assets/fe5cfd11-f816-4be1-9f07-2067ba06327a)

Hint bảo là phải hoạt động với nạn nhân, tôi thấy trong số các event thì cái onmouseout là nguy hiểm nhất vì chỉ cần di chuyển chuột là xuất hiện alert 

![image](https://github.com/user-attachments/assets/7b922f29-bbda-4751-8b2b-c2f6ef471aaa)

![image](https://github.com/user-attachments/assets/85b02494-6c06-4a8a-b263-8c9390eb1e68)

Tôi lay hoay không biết sao nó chưa hiện cái solve thì hóa ra tôi dùng nhầm onmouseout thay vì onmouseover, nhìn nhầm

![image](https://github.com/user-attachments/assets/738c5c67-033e-4c92-ae8c-3f91cc1bb01a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/7aa47588-8d86-46fc-8a40-87e904a630a6)

Vào chức năng của comment và dùng thử 

![image](https://github.com/user-attachments/assets/fff069ca-7d2f-43e0-9b66-311d6efec6f9)

![image](https://github.com/user-attachments/assets/0dd4fb52-794f-4f08-8de0-d08b76eae5d3)

Để ý đến phần website thì chức năng của nó là gắn vào tên, khi ấn vào tên là dẫn đến đường dẫn đó luôn, tôi thử luôn với payload `"><img src="xss" onerror="alert(1)` thì thấy đã được xử lý dấu <>" nên không làm gì được

![image](https://github.com/user-attachments/assets/2798357c-0f67-4e06-b8f0-4b707b74034e)

Không chứa <>" và lại còn liên quan đến thanh trình duyệt thì tôi nghĩ ngay tới javascript:

![image](https://github.com/user-attachments/assets/b12d82b4-48d0-401d-b0e8-3cb962971974)

![image](https://github.com/user-attachments/assets/b4bacbce-85fb-4997-b464-b309f878ed60)

Đã solve

<h1>---------------------------------------------------------</h1>
<br>













































