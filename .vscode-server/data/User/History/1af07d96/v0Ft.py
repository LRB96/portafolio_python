from datetime import datetime
import pytz

seoul_timezone = pytz.timezone("Asia/Seoul")
seoul_date = datetime.now(seoul_timezone)
print("Seúl, Corea del Sur: " + seoul_date.strftime("%d, %m, %Y, %H, %M, %S"))
f"Seúl, Corea del Sur: " + {seoul_date.strftime("%d, %m, %Y, %H, %M, %S")}
