![image](https://github.com/user-attachments/assets/7148c292-427d-4648-be44-3ef286b1c8ee)

vào cái robots.txt có cái dir của admin 

![image](https://github.com/user-attachments/assets/b5cf07d5-6f48-4e6d-bdc2-19f02b3cc9d8)

![image](https://github.com/user-attachments/assets/dbfdef31-af5c-427b-acdc-77b9166609b8)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/73461095-2ca1-48bc-8663-a135f5f85457)

Lần này thì không có robots.txt nữa 

![image](https://github.com/user-attachments/assets/092ffa2a-a10c-441b-8d05-10277b368f06)

Fuzz thử thì ra có thế này 

![image](https://github.com/user-attachments/assets/8f3f09dd-f566-4da2-ad09-dbc2ff876527)

Sau 1 lúc tìm tòi, tôi đọc thử src code thì có cái `/admin-z8osff` 

![image](https://github.com/user-attachments/assets/08b8a790-9d05-407b-b821-2d18e87eee60)

![image](https://github.com/user-attachments/assets/7ebdcaa3-0fa5-4d2d-a279-374083ae4ed2)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/6e000587-75b7-4726-b1ce-8a276a12b209)

Lần này /admin chặn rồi 

![image](https://github.com/user-attachments/assets/53e604fa-eb4b-41e4-8553-86aecc8c0375)

Để ý đến cái cookie trong req vào admin 

![image](https://github.com/user-attachments/assets/0699170f-33b9-4c9b-a1cf-c4470379ce1c)

Ném và repeater, sửa thành true và gửi đi:

![image](https://github.com/user-attachments/assets/60626b48-076d-4ad6-b5bb-1f19cd732a54)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/827ddecf-0f00-4b64-a8df-5bffa5bd2de6)

Đăng nhập bằng wiener:peter

![image](https://github.com/user-attachments/assets/e3188080-ad80-40f5-81e5-2ff2991f69ef)

Khi dùng tính năng đổi email thì có hết các thông tin của user, có cả roleid

![image](https://github.com/user-attachments/assets/01d8f523-261b-46d9-a469-3be88f2d93a6)

Bật intercept lên và sửa roleid thành 2 

![image](https://github.com/user-attachments/assets/52f82c0b-72df-4308-bd1a-b499fe992a6d)

À làm thế nó không có đổi được, tôi thử thêm cái roleid vào dưới email xem như nào

![image](https://github.com/user-attachments/assets/93d79e58-b805-42d0-a81a-afdfc2d21ef5)

![image](https://github.com/user-attachments/assets/85de01dd-83aa-4697-8803-19a98de4eda1)

Và đã vào được 

![image](https://github.com/user-attachments/assets/a2082abc-d5a2-4c3d-a037-2730faf791cc)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/cbbaf760-3308-40bb-ad17-84550505d47e)

Sau khi login thì có cái API 

![image](https://github.com/user-attachments/assets/f88c39a5-a85c-42ce-94d6-7bdd9801966b)

Đổi id thành carlos là ra 

![image](https://github.com/user-attachments/assets/8a9b6de8-c4de-451e-a65e-c9962db15919)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/3ee93db1-ff43-48f8-b5ee-f414786bd367)

Lần này thì id nó nhìn dài dòng hơn 

![image](https://github.com/user-attachments/assets/f175188e-7626-4035-976c-c3c189c717a3)

Để ý trong các bài post thì có bài post của carlos 

![image](https://github.com/user-attachments/assets/e8c07d41-e2eb-43a7-8dae-03496b0f3dd7)

![image](https://github.com/user-attachments/assets/a5d7e1f9-931e-46e5-8c47-09662132d8e7)

Lấy được cái id của carlos 

![image](https://github.com/user-attachments/assets/5aff7dcc-de81-4e7a-b1f3-5aa0a2f02840)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/cd838bc2-3027-4d2a-b065-6c74ea7e2d40)

![image](https://github.com/user-attachments/assets/cfcf39a5-f7ee-4963-9858-0b9bd2e7348f)

Đổi cái id là vào được 

![image](https://github.com/user-attachments/assets/aae8191f-b912-4494-8162-fd161d5b5a19)

Nó chuyển hướng sang login khi đổi id thành carlos cơ mà vẫn xem được api 

![image](https://github.com/user-attachments/assets/b0755ce3-a17a-48b0-8433-6b95bbd3c8eb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/012e8f69-c6ce-40d7-a607-16e4d96ddb56)

Đăng nhập vào thì thấy quả mật khẩu bị che trước mặt

![image](https://github.com/user-attachments/assets/22d7d0e8-aab5-41dd-b63c-7dd913ed47f3)

Dùng cái f12 là ra hết 

![image](https://github.com/user-attachments/assets/99d3c945-4120-4ee4-8c4c-a7c966d5deaa)

![image](https://github.com/user-attachments/assets/5d07dc35-d132-4e00-89c7-61e3e620ef32)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/cb0c65be-8856-460c-9f34-0b1c546361a2)

Vào thì thấy live chat nên nghịch thử 

![image](https://github.com/user-attachments/assets/efdcce84-a94a-4f2f-9626-b373ce21f8fb)

Ấn view transcript thì tải mấy file có đánh số .txt về máy và trong đó là thông tin cuộc trò chuyện

![image](https://github.com/user-attachments/assets/71ae867b-baf5-4432-825d-d9d43aa5549b)

Tôi tò mò đổi thử thành mấy số linh tinh khác, đến số 1 thì có cuộc trò chuyện có chứa mật khẩu 

![image](https://github.com/user-attachments/assets/0d98dfa6-74b9-46d6-90d4-cb5101f6f5d5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/17ee5ebf-86d7-4e08-9d5d-97fc465bc79b)

Cái này không cho tôi truy cập vào /admin

![image](https://github.com/user-attachments/assets/045e8c80-0dcc-4493-a05e-322ed658a22b)

Sau khi tôi thêm cái `X-Original-Url: /admin` ở req / thì được:

![image](https://github.com/user-attachments/assets/735a469e-a074-4abc-aa9b-b3e6cbf06d38)

X-Original-URL là một HTTP header mà một số web framework hoặc proxy sử dụng để xác định đường dẫn gốc của yêu cầu trước khi nó bị thay đổi bởi proxy hoặc middleware. Nó thường xuất hiện trong các hệ thống có proxy ngược (reverse proxy) hoặc cân bằng tải, xóa carlos:

![image](https://github.com/user-attachments/assets/46d0574a-e3f0-406a-8166-ed74d9f7506b)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/4d71d737-4db7-4139-af84-4b6d8eb895cd)

Tôi vào và thử nâng quyền carlos lên admin 

![image](https://github.com/user-attachments/assets/016822e8-fbce-403a-99e9-1db4a35e817f)

Cái req đi qua admin-roles, wiener đang không phải admin, tôi thử dùng req đó với wiener:

![image](https://github.com/user-attachments/assets/2f684a62-5cd6-4b06-9d90-6de346b406e0)

Thiếu tham số, nhìn qua req này thì thấy nó là GET 

![image](https://github.com/user-attachments/assets/fff373cc-6299-460a-97c2-216538ed9623)

Tôi thêm tham số get vào thì vẫn không được 

![image](https://github.com/user-attachments/assets/66645661-fd16-40f2-a2c3-49c1f8c39d0e)

Quay lại chỗ admin thì ngạc nhiên thấy carlos đang làm admin 

![image](https://github.com/user-attachments/assets/343161ca-b50c-4c74-95e2-2d8abb5a3943)

Tôi thử với wiener và xong

![image](https://github.com/user-attachments/assets/40abb2c9-c5b4-407e-9c49-f97f123644db)

![image](https://github.com/user-attachments/assets/d46033e4-f6b0-465d-9e27-3c173d3b2c12)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/3afcf901-101b-4189-a67e-00e8c6e24650)

Lần này có hẳn "Are you sure?" để chắc chắn

![image](https://github.com/user-attachments/assets/f7b7315a-6aa9-4827-be6a-4f20caf65cce)

Cái request như này

![image](https://github.com/user-attachments/assets/e2635a9f-3356-43ea-bb19-62495edd809d)

Lần này có vẻ không vào được 

![image](https://github.com/user-attachments/assets/e5850690-de1a-4446-8bcf-b3fed453782a)

Tôi mở tạm cái ẩn danh, đăng nhập với wiener và đổi sang POST, thêm mấy cái tham số vào, chạy thử và carlos lên admin thật

![image](https://github.com/user-attachments/assets/0f4d685a-67f2-49ca-b29f-e48008a836c5)

Đổi tên và gửi req, xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/615167f8-377c-4848-877e-2ca4e901fcfb)

Ở bên admin là dùng GET để upgrade lên admin, tôi đăng nhập với wiener và làm giống hệt thì không có được 

![image](https://github.com/user-attachments/assets/f5790b28-0cc1-4b66-9e12-aa891d2c30de)

Do tên đề bài có chữ Referer và kết hợp nhìn thấy bên admin cũng có `Referer: https://0acf00ba047b4bb28610e93f00fd0094.web-security-academy.net/admin` nên tôi copy ném vào:

![image](https://github.com/user-attachments/assets/f04e2438-12f3-4228-b7b7-985680b95e42)

Xong

![image](https://github.com/user-attachments/assets/ba4ca56f-0821-42aa-a2bd-48c29d37ce20)

