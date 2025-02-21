![image](https://github.com/user-attachments/assets/4d7a7656-1897-429f-8afe-afbecf47bf82)

![image](https://github.com/user-attachments/assets/414e00a2-ba30-4a8b-9da3-97e913716161)

Tôi login bằng username:password random để bắt tạm request và ném vào trong intruder, brute bằng wordlist mà portswigger cho:

![image](https://github.com/user-attachments/assets/5fc8e68b-8c31-4f72-ae4a-d50e81775edc)

Sau đó hiện ra cái tên adserver kèm với response là invalid password, giờ thì dùng adserver để brute password

![image](https://github.com/user-attachments/assets/16c75b74-dd21-464f-bfb9-49c9f1634bb2)

Thêm được quả pasword là michelle

![image](https://github.com/user-attachments/assets/a05e9c2c-079d-47e4-9f36-91ce7aac689f)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/b2fc8705-2aac-4d00-9170-a41913f3c762)

![image](https://github.com/user-attachments/assets/adfaee84-8071-456b-a834-f4749dab7cd1)

![image](https://github.com/user-attachments/assets/94006d3d-abed-4c20-b97c-bad17459ced4)

![image](https://github.com/user-attachments/assets/98810bf3-842a-4af2-9e0d-38e6fe8cbdad)

Bài này tôi hơi ngơ, đang hí hoáy thử login wiener:peter lấy cái 2fa xem nó như nào, sau đó tôi nhập bừa và logout, lúc sau mới thấy có cái để check email, vô thử check mail rồi out ra login carlos:montoya, sau đó tôi đang bấm nút thoát nhằm vào wiener:peter để nhập thử thì nó bảo solved
Tóm lại là tôi vô tình giải được mà không có biết

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/444a8fa1-066d-4e66-9846-c26a96fbff2b)

![image](https://github.com/user-attachments/assets/7e93afe9-9b0f-43a2-af9d-a2537f6d7023)

![image](https://github.com/user-attachments/assets/e4bf43db-ea38-49a4-a632-7adeb752062f)

![image](https://github.com/user-attachments/assets/fd1d3be1-adf6-4fd0-af30-2f14312fdadf)

Test qua qua cái chức năng thì tôi thấy bấm quên mật khẩu là nó gửi link về mail, khi bấm vào link là nó dẫn thẳng đến đổi mật khẩu, tôi bật cái intercept lên và nhập mật khẩu mới

![image](https://github.com/user-attachments/assets/f9bd3ad5-9bbf-44ae-bd27-c4ddbc3e6c71)

Nhập xong thì trong cái request có chứa username cần thay đổi, đổi thành carlos là xong

![image](https://github.com/user-attachments/assets/8503b081-8bb2-420f-98d8-f15f2baa5158)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/7837f255-3968-46c3-81d6-6c9eef6e7580)

Tôi bắt cái request login và thử brute username trước 

![image](https://github.com/user-attachments/assets/659bd638-5a66-4a44-baca-1ed50ed4c3d5)

Có vẻ bài này đã cải tiến, chơi cái username or password rồi nên đổi lại cách làm

![image](https://github.com/user-attachments/assets/f238e60d-978d-4f9b-9c8a-c4f0e757a0ce)

Thôi thì tôi dùng Cluster bomb attack để brute, tức là kiểm tra tất cả các tổ hợp có thể giữa hai wordlist username và password, cái nào dính thì dính 

![image](https://github.com/user-attachments/assets/bf908c59-7efc-4ca9-862a-69528d4360a7)

Đây rồi đây rồi username=apps&password=nicole

![image](https://github.com/user-attachments/assets/7384b027-d6e5-4d98-a618-68d441fa5e9a)

Còn 1 cách nữa là brute username, username đúng thì sẽ là "Invalid username or password" và sai thì là "Invalid username or password.", nó khác nhau ở dấu . và tôi không có để ý chi tiết này

![image](https://github.com/user-attachments/assets/130e187c-4423-4ebf-bd80-87e3b8ab7e59)

![image](https://github.com/user-attachments/assets/0f10f589-296d-4d72-b408-df108e4498f4)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/98e7bf5e-a61b-466c-a7e0-40c670150610)

Cái thời gian phản hồi, tôi xếp xuôi hay ngược thì có đến vài cái, không biết là như nào cho dù có lấy cái wiener:peter đúng thì nó vẫn...

![image](https://github.com/user-attachments/assets/a8e2df2e-a634-46c0-978b-8f576ddf0fea)

![image](https://github.com/user-attachments/assets/ec8e29db-fff7-4874-9b8c-d941f3ebeacb)

Dùng lại trò cũ vậy...

![image](https://github.com/user-attachments/assets/3b74f061-ab19-4d1c-8288-eaea7d62ec7f)

Treo đấy 1 lúc rồi quay lại thì thấy cái này, bruh

![image](https://github.com/user-attachments/assets/af6aefdd-aa85-4de9-ab65-28f4ef32682a)

Sau 1 lúc đọc tài liệu thì cuối cùng tôi cũng ngộ ra

![image](https://github.com/user-attachments/assets/846eac66-9c48-4c11-ac85-a0d8fc653aea)

![image](https://github.com/user-attachments/assets/ca33fc05-ab85-4110-bbd2-65efea830d33)

Spam cái mật khẩu dài dài ra bởi vì khi đưa vào server, nó sẽ bỏ qua các invalid username và chỉ chỉ valid, việc mật khẩu quá dài sẽ gây lên tình trạng mất thời gian và tôi kiếm được username là arlington, để kiếm chứng điều này thì có thể dùng username wiener

![image](https://github.com/user-attachments/assets/d90af675-099d-4da3-b3c5-80ff4ebb01ba)

![image](https://github.com/user-attachments/assets/78506e04-4270-4bcc-b87f-daa9afff757a)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f74210f3-dda7-4129-b549-540d2b72a0e8)

Sau khi brute thì nó như này đây:

![image](https://github.com/user-attachments/assets/ea7dbec1-b382-49a4-b9a8-a16c830b395b)

Sau 3 lần sai mật khẩu là nó như thế, tôi làm hẳn cái payload cách 1 phút gửi 1 lần:

![image](https://github.com/user-attachments/assets/4a30909c-de5d-4026-b888-ed92e68ee2bc)

Sau khi ngồi đợi, tôi tính qua qua có khoảng 100 cái password, tức là phải đợi 100p, tôi nghĩ là tôi nên tìm cách khác thay vì bỏ gần 2 tiếng đợi<br>

Sau 1 lúc nghịch thử thì tôi nhận ra quy luật, gửi sai 2 lần và lần cuối đúng thì nó được reset, tôi làm lại payload để cho nó tự chạy

![image](https://github.com/user-attachments/assets/9192a97e-1bf5-4381-83f4-edfe0f68c5af)

![image](https://github.com/user-attachments/assets/112d3726-32be-45e7-b841-024c352e433f)

![image](https://github.com/user-attachments/assets/59d3699a-c7db-4de7-92b5-aee90715cc5d)

Tôi chỉnh thành so le, 2 lần carlos và 1 lần wiener, cứ như vậy và để nhanh hơn thì tôi dùng python xếp cho dễ dùng:

![image](https://github.com/user-attachments/assets/5ce868f3-74ce-463f-a74c-d06eaa097857)

Và xong:

![image](https://github.com/user-attachments/assets/7c0fb508-5210-4e14-a7fc-6800dcfc6d79)

<h1>---------------------------------------------------------</h1>
<br>



















