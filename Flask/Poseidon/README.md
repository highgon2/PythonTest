# Required Modules
  - Flask
  - Flask-Migrate
  - Flask-WTF
# JSON format
```json
{
  "imei":"860517046333086",
  "datetime":"21/07/27 021:45:44",
  "rpm":0,
  "coolant":0,
  "oil_pressure":0,
  "oil_temperature":0,
  "voltage":49,
  "fuel":0,
  "fault_code":[
    "P0223",
    "P250D",
    "P0238",
    "P0117"
  ],
  "gps_date":"270721",
  "gps_utc":"124902.00",
  "gps_latitude":3726.244816,
  "gps_longitude":12708.775338,
  "gps_knots":0.0,
  "gps_direction":241.4
}
```
  - fault_code / gps data 생략 가능
  - 그 이외의 데이터는 생략 불가