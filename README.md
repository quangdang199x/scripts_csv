### Tiến độ thực hiện

+ [x] Thiết lập các inputs để nhập các thông số cần thiết;

+ [x] Làm được phần code xử lý và tính toán các thông số đầu vào;

+ [x] Có phần code dùng để xuất được một file chứa giá trị của một inverter mẫu;

+ [x] Kiểm tra lại tính chính xác của các thông số của một inverter trước khi export ra file inverter.csv;

+ [x] Xử lý code để xuất được một file chứa giá trị cần import vào databases của tất cả các inverter trong site;

+ [x] Kiểm tra lại giá trị trước khi export ra file inverter.csv chứa tất cả inverter trong site hoàn chỉnh;

+ [x] Bổ sung phần các giá trị inputs sử dụng YML;

+ [x] Tạo hàm để xuất thời gian mà không cần phải đổi bằng tay (tạo 1 file CSV chứa thời gian);

+ [x] Tạo hàm để xử lý việc xuất được một file "inverter.csv" chứa được nhiều ngày;

+ [x] Tìm cách chỉnh phần add tháng mới.

+ [x] Tối ưu hóa code cho nhiều Inverter hơn.

# Update database from csv - Single day

## Procedure
1.	Determine the lost date or time period 
2.	Download inverter csv file from webportal
3.	Calculate active energy of inverters at a single datapoints at every 15 minutes 
4.  Create new csv file with new data points for all inverters 
4.	Validate the site's summary active energy for the whole day 
5.	Import the new *.csv file to Solarmon database

# Requirements
## Input
-  Inverters' single day csv file from ABB/SMA webportal (15mins resolution)

-  Active energy value: 

    + lower bound: last Active energy

    + upper bound: last Active energy + day's active energy

## Output
- Active energy at every point in the day for every inverter

- Combined CSV file to import to Solarmon database

## Validation
- Site's summary active energy vs summary of all inverters' active energy in a single day

# create_csv_file

#Bài toán dùng để tính toán dailyEnergy:

Thư viện sử dụng để tạo file *.csv là: pandas, version: 1.3.1

A/ Inputs:

1/ Nhập vào các header cần thiết: time, asset, scope, active_power, active_energy.

    + Phần "time" sẽ lấy từ file inverter1.csv để dễ chỉnh sửa thời gian.

    + "active_power" sẽ lấy từ file download trên hãng.

    + "asset, scope" --> tạo hàm để nhập, hoặc nhập tay bằng lệnh input().

    + "active_energy" sẽ được tính toán dựa vào phần active_power đã download.

2/ Tính toán phần active_energy:

    + Xác định được điểm tham chiếu của từng inverter (active_energy).

    + Xác định được daily_energy của mỗi inverter trên website của hãng.

    + Dùng điểm tham chiếu cộng/trừ cho daily_energy để lấy được hai điểm chặn trên và chặn dưới.

    + Tiến hành chia phần daily_energy theo active_power, có thể cộng phần dư hoặc trừ phần thiếu vào các peak power. Hoặc là chia theo tỉ lệ gì đó dựa theo active_power của từng inverter.

    + Dùng lệnh kiểm tra lại các số liệu tính toán xem thử đã chính xác chưa.

B/ Output:

    + File inverter.csv của từng inverter, sau đó gộp thành một file chung --> import vào databases.

    + Hoặc là xuất ra 1 file chung của tất cả inverter trong site --> import vào databases.  

### Quy trình thực hiện việc tạo và xuất một file CSV:

+ File "create_csv.py" chứa các function cần thiết. File "Run.py" dùng để chạy chương trình xuất file CSV. File "inputs.yml" dùng để nhập các thông số đầu vào và đầu ra.;

+ Giả sử đã xác định được Site cần thực hiện, ví dụ ở đây là site Linh Trung 8, ta tiến hành theo các bước bên dưới;

 #### Các bước tiến hành:

 + Xác định được các ngày còn thiếu, số lượng inverter trong site và điền vào dòng code: "number_Day" và "number_inverter". Hiện tại chỉ mới nhập được tối đa 7 ngày và tối đa 7 inverter. Số lượng này có thể tăng thêm.

 + Vào "Solarmon" -> "LT8" -> "Devices" -> "Edit Device" -> Copy phần "ID" để lấy Asset của inverter; 

 ![image](https://user-images.githubusercontent.com/87714271/130497398-baf6264f-51d0-44b5-87f5-8640b01c7a72.png)

 + Sử dụng "ID" vừa copy và vào database paste vào mục tìm kiếm để lấy "Lastest active energy" và "Scope" của inverter có ID đó. Làm tương tự cho các inverter khác. 

 ![image](https://user-images.githubusercontent.com/87714271/130497905-4b3ef417-8708-484e-9080-a47f4a813ca2.png)
 
 + Download file chứa phần active power của tất cả inverter trong site về. Copy phần "Entity Name" và phần "Active Power" (theo đúng thứ tự) sau đó paste sang file "download.xlsx"; 

 ![image](https://user-images.githubusercontent.com/87714271/130495687-456107b5-aef5-4664-b6e0-0ef7206e1550.png)

 + Lên website của hãng và lấy giá trị total daily energy của tất cả inverter trong site ở ngày cần làm. Nhập giá trị đó vào: "total_dailyEnergy_site = None" ở file "inputs.py"; 

 ![image](https://user-images.githubusercontent.com/87714271/130494020-fcf82d78-5927-4b77-9dd5-dbc57677aa19.png)

 + Xác định được web_dailyEnergy ứng với mỗi inverter trong site (lấy giá trị này ở website của hãng inverter); 

 ![image](https://user-images.githubusercontent.com/87714271/130494487-73e6562b-f56f-4456-915f-73505ff10838.png)

 + Nhập vào các asset, scope, mốc latest day energy (đã lấy các giá trị này ở database bước trên);

 + Sau khi xác định được các mục cần thiết, nhập chúng vào các dòng lệnh tương ứng.

 + Chạy file "Run.py" và import file "inverter.csv" vừa tạo được vào database.

 + Hình ảnh trên Website của hãng: 

 ![image](https://user-images.githubusercontent.com/87714271/130494382-165a658c-8408-42a8-a950-639fd16a7feb.png) 

 ![image](https://user-images.githubusercontent.com/87714271/130494020-fcf82d78-5927-4b77-9dd5-dbc57677aa19.png)


 + Hình ảnh thu được trên solarmon sau khi import file "inverter.csv" vào database: 
 
 ![image](https://user-images.githubusercontent.com/87714271/130495463-118abe90-21a3-44e2-b2f4-2670aed9265c.png) 

 ![image](https://user-images.githubusercontent.com/87714271/130495511-1a4a7bda-6eaa-48f6-81e7-e94a10373ee6.png) 

 ![image](https://user-images.githubusercontent.com/87714271/130499788-7a51ba8e-f74d-468b-a42d-987e8a6e0423.png)


 
