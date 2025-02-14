![image](https://github.com/user-attachments/assets/594af6d7-14d6-46bb-8ca1-849dbca3dbec)

![image](https://github.com/user-attachments/assets/d2d037fc-8fe8-4d57-86fe-0391b2053160)

Vào thì thấy 1 cái ô nhập, tôi nhập thử thì dòng chữ có hiện lên màn hình:

![image](https://github.com/user-attachments/assets/c6999a43-5920-4046-9331-98d5121dd1af)

![image](https://github.com/user-attachments/assets/5fa498b4-a823-4cef-9794-da11dbf1df40)

Code không thấy được mã hóa và có dấu ' đi kèm theo, tôi thử payload `a' </h1> <script>alert('abc')</script> <h1>'lmao`, `a' </h1>` để kết thúc cái thẻ cũ và làm hẳn cái script mới, `<h1>` đằng sau là để nối cái đuôi

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

![image](https://github.com/user-attachments/assets/cc9cc861-553f-4234-b2e4-673008157d3b)

![image](https://github.com/user-attachments/assets/13236c10-352a-4555-a282-1a0e7e920ff8)

Đại khái thì nó lấy cái giá trị của searchTerms thôi, khi tôi nhập dấu > thì bị mã hóa thành `&gt;` nhưng mà lại không mã hóa dấu "

![image](https://github.com/user-attachments/assets/34815687-9bd8-44a9-83c8-b5b4058084eb)

Nhìn ở chỗ document.write thì có vẻ tôi sẽ khai thác được gì đó từ dấu " với payload `aa" onerror="alert(1)`, và không thấy xảy ra cái gì 

![image](https://github.com/user-attachments/assets/42e077df-87f9-48a7-a677-2c9d28ee8a60)

Gà quá nên tôi coi solution 1 chút thì thấy `'-alert(1)-'`

![image](https://github.com/user-attachments/assets/02f06c65-f9d5-4d93-9e0e-260c1de62c82)

Có thể thay 2 dấu - thành dấu khác như + / % & * |, mấy cái liên quan đến phép tính ấy, vì cái đường dẫn sẽ trở thành src="/resources/images/tracker.gif?searchTerms=-alert(1)- và nó là đường dẫn hợp lệ, để dê hiểu hơn thì https://security.stackexchange.com/questions/196096/why-does-my-stack-contain-the-return-address-to-libc-csu-init-after-main-is-in đây là đường dẫn hợp lệ và có dấu - trong đó, đôi khi có thể 1 số web sẽ dùng dấu + *..., vậy nên có xuất hiện 2 dấu - kia để lưu không đánh động đến cái alert(1), dấu ' kia thì trong document.write nên biết rồi, việc làm như này là để lợi dụng thẻ script ở ngoài 

![image](https://github.com/user-attachments/assets/5c724f43-3dca-4994-88e5-a0a5710c61b2)

Cái thẻ tôi bôi đen ấy, nó dùng để thực thi cái alert bên trong nên là cái đấy nó chạy được, vậy thôi

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/c805b10c-3d7d-4a17-9a38-b89faf42f5e0)

![image](https://github.com/user-attachments/assets/2e7327a6-77f9-4a68-a7c2-3866bf8e6160)

![image](https://github.com/user-attachments/assets/8beb273c-6207-4ce1-bf78-aa69638273b8)

Trong đoạn code này, có 1 list là tores = ["London","Paris","Milan"], nó lấy giá trị từ tham số storeId, nếu store tồn tại, nó được thêm làm một <option> được chọn, để ví dụ dễ hiểu thì nếu để storeId là hello hay gì đó thì ở chỗ chọn sẽ xuất hiện:

![image](https://github.com/user-attachments/assets/3fa68b8a-f7d4-4e2e-9cce-f07cc30022c5)

![image](https://github.com/user-attachments/assets/50d60e95-1c8a-4f88-b409-e7e228b9d393)

Và cả cái này bên trong thẻ select 

![image](https://github.com/user-attachments/assets/b50c575e-a652-4cca-b57e-21c9989a2ef8)

Và chỉ vậy thôi

![image](https://github.com/user-attachments/assets/25853b23-ae8b-4e4b-b5d6-cb4dd4b7cdbd)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f162e2a1-8cd1-4812-9f9a-a6a7fdb028c7)

Cái web này nó mã hóa <>" rồi nên phải dùng cách không liên quan đến mấy cái dấu đấy, dùng cái Wappalyzer thì có thấy AngularJS 

![image](https://github.com/user-attachments/assets/a926a19e-be91-4543-96d4-ffd8d345b7d8)

Tra trên mạng thêm về cái AngularJS expression

![image](https://github.com/user-attachments/assets/39a61d6e-9e00-4c24-8885-2ce491091661)

Khi tôi thử `{{ 5 + 5 }}` vào thì kết quả trả lại à 10 

![image](https://github.com/user-attachments/assets/0d1e4ab2-c1de-43a6-9a3b-0d7c6eac0170)

Đây là kết quả sau khi tôi dùng payload `{{alert(window.origin)}}`

![image](https://github.com/user-attachments/assets/282489e4-fe5c-403b-90ed-635005474ed0)

Tôi lên gg và search được 1 trang của HackerOne, [đây](https://hackerone.com/reports/141463)

![image](https://github.com/user-attachments/assets/517f7e6c-5ea5-4cea-abcc-872e2facc0cf)

![image](https://github.com/user-attachments/assets/44adbafd-ba7a-4236-b8f0-db6980840553)

Tôi đổi cái dấu [[ thành {{ và payload nó như này `{{constructor.constructor('alert(window.origin)')()}}`

![image](https://github.com/user-attachments/assets/b2fb1c46-b54b-4192-b89d-ec5044e682cd)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9f482d29-0db2-4c63-b000-58e39e99a61d)

Bật intercept và search gì đó:

![image](https://github.com/user-attachments/assets/ebb06977-6868-424e-a9ea-8226e5bab514)

![image](https://github.com/user-attachments/assets/814ab1af-9503-4315-bb36-0628f5a0db4d)

Tôi để ý đến cái `search('search-results')` này

![image](https://github.com/user-attachments/assets/447b2a3d-4971-4802-a24e-caedcf832f54)

![image](https://github.com/user-attachments/assets/aadd06a9-337b-4ea6-9ea9-bdbf3a9f7e90)

Tôi thử với payload `lmao"}` thì

![image](https://github.com/user-attachments/assets/fc2535b3-2d4b-4c45-a1d0-6bfbb9148b08)

Có cái filter dấu " bằng cách thêm \ vào trước nó, thử với payload  `lmao \" lmao` thì chữ đổi màu bởi vì trong cái \" thì khi thêm \ vào trước " nó sẽ thành \\", từ đó dấu \ sẽ thành con tốt thí, biến thành string 

![image](https://github.com/user-attachments/assets/944e4d0d-95f4-4f9d-bc9a-36dd90f41194)

Vấn đề bây giờ là dấu " ở sau, sau khi chèn `lmao \"} alert(window.origin)` thì nó ra như này:

![image](https://github.com/user-attachments/assets/7406dbaa-82c8-4d78-b8d7-9777ed0a21c2)

Xong, thấy nó ghi đã solve, với cả solution dùng payload này `\"-alert(1)}//`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/fe75c818-4c46-4ba9-8397-e92da5018908)

Test thử 

![image](https://github.com/user-attachments/assets/4c81e658-863c-4939-bbca-e3d72afd0c19)

Đây là cái code nó filter đây:

![image](https://github.com/user-attachments/assets/432ac9af-81db-4320-9696-eb0906c4359a)

Bỏ qua cái trên đi, đọc src code thì nhận ra nó không hề dùng vòng lặp, tức là nếu tôi dùng nhiều <> thì có vẻ sẽ được, tôi dùng payload `<><><><script>alert(origin.window)</script>` 

![image](https://github.com/user-attachments/assets/a8363986-9ebd-4aeb-93db-4cf45064279e)

Dùng xong thì tôi quên mất đây là DOM xss, tôi xoay sang `<><><><img src="lmao" onerror="alert(1)">`

![image](https://github.com/user-attachments/assets/87dc5998-f510-420f-856c-3f3ca7fb5742)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/549ed542-e65a-4406-bec6-968b1730937a)

Ầu

![image](https://github.com/user-attachments/assets/1c357d6c-c1fa-4bf5-a243-c0326bfe589d)

Tôi chạy FUZZ để mò payload `ffuf -u https://0a8e00b1031a85a9828cacc6007d0016.web-security-academy.net/?search=FUZZ -w payload_tag_event.txt:FUZZ`

![image](https://github.com/user-attachments/assets/bebf8d86-5568-4414-91d1-ce97ddd0b0e3)

À tôi quên là bên PortSwigger nó chặn bên thứ 3, quên, tôi chạy intruder thì được 1 số thẻ body với custom là 2 thẻ không bị cấm:

![image](https://github.com/user-attachments/assets/d7207196-cfc7-4823-ae2c-ca48c0e953e3)

Trong 1 đống các payload thì tôi thấy cái onresize nó ngắn ngắn, search thử thì thấy chức năng là chạy alert khi chỉnh lại kích thước của cửa sổ trình duyệt, nếu nạn nhân điều chỉnh cửa sổ thì đi 

![image](https://github.com/user-attachments/assets/f870c75e-728b-4a52-bef2-f7d876a71a9c)

Thử `<body onresize="print()" onload="window.resizeTo(800,600)"></body>` thì thấy không được do cấm cái window kia

![image](https://github.com/user-attachments/assets/2493a51a-e477-4c44-b457-945e4598ddcb)

`<iframe src="https://0a8e00b1031a85a9828cacc6007d0016.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'>`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/ffba47a3-fb46-45b6-a463-186bd11d8e01)

Tất cả đều bị lọc trừ cái custom:

![image](https://github.com/user-attachments/assets/f580f7b1-6d95-454f-bef0-ebbe56dce8e0)

Sau khi thử 1 đống payload thì chạy được payload `<custom tags onmousemove="alert(1)" style=display:block>test</custom tags>` là ngon rồi

![image](https://github.com/user-attachments/assets/88b325a3-f549-4230-a5fe-ce4f10e8d1b8)

Tôi tìm được quả payload `<custom id=x onfocus=alert(document.cookie) tabindex=1>` này hay phết 

![image](https://github.com/user-attachments/assets/8e656d8f-d588-498b-8ce1-16fe0a37d544)

Tôi gà quá nghĩ không ra, xem solution thì thấy có thêm cả #x vào cuối payload, vì cái đấy để nó tập trung vào cái x kia, nó sẽ tự động chạy xss luôn, còn không có thì không tự động, phải làm thủ công

![image](https://github.com/user-attachments/assets/1775a5da-1692-4c16-b743-253e8eae0fb4)

`<script>
location = 'https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
</script>`

Payload ở solution đây

![image](https://github.com/user-attachments/assets/c3fba808-32c1-4dbb-8d32-e49aa091b31a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/10166b71-96a8-491d-8a1c-313fe7fabf9f)

![image](https://github.com/user-attachments/assets/f7e6a8ed-b6a1-4432-b8be-20fd4100d515)

Đề bảo thả cho cái tag svg, tôi lấy tạm trên mạng vứt bừa vào thì ra:

![image](https://github.com/user-attachments/assets/a99432bc-0dd2-4c6f-b17e-c5e99420a0ea)

Chặn rồi, chặn cái onfocus rồi

![image](https://github.com/user-attachments/assets/eb0cf782-fee1-4579-9d4e-864f710a3274)

![image](https://github.com/user-attachments/assets/8297cb39-3eb0-4937-9ca6-3b04d882974b)

Ưtf

![image](https://github.com/user-attachments/assets/ed967bbb-6db9-4de9-9b30-2e280c77e498)

Nãy đang hí hoáy dùng intruder cơ mà lỗi không hiển thị ô tấn công nên tắt đi bật lại, vào thì thấy nó giải xong 

![image](https://github.com/user-attachments/assets/dd6c9f33-f6f1-4dc6-959e-cc2ed2e6d1dd)

Payload đây `<svg><animatetransform onbegin=alert(1) attributeName=transform>`, nó không có chặn animatetransform và onbegin chỉ kích hoạt khi có mấy cái như animatetransform

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/4cdcadfd-ad6f-4ff0-a274-1db3a0691794)

Trước tiên phải tìm hiểu xem canonical link tag là gì 

![image](https://github.com/user-attachments/assets/3a793e93-1fc0-48aa-b910-276ba3bce7e1)

Vào thì không thấy chỗ nào để input luôn 

![image](https://github.com/user-attachments/assets/49c40727-eb1c-4e30-8b53-87830021ee7f)

![image](https://github.com/user-attachments/assets/203a21d0-24e2-400d-9a25-55f10c5caaca)

Tôi nghĩ là tôi nên làm đó để chèn được vào đây 

![image](https://github.com/user-attachments/assets/9b7f4898-fdac-44c9-bcc0-6c18dfcc5930)

Khi vào 1 bài post thì nó hiện lên, sau 1 lúc mày mò thì ra: 

![image](https://github.com/user-attachments/assets/b8177e22-7838-4036-8de0-b2599f5da034)

Thêm dấu ' vào là chữ đổi màu ngay 

![image](https://github.com/user-attachments/assets/88f32289-d488-4d6e-98b3-a6cd3d660605)

Nghiên cứu về alt thì tôi tìm được cái này: 

![image](https://github.com/user-attachments/assets/3bf53d52-71d3-4885-b366-314d3103a524)

![image](https://github.com/user-attachments/assets/eeef8eb6-788b-4fd8-a90f-3bfbed8e01f4)

Thêm hành động khi dùng onclick nữa là xong

![image](https://github.com/user-attachments/assets/ef7f26c0-5668-481f-9c50-8d338c83d328)

Quên mất dấu cách, bỏ dấu cách đi: 

![image](https://github.com/user-attachments/assets/aef14f4c-5efc-475e-8e42-bf794f7f4471)

`view-source:https://0aa9009e04b21b7d805dfd6c00bf0098.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/792449e2-e10e-4c26-8a0d-7000a89c598d)

![image](https://github.com/user-attachments/assets/47b9164b-2d92-4ad5-a0fb-6d6549b4eb9d)

Khi tôi nhập aa'aaa thì đã được thêm dấu \ để ngăn dấu ' và dấu \

![image](https://github.com/user-attachments/assets/170f9b79-9436-4594-9f37-8880c60a5161)

Tự nhiên tôi thắc mắc sao nó không ngăn cả dấu <> các thứ? 

![image](https://github.com/user-attachments/assets/52035131-aa71-44a9-bb23-b36773106938)

![image](https://github.com/user-attachments/assets/be60253b-63ab-43cc-b714-862c11288dcd)

`</script><script>alert(1)</script>`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/199701f5-1929-48b4-85ee-04b286c72d6b)

Dấu " và >< đã được filter và vẫn giữa ' nhưng dấu \ không bị filter 

![image](https://github.com/user-attachments/assets/8c2b6ffa-6cea-4160-8821-670c2b2183e2)

![image](https://github.com/user-attachments/assets/b9e52e95-3175-4053-be11-5ed757fc882c)

Tôi nhập vào aaaa\' trong code sẽ filter thành aaaa\\', khi đó dấu \\ đã biết thành string 

![image](https://github.com/user-attachments/assets/04e5a1c9-aa1f-4f4d-8cb4-ebb2f2db83df)

Đoạn thừa ở sau thì dùng comment để cho nó biến mất :

![image](https://github.com/user-attachments/assets/11512a32-8927-48e7-b8da-df9cb8058615)

Để trong cái này cho dễ nhìn chứ ở kia không nhìn được 

![image](https://github.com/user-attachments/assets/d18c39a8-ec51-4375-ba42-cb34613b8b6e)

![image](https://github.com/user-attachments/assets/4f5b3724-0164-4d5b-ac1b-ccb9abf24a00)

![image](https://github.com/user-attachments/assets/c3d2e9b5-ffc7-4791-a986-1751df73a5da)

`aaaa\';alert(1)//` 

<h1>---------------------------------------------------------</h1>
<br>














































