### Tiến độ thực hiện

+ [x] Thiết lập các inputs để nhập các thông số cần thiết;

+ [x] Làm được phần code xử lý và tính toán các thông số đầu vào;

+ [x] Có phần code dùng để xuất được một file chứa giá trị của một inverter mẫu;

+ [x] Kiểm tra lại tính chính xác của các thông số của một inverter trước khi export ra file inverter.csv;

+ [x] Xử lý code để xuất được một file chứa giá trị cần import vào databases của tất cả các inverter trong site;

+ [x] Kiểm tra lại giá trị trước khi export ra file inverter.csv chứa tất cả inverter trong site hoàn chỉnh;

+ [ ] Bổ sung phần các giá trị inputs sử dụng YML;

+ [ ] Tạo hàm để xuất thời gian mà không cần phải đổi bằng tay (tạo 1 file CSV chứa thời gian);

+ [ ] Tạo hàm để xử lý việc xuất được một file "inverter.csv" chứa được nhiều ngày;

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

+ File "create_csv.py" chứa các function cần thiết. File "main.py" dùng để chạy chương trình xuất file. Mọi thao tác sẽ làm trên file "main.py";

+ Chỉnh lại thời gian trong file "time.csv" cho đúng với ngày còn thiếu;

+ Download file chứa phần active power của tất cả inverter trong site về. Copy những thứ cần thiết sang file "download.csv";

+ Xác định được total daily energy của tất cả inverter trong site ở ngày cần làm. Nhập giá trị đó vào: "total_dailyEnergy_site = None" ở file "main.py";

+ Xác định được số lượng inverter trong site;

+ Xác định được web_dailyEnergy ứng với mỗi inverter trong site (lấy giá trị này ở website của hãng inverter);

+ Xác định được asset, scope, mốc latest day energy (lấy các giá trị này ở database);

+ Sau khi xác định được các mục cần thiết, nhập chúng vào các dòng lệnh tương ứng.

+ Chạy file "main.py" và import file "inverter.csv" vừa tạo được vào database.