![image](https://github.com/user-attachments/assets/777af23d-4595-452c-9caa-6ae457eeb17f)

Đây là phần đăng nhập, có thể dùng username hoặc email:

![image](https://github.com/user-attachments/assets/e85bfdb9-0ea8-4165-a11e-3d75ee6123a5)

Sau khi tôi đăng nhập thì hiện ra cái này:

![image](https://github.com/user-attachments/assets/a2a360a2-4175-4481-9214-c52787666b4e)

Để ý cái req POST này thì nó gửi email, username và token đi để đăng nhập vào:

![image](https://github.com/user-attachments/assets/48535a5a-2056-4017-9788-98aa97d62487)

Tôi thử giữ nguyễn token và đổi username, email:

![image](https://github.com/user-attachments/assets/aafc3c12-5db2-4e68-88db-6d442f002e1f)

![image](https://github.com/user-attachments/assets/3fdf9c89-0d7e-4640-85d7-c4e1cd631aa5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/cd07e05f-1d2f-4f2d-b5e6-568667ed9f05)

Nếu để ý ở cái req GET /auth/N_xs7k6hm-N8hyLImCFs_  thì có cái host 

![image](https://github.com/user-attachments/assets/cab85b87-9ec8-42d9-9718-9866c5b50387)

Nếu chịu khó tra google thì tìm được cái [OAuth Endpoints](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_endpoints.htm&type=5):

![image](https://github.com/user-attachments/assets/fed06646-de2b-4328-acd5-5edb20e340f4)

Đi theo đường link đấy thì ra cái này:

![image](https://github.com/user-attachments/assets/89629745-0657-4656-9173-1e57576c5e96)

Và có thể đăng kí bằng POST /reg dưới dạng json:

![image](https://github.com/user-attachments/assets/76358574-18de-4207-8bea-d74a52d3024c)

Ở response thì có cái client id và nhìn cái req GET /client/ogph0p6bgprolz19gnsfa/logo  cũng là client id:

![image](https://github.com/user-attachments/assets/c18d97ac-02e3-4f57-9c1d-7eb642a5fc0a)

![image](https://github.com/user-attachments/assets/48a4a4f7-fad0-441a-9030-38d855407e6b)

Thêm cái `"logo_uri":"https://qtncodu2t1992nib5lpg11ylkcq3ev2k.oastify.com"` này vào, link là từ burp collaborator:

![image](https://github.com/user-attachments/assets/59ae5c54-4df0-49b7-a6f2-69a6dbde4b1d)

Lấy cái client_id thay cho client_id của req này để test xem có hoạt động không:

![image](https://github.com/user-attachments/assets/19168146-cee7-46d9-9857-2caa2f670172)

Sau khi nhận được req ở collaborator thì chuyển cái logo_uri sang http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/ và làm tương tự:

![image](https://github.com/user-attachments/assets/c57a2059-65fd-4df8-b5ba-c40fbe6de56b)

Gửi cái SecretAccessKey là xong

<h1>---------------------------------------------------------</h1>
<br>


































